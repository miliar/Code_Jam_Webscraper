#!/usr/bin/python
from sys import argv


def calculate_steps(n_buttons, inst_list):
    inst_num=0
    orange_list=[]
    blue_list=[]
    for x in xrange(0, len(inst_list), 2):
        if inst_list[x] == 'O':
            orange_list.append([int(inst_num), int(inst_list[x+1])])
        else:
            blue_list.append([int(inst_num), int(inst_list[x+1])])
        inst_num+=1
    n_steps=0
    button=0
    blue_pos=1
    orange_pos=1
    while button<n_buttons:
        #if only the blue bot must press buttons
        if orange_list == []:
            if blue_list[0][1]>blue_pos:
                blue_pos+=1
            elif blue_list[0][1]<blue_pos:
                blue_pos-=1
            else:
                button+=1
                blue_list.pop(0)
            n_steps+=1
        #if only the orange bot must press buttons
        elif blue_list == []:
            if orange_list[0][1]>orange_pos:
                orange_pos+=1
            elif orange_list[0][1]<orange_pos:
                orange_pos-=1
            else:
                button+=1
                orange_list.pop(0)
            n_steps+=1
        else:
            if orange_list[0][1] > orange_pos:
                orange_pos+=1
                if blue_list[0][1] > blue_pos:
                    blue_pos+=1
                elif blue_list[0][1] < blue_pos:
                    blue_pos-=1
                elif blue_list[0][0] == button:
                    blue_list.pop(0)
                    button+=1

            elif orange_list[0][1] < orange_pos:
                orange_pos-=1
                if blue_list[0][1] > blue_pos:
                    blue_pos+=1
                elif blue_list[0][1] < blue_pos:
                    blue_pos-=1
                elif blue_list[0][0] == button:
                    blue_list.pop(0)
                    button+=1

            elif orange_list[0][0] == button:
                button+=1
                orange_list.pop(0)
                if blue_list[0][1] > blue_pos:
                    blue_pos+=1
                elif blue_list[0][1] < blue_pos:
                    blue_pos-=1

            else:
                if blue_list[0][1] > blue_pos:
                    blue_pos+=1
                elif blue_list[0][1] < blue_pos:
                    blue_pos-=1
                elif blue_list[0][0] == button:
                    blue_list.pop(0)
                    button+=1
            n_steps+=1
    return n_steps


def robots(input_file, output_file):
    f=open(input_file, 'r')
    N=int(f.readline())
    g=open(output_file, 'w')
    for i in xrange(N):
        line=f.readline()
        inst_list=line.split(' ')
        n_buttons=int(inst_list[0])
        inst=inst_list[1:]
        g.write('Case #'+str(i+1)+': ')
        n_steps=calculate_steps(n_buttons, inst)
        g.write(str(n_steps)+'\n')
    f.close()
    g.close()


#run: python robots.py input output
if __name__=='__main__':
    if argv[0].find('robots.py')!=-1:
        if len(argv)>=3:
            robots(argv[1], argv[2])
