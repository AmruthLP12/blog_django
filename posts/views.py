from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

posts = [
    {
        "id": 1,
        "title": "Hello World",
        "content": "This is the first post",
    },
    {
        "id": 2,
        "title": "Hello World 2",
        "content": "This is the second post",
    },
    {
        "id": 3,
        "title": "Hello World 3",
        "content": "This is the third post",
    },
]


def home(request):
    html = ""
    for post in posts:
        html += f"""
        <div>
        <a href="/posts/{post['id']}/">
            <h2>{post['id']} - {post['title']}</h2></a>
            <p>{post['content']}</p>
        </div>
        """
    return HttpResponse(html)


def post(request, id):
    for post in posts:
        if post["id"] == id:
            post_dict = post
            break
    html = f"""
        <div>
           <h2>{post_dict['id']} - {post_dict['title']}</h2>
            <p>{post_dict['content']}</p>
        </div>
    """
    return HttpResponse(html)
