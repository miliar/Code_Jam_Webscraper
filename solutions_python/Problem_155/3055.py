__author__ = 'Stephane'


import os, optparse, sys, re, commands, socket, fileinput, threading


nb_threads = 8

tab = []
cases = 0
msg = ''
debug = ''

def deal_with_jobs(jobs):

    count = 0
    wait = 0
    nb_threads
    active_jobs_tab = []
    if len(jobs) >= nb_threads:
        active_jobs_tab_size = nb_threads
    else:
        active_jobs_tab_size = len(jobs)

    for i in range(active_jobs_tab_size):
        # initialize the active_jobs_tab
        active_jobs_tab.append(i)
        #start as many threads as the tab size
        jobs[i].start()
        wait += 1
        count += 1
    try:
        while wait > 0:
            for t in range(active_jobs_tab_size):
                if not jobs[active_jobs_tab[t]].isAlive():
                    # if the job is not alive replace it with another one
                    # if no more jobs to start reduce wait
                    if count == len(jobs):
                        wait -= 1
                        #once wait is 0 we exit the loop
                    else:
                        active_jobs_tab[t] = count
                        jobs[count].start()
                        count += 1

        #extra wait but should not be necessary
        for j in jobs:
            j.join()
        return
    except KeyboardInterrupt:
        print 'keyboard interrupted prout'
        raise
    except:
       print "Unexpected error from deal_with_jobs:", sys.exc_info()[0]
       raise

def read(input):
    f = open(input, 'r')

    case = 0
    content = f.readlines()

    cases = int(content[0].rstrip('\r\n'))

    for i in content[1:]:
    #for line in truncated:
        #print i
        l = i.rstrip('\r\n')
        ls=l.split(' ')
        smax = int(ls[0])
        row = list(ls[1])
        for a,i in enumerate(row):
            row[a]=int(i)
        #print row

        case+=1
        current = [case,smax,row,0]
        #print current
        tab.append(current)
    f.close()
    #print 'tab \n %s' % tab
    return



def main():
    try :
        input = sys.argv[1]
        output = sys.argv[2]
        global msg, tab, debug
        read(input)
        jobs = []
        for n in tab:

            proc = threading.Thread(target=do_the_calc, args=(n))
            jobs.append(proc)

        print 'jobs %s' % len(jobs)
        deal_with_jobs(jobs)
        print 'done'
        print debug
        for a in tab:
            msg += 'Case #%s: %s\n' % (a[0],a[3])

        o = open(output,'w+')
        o.write(msg)
        o.close()
    except KeyboardInterrupt:
        print 'keyboard interrupted'
        raise
        #sys.exit(1)
    except:
       print "Unexpected error:", sys.exc_info()[0]
       raise
    return


def do_the_calc(case,smax,row,res):
    ppl_to_add = 0
    global debug
    debug += 'do the calc %s %s %s\n' %(case,smax,row)
    res = 0
    sum = 0
    debug+='len %s \n' % len(row)
    if len(row) > 1:
        for index, number in enumerate(row):
            #print index,number
            if index == 0:
                continue
            #print row
            debug+='sum before %s' % sum
            sum += row[index-1]
            debug+='sum at index %s is %s\n' % (index,sum)
            while sum < index:
                res += 1
                #print 'index %s bbb %s' % (index,row[index-1])
                row[index-1]+=1
                #print ' cccc %s ' % row[index-1]
                sum += 1

    tab[case-1][3] = res




    return

if __name__ == '__main__':
    sys.exit(main())