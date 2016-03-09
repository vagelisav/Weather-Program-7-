import urllib,json
lat1,lon1 = input("Give me coordinates \n ") 
ap='b9edd496ab2d4e375ff49619fcdfdea3'
#Enter your API key (in ap)
url = "http://api.openweathermap.org/data/2.5/weather?"
params = urllib.urlencode({'lat':(lat1),'lon':(lon1),'appid':(ap)})
url = url.endswith( '&' ) and (url + params) or (url + '&' + params)
response = urllib.urlopen(url)
data = json.loads(response.read())
try:
	t=data['main']['temp']
	if t > 293.15:
		print 'nice...'
	elif t < 278.15:
		print 'brrr'
	for i in data['weather']:		
		if i['main'] == 'Rain':
			print "I'm singing in the rain!"
except:
		print 'Not found city'


