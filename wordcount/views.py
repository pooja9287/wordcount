from django.http import HttpResponse
from django.shortcuts import render
import operator
def homepage(request):
    return render(request,'home.html')

def count(request):
    data=request.GET['t1']
    word_list=data.split()
    list_len= len(word_list)
    worddictionary={}
    for word in word_list:
        if word in worddictionary:
            worddictionary[word] += 1
        else:
            worddictionary[word] = 1
    sorted_list=sorted(worddictionary.items(),key = operator.itemgetter(1), reverse=True)

    return render (request,'counted.html',{'fulltext':data,'list_len':list_len,'worddictionary':sorted_list})
