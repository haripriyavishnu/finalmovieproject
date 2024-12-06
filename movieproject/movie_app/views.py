import datetime
from django.core.files.storage import FileSystemStorage
from django.http import HttpResponse
from django.shortcuts import render, redirect

# Create your views here.
from movie_app.models import Login, User, Admin, Movie, Rating, Review


def login(request):
    return render(request,'login.html')

def logout(request):
    request.session['lid']=''
    return HttpResponse('''<script>alert('Logout');window.location='/'</script>''')






def userpage(request):

    return render(request,'userpage/userindex.html')

def adminpage(request):
    return render(request,'adminpage/adminindex.html')


def add_user(request):
    a=User.objects.all()
    return render(request,'userpage/user.html',{'data':a})


def add_user_POST(request):
    username=request.POST['username']
    firstname=request.POST['firstname']
    lastname=request.POST['lastname']
    email=request.POST['email']
    password=request.POST['password']


    a=Login()
    a.username=username
    a.password=password
    a.type="user"
    a.save()


    b=User()
    b.username=username
    b.firstname=firstname
    b.lastname=lastname
    b.email=email
    b.password=password
    b.LOGIN=a
    b.save()

    return HttpResponse('''<script>alert('hello welcome');window.location='/'</script>''')



def view_profile_user(request):
    v=User.objects.get(LOGIN_id=request.session['lid'])
    return render(request,'userpage/viewprofileuser.html',{'data':v})


def login_post(request):
    username=request.POST['username']
    password=request.POST['password']
    l=Login.objects.filter(username=username,password=password)


    if l.exists():
        m=Login.objects.get(username=username,password=password)
        request.session['lid']=m.id

        if m.type=="admin":
            return HttpResponse('''<script>alert('success');window.location='/adminpage'</script>''')

        elif m.type=="user":
            return HttpResponse('''<script>alert('success');window.location='/userpage'</script>''')
        else:
            return HttpResponse('''<script>alert('invalid');window.location='/'</script>''')

    else:
        return HttpResponse('''<script>alert('success');window.location='/'</script>''')




def edit_user_profile(request,id):
    e=User.objects.get(id=id)
    return render(request,'userpage/edit user profile.html',{'data':e})



def edit_user_profile_POST(request):
    id=request.POST['id']
    username=request.POST['username']
    firstname=request.POST['firstname']
    lastname=request.POST['lastname']
    email=request.POST['email']
    password=request.POST['password']

    f=User.objects.get(id=id)

    f.username=username
    f.firstname=firstname
    f.lastname=lastname
    f.email=email
    f.password=password
    f.save()

    return HttpResponse('''<script>alert('success');window.location='/userpage'</script>''')



def add_movie_admin(request):
    p=Admin.objects.all()
    return render(request,'adminpage/movie.html',{'data':p})


def add_movie_admin_POST(request):
    title=request.POST['title']
    description=request.POST['description']
    release_date=request.POST['release_date']
    genres=request.POST['genres']
    actors=request.POST['actors']
    trailerlink=request.POST['trailerlink']

    a = Movie()
    if 'image' in request.FILES:
        image = request.FILES['image']
        fs = FileSystemStorage()
        date = datetime.datetime.now().strftime("%Y-%m-%d-%H-%M-%S") + '.JPG'
        fs.save(date, image)
        path = fs.url(date)
        a.image = path


    a.title=title
    a.description=description
    a.release_date=release_date
    a.genres=genres
    a.actors=actors
    a.trailerlink=trailerlink


    a.USER=User.objects.get(id=request.session['lid'])

    a.save()
    return HttpResponse('''<script>alert('success');window.location='/adminpage'</script>''')







def add_movie_user(request):
    c=User.objects.all()
    return render(request,'userpage/add movie user.html',{'data':c})


def add_movie_user_POST(request):
    title = request.POST['title']
    description = request.POST['description']
    release_date = request.POST['release_date']
    genres = request.POST['genres']
    actors = request.POST['actors']
    trailerlink = request.POST['trailerlink']

    a = Movie()
    if 'image' in request.FILES:
        image = request.FILES['image']
        fs = FileSystemStorage()
        date = datetime.datetime.now().strftime("%Y-%m-%d-%H-%M-%S") + '.JPG'
        fs.save(date, image)
        path = fs.url(date)
        a.image = path


    a.title = title
    a.description = description
    a.release_date = release_date
    a.genres = genres
    a.actors = actors
    a.trailerlink = trailerlink


    a.USER=User.objects.get(LOGIN_id=request.session['lid'])
    a.save()
    return HttpResponse('''<script>alert('added');window.location='/userpage'</script>''')



def edit_movie_user(request,id):
    a=Movie.objects.get(id=id)
    return render(request,'userpage/edit movie user.html',{'data':a})


def add_genre_admin(request,id):
    a=Movie.objects.get(id=id)
    return render(request,'adminpage/genre.html',{'data':a})





def edit_movie_user_POST(request):
    id=request.POST['id']
    title=request.POST['title']
    description = request.POST['description']
    release_date = request.POST['release_date']
    genres = request.POST['genres']
    actors = request.POST['actors']
    trailerlink = request.POST['trailerlink']

    c=Movie.objects.get(id=id)
    if 'image' in request.FILES:
        image = request.FILES['image']
        fs = FileSystemStorage()
        date = datetime.datetime.now().strftime("%Y-%m-%d-%H-%M-%S") + '.JPG'
        fs.save(date, image)
        path = fs.url(date)
        c.image = path
    c.title=title
    c.description = description
    c.release_date = release_date
    c.genres = genres
    c.actors = actors
    c.trailerlink = trailerlink


    c.save()
    return HttpResponse('''<script>alert('added');window.location='/userpage'</script>''')


def add_genre_admin_POST(request):
    id = request.POST['id']
    genres = request.POST['genres']
    title=request.POST['title']
    c = Movie.objects.get(id=id)
    c.genres = genres
    c.title=title
    c.save()
    return HttpResponse('''<script>alert('added');window.location='/adminpage'</script>''')


def delete_movie_user(request,id):
    d=Movie.objects.get(id=id)
    d.delete()
    return HttpResponse('''<script>alert('deleted');window.location='/userpage'</script>''')

def view_movie_user(request):
    d=Movie.objects.all()
    return render(request,'userpage/view movie user.html',{'data':d})


def view_movie_admin(request):
    d=Movie.objects.all()
    return render(request,'adminpage/view movie admin.html',{'data':d})


def sent_rating_user(request,id):
    a=Movie.objects.get(id=id)

    return render(request,'userpage/sent rating movie.html',{'data':a})


def sent_rating_user_POST(request):
    id=request.POST['id']
    rating=request.POST['rating']

    s=Rating()
    s.rating=rating
    s.date=datetime.datetime.now().today()
    s.USER=User.objects.get(id=id)
    s.save()
    return HttpResponse('''<script>alert('send');window.location='/userpage'</script>''')


def sent_review_user(request):
    return render(request,'userpage/sent review movie.html')


def sent_review_user_POST(request):
    review=request.POST['review']
    a=Review()
    a.review=review
    a.USER=User.objects.get(LOGIN_id=request.session['lid'])
    a.date=datetime.datetime.now().today()
    a.save()
    return HttpResponse('''<script>alert('send');window.location='/userpage'</script>''')


def view_search_movie(request):
    title=request.POST['title']
    v=Movie.objects.filter(title__icontains=title)
    return render(request,'userpage/view movie user.html',{'data':v})






def delete_movie_admin(request,id):
    d=Movie.objects.get(id=id)
    d.delete()
    return HttpResponse('''<script>alert('deleted');window.location='/adminpage'</script>''')


def view_user(request):
    u=User.objects.all()
    return render(request,'adminpage/view user admin.html',{'data':u})


def delete_user_admin(request,id):
    d=User.objects.get(id=id)
    d.delete()
    return HttpResponse('''<script>alert('deleted');window.location='/adminpage'</script>''')


# def add_genre_admin(request):
#     p=Movie.objects.all()
#     return render(request,'adminpage/genre.html',{'data':p})
#
#
# def add_genre_admin_POST(request):
#     MOVIE=request.POST['select']
#     genres=request.POST['genres']
#
#     f=Movie()
#     f.genres=genres
#     f.MOVIE=Movie.objects.get(id=MOVIE)
#     f.USER=User.objects.get(LOGIN_id=request.session['lid'])
#     # f.title=title
#     f.save()
#
#     return HttpResponse('''<script>alert('success');window.location='/adminpage'</script>''')
#


































































