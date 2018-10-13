import fileinput
import sys
import os

def process_input():
    tc_in = fileinput.input()
    tc_count = int(tc_in.readline())
    for i in range(tc_count):
        os.system("rm -rf sandbox/*")

        existing_count, to_create_count = (int(x) for x in tc_in.readline().split())
        to_create = []
        for j in range(existing_count):
            try:
                os.makedirs("sandbox" + tc_in.readline().rstrip())
            except OSError:
                #if exc.errno == errno.EEXIST:
                    pass
                #else: raise

        for j in range(to_create_count):
            to_create.append(tc_in.readline())
        total = 0
        for d in to_create:
            total += dirs_created(d.rstrip())
        print "Case #%d: %d" % (i+1, total)

def dirs_created(d):
    total = 0
    path = ""
    for i in d.split("/")[1:]:
        path += i + "/"
        if not os.access("sandbox/"+path, os.F_OK):
            total += 1
            os.mkdir("sandbox/"+path)
    return total


#class Directory:
    #subdirs = []
    #name = ""
    #def __init__(self, path):
        ##path.split("/")
        #self.parent = path[:-1]
        #self.name = path[-1]
        #self.subdirs = []
    #def exists(path):
    #def getParent(self, d):
        



def main():
    process_input()
    #os.system("rm -rf sandbox/*")

if __name__ == '__main__':
    status = main()
    sys.exit(status)
