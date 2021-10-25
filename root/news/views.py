from django.shortcuts import render, HttpResponse,redirect
from news.models import Post,NewsComment
from django.contrib import messages
from news.templatetags import extras

# Create your views here.
def newsHome (request):
    allposts = Post.objects.all()
    context = {'allposts':allposts}
    return render(request,'news/newsHome.html',context)
def newsPost(request,slug):
    post = Post.objects.filter(slug=slug).first()
    comments = NewsComment.objects.filter(post=post,parent=None)
    replies = NewsComment.objects.filter(post=post).exclude(parent=None)
    replyDict={}
    for reply in replies:
        if reply.parent.sno not in replyDict.keys():
            replyDict[reply.parent.sno] = [reply]
        else:
            replyDict[reply.parent.sno].append(reply)

    context = {'post':post,'comments':comments,'user':request.user,'replyDict':replyDict}
    return render(request,'news/newsPost.html',context)

def postComment(request):
    if request.method =='POST':
        comment = request.POST.get("comment")
        user = request.user
        postSno = request.POST.get('postSno')
        post = Post.objects.get(sno=postSno)
        parentSno = request.POST.get("parentSno")
        if parentSno == "":
            comment = NewsComment(comment=comment,user=user,post=post)
            comment.save();
            messages.success(request,'your comment has been posted successfully')
        else:
            parent = NewsComment.objects.get(sno=parentSno)
            comment = NewsComment(comment=comment,user=user,post=post,parent=parent)
            comment.save();
            messages.success(request,'your reply has been posted successfully')

    return redirect(f"/news/{post.slug}")




