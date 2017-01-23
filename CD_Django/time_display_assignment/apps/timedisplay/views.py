from django.shortcuts import render, HttpResponse
import datetime

def index(request):
	time = datetime.datetime.now().strftime('%b %d, %Y, %I:%M:%S ' ' %p')
	data = {
		'currentTime' : time,
	}
	return render(request, 'timedisplay/index.html', data)
