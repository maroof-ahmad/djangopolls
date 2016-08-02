from django.shortcuts import render
# from django.http import HttpResponse
# from django.template import loader
from .models import Question

# Create your views here.

def index(request):
    latest_question_list = Question.objects.order_by('-pub_date')[:5]
    # template = loader.get_template('polls/index.html')
    context = {
    'latest_question_list' : latest_question_list,
    }
    #output = ', '.join([q.question_text for q in latest_question_list])
    # return HttpResponse(template.render(context, request))
    return render(request,'polls/index.html',context)

def detail(request, question_id):
    #other way to do the below
    #question = get_object_or_404(Question, pk=question_id)
    try:
        question = Question.objects.get(pk = question_id)
    except:
        raise Http404("Question does not exist")
    # return HttpResponse("You're looking at question %s" % question_id)
    return render(request, 'polls/detail.html', {'question' : question})
def results(request, question_id):
    response = "Results of question %s"
    return HttpResponse(response % question_id)

def vote(request, question_id):
    return HttpResponse (" vote for question %s" % question_id)
