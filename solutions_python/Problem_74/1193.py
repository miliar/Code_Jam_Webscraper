import sys

class Bot:
	color = ""
	pos = 1
	didSomething = 0
	hitButton = 0
	def __init__(self,color):
		self.color = color


time = 0
atlas = Bot("blue")
pbody = Bot("orange")

fileName = sys.argv[1]
file=open(fileName,'r')

output = open("results.txt","w")

numTrials = int(file.readline())

for r in range(0,numTrials):
	line = file.readline()
	line = line.split(" ")
	numOfEvents = line.pop(0)
	eventQueue = line

	time=0
	atlas.pos=1
	pbody.pos=1
	while(len(eventQueue)>0):
		if len(eventQueue)<3:
			curEvent=(eventQueue[0] , int(eventQueue[1]))
			nextEvent=[]
		else:
			curEvent=(eventQueue[0] , int(eventQueue[1]))
			for t in range(2,len(eventQueue)):
				if(eventQueue[0]=="B"):
					if(eventQueue[t]=="O"):
						nextEvent=(eventQueue[t] , int(eventQueue[t+1]))
						break
				if(eventQueue[0]=="O"):
					if(eventQueue[t]=="B"):
						nextEvent=(eventQueue[t] , int(eventQueue[t+1]))
						break
			

		pbody.didSomething = 0
		atlas.didSomething = 0
		pbody.hitButton = 0
		atlas.hitButton = 0
		
		if(curEvent[0]=="O"):
			if(curEvent[1]==pbody.pos):
				pbody.didSomething = 1
				pbody.hitButton=1
				eventQueue.pop(0)
				eventQueue.pop(0)
			elif(curEvent[1]<pbody.pos):
				pbody.pos-=1
				pbody.didSomething = 1
			else:
				pbody.pos+=1
				pbody.didSomething = 1
		
		elif(curEvent[0]=="B"):
			if(curEvent[1]==atlas.pos):
				atlas.didSomething = 1
				atlas.hitButton=1
				eventQueue.pop(0)
				eventQueue.pop(0)
			elif(curEvent[1]<atlas.pos):
				atlas.pos-=1
				atlas.didSomething = 1
			else:
				atlas.pos+=1
				atlas.didSomething = 1
				
		if(len(nextEvent)>0 and nextEvent[0]=="O" and pbody.didSomething==0):
			
			if(nextEvent[1]<pbody.pos):
				pbody.pos-=1
				pbody.didSomething = 1
			elif(nextEvent[1]>pbody.pos):
				pbody.pos+=1
				pbody.didSomething = 1
		elif(len(nextEvent)>0 and nextEvent[0]=="B" and atlas.didSomething==0):
		
			if(nextEvent[1]<atlas.pos):
				atlas.pos-=1
				atlas.didSomething = 1
			elif(nextEvent[1]>atlas.pos):
				atlas.pos+=1
				atlas.didSomething = 1
	
		time+=1
	output.write( "Case #" + str(r+1) + ": " + str(time) +"\n")
		
		
		
		



	