import sys

class Task:
    def __init__(self, sym, button):
        self.symbol = sym
        self.button = button
        self.finish = None

    def __repr__(self):
        return '%s: %d => %d' % (self.symbol, self.button, self.finish)

    @staticmethod
    def load(count, tokens):
        result = []
        for i in range(0, count):
            pos = i * 2
            t = Task(tokens[pos], int(tokens[pos+1]))
            result.append(t)
        return result

def abs(val):
    if val < 0:
        return -val
    return val

def diffTask(prev, now):
    return abs(now.button - prev.button)

def diffTime(prev, now):
    return now - prev

def calcTime(prevTask, task, nowTime):
    t = diffTask(prevTask, task) - diffTime(prevTask.finish, nowTime)
    if t < 0:
        t = 0
    return nowTime + t + 1

class Robot:
    def __init__(self, sym):
        self.symbol = sym
        self.pos = 0
        self.lastTask = Task(sym, 1)
        self.lastTask.finish = 0

    def getLastTask(self):
        return self.lastTask

    def finishTask(self, task):
        self.lastTask = task

def solv(tasks):
    robots = {'O': Robot('O'), 'B': Robot('B') }
    time = 0
    for i in range(0, len(tasks)):
        task = tasks[i]
        robot = robots[task.symbol]
        prevTask = robot.getLastTask()
        time = calcTime(prevTask, task, time)
        task.finish = time
#        print(task)
        robot.finishTask(task)
    return time

if __name__ == '__main__':
    dataSet = [line.rstrip() for line in open(sys.argv[1])]
    dataCount = int(dataSet[0])
    for i in range(0, dataCount):
        datas = dataSet[i+1].split()
        tasks = Task.load(int(datas[0]), datas[1:])
        print 'Case #%d: %d' % (i+1, solv(tasks))
