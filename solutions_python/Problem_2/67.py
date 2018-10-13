from time import *

DATE="20000101"
START_OF_DATE=mktime(strptime(DATE+"0000","%Y%m%d%H%M"))
END_OF_DATE=START_OF_DATE+86400

def main():
	import sys
	numberOfInputs = int(sys.stdin.readline())
	for i in range(1, numberOfInputs+1):
		turnAroundSeconds = int(sys.stdin.readline()) * 60
		numbersOfTrips = map(lambda a:int(a), sys.stdin.readline().split())

		trips = []
		for j in range(numbersOfTrips[0]):
			tripTime = map(lambda a:mktime(strptime(DATE+a,"%Y%m%d%H:%M")), sys.stdin.readline().split())
			trips.append({"time":tripTime, "from":"A", "to":"B"})

		for j in range(numbersOfTrips[1]):
			tripTime = map(lambda a:mktime(strptime(DATE+a,"%Y%m%d%H:%M")), sys.stdin.readline().split())
			trips.append({"time":tripTime, "from":"B", "to":"A"})

		trips.sort(lambda a,b:a["time"][0] > b["time"][0] and 1 or (a["time"][0] < b["time"][0] and -1 or 0))

		stations = {"A":[], "B":[]}
		trains = {"A":0, "B":0}
		for trip in trips:
			trainFound = False
			for ableTime in stations[trip["from"]]:
				if ableTime <= trip["time"][0]:
					stations[trip["from"]].remove(ableTime)
					trainFound = True
					break
			if not trainFound: trains[trip["from"]] += 1
			stations[trip["to"]].append(trip["time"][1] + turnAroundSeconds)
			stations[trip["to"]].sort()

		print "Case #"+str(i)+": " + str(trains["A"])+" "+str(trains["B"])


if __name__ == "__main__": main()
