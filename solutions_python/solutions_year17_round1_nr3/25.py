import urllib
import urllib2
import re
import json
import requests
import os
from multiprocessing.dummy import Pool

class Spider:
	def __init__ (self, Query_id, Root = "photo"):
		self.Query_id = Query_id
		self.root = Root
		self.photo_prefix = "http://drpem3xzef3kf.cloudfront.net/"

	def Get_Json(self, Page_number = 0, Page_size = 20):
		URL ="https://www.petfinder.com/v1/pets/search/" + self.Query_id + ".json?" + \
				"page_number=" + str(Page_number) + \
				"&page_size=" + str(Page_size) + \
				"&status=adoptable" + \
				"&api_key=98719f8ded45b41f3153f5736d55d162"
		return urllib2.urlopen(URL)

	def __Grab(self, pet):
		position = self.root +'/' + pet['id'] + '/'
		if not os.path.isdir(position):
			os.makedirs(position)
		for i , photo_url in enumerate(pet["pet_photo"]):
			photo = urllib2.urlopen(self.photo_prefix + photo_url).read()
			fp = open( position + str(i) + '.jpg', 'wb' )
			fp.write(photo)
	def Grab(self, Npage):
		for page in range(Npage):
			results = json.loads(self.Get_Json(Page_number = page).read())["results"]
			pool = Pool(len(results))
			pool.map(self.__Grab, results)
				

Qid = "ED277D80-9C0E-11E6-B49E-0406B0B3A6EB"

Spider(Query_id = Qid,Root = "photo").Grab(Npage = 100)
