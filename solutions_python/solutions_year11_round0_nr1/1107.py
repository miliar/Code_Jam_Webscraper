import sys
import os, time

path = os.path.abspath(sys.argv[1])
with open(path) as test_file:
    t = int(test_file.readline().strip())
    i_output = 1
    while t > 0:
        input_line = test_file.readline().strip().split()
        n = int(input_line[0])
        i = 1

        input_list = []
        v_orange = []
        v_blue = []
        while n > 0:
            key = input_line[2 * i - 1]
            value = int(input_line[2 * i])
            input_list.append((key, value))
            if key == 'O':
                v_orange.append(value)
            if key == 'B':
                v_blue.append(value)
            n -= 1
            i += 1
        if len(v_orange) > 0:
            v_orange.append(v_orange[len(v_orange) - 1]) 
        else:
            v_orange.append(0)
        if len(v_blue) > 0:
            v_blue.append(v_blue[len(v_blue) - 1])
        else:
            v_blue.append(0)
        i_list = 0
        c_orange = 1
        i_orange = 0
        c_blue = 1
        i_blue = 0
        output = 0
        push = False
#        print input_list, v_orange, v_blue
        while i_list < len(input_list):
            key, value = input_list[i_list]
#            print 'Before', i_list, key, value, '>', c_orange, c_blue
            push_orange = False
            push_blue = False
            if key == 'O' and c_orange == value:
                i_list += 1
                i_orange += 1
                push_orange = True
#                print 'Push O'
            elif key == 'B' and c_blue == value:
                i_list += 1
                i_blue += 1
                push_blue = True
#                print 'Push B'
            if not push_orange:
                if c_orange < v_orange[i_orange]:
                    c_orange += 1
#                    print 'Move O to', c_orange, 1
                elif c_orange > v_orange[i_orange]:
                    c_orange -= 1
#                    print 'Move O to', c_orange, -1
                else:
                    pass
#                    print 'Stay O'
            if not push_blue:
                if c_blue < v_blue[i_blue]:
                    c_blue += 1
#                    print 'Move B to', c_blue, 1
                elif c_blue > v_blue[i_blue]:
                    c_blue -= 1
#                    print 'Move B to', c_blue, -1
                else:
                    pass
#                    print 'Stay B'
            output += 1
#            print 'After', i_list, key, value, '>', c_orange, c_blue
#            print ''
#            time.sleep(0.1)
        print 'Case #%d: %d' % (i_output, output)
        t -= 1
        i_output += 1
    
