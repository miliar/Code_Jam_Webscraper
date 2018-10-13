#!/usr/bin/env python
import sys

def main(in_array, rule_1, rule_2, rule_2_chars):
    results = []
    rule_2_mark = -1
    for i in xrange(0, len(in_array)):
        results.append([])
        length = len(in_array[i])
        idx = 0
        while idx < length:
            if idx == length - 1:
                results[i].append(in_array[i][idx])
                if in_array[i][idx] in rule_2_chars[i] and rule_2_mark != -1:
                    if rule_2[i].has_key(in_array[i][idx]+in_array[i][rule_2_mark]):
                        results[i] = []
                break
            if in_array[i][idx] in rule_2_chars[i]:
                if rule_2_mark != -1:
                    if rule_2[i].has_key(in_array[i][idx]+in_array[i][rule_2_mark]):
                        results[i] = []
                        rule_2_mark = -1
                        idx += 1
                        '''special case'''
                        if in_array[i][idx] in rule_2_chars[i]:
                            rule_2_mark = idx
                else:
                    rule_2_mark = idx
            
            if idx < length - 1 and rule_1[i].has_key(in_array[i][idx]+in_array[i][idx+1]):
                results[i].append(rule_1[i][ in_array[i][idx] + in_array[i][idx+1]])
                idx = idx + 1
                if rule_2_mark == idx-1 or rule_2_mark == idx:
                    rule_2_mark = -1
            elif idx < length:
                results[i].append(in_array[i][idx])
            idx += 1
        rule_2_mark = -1
    return results

if __name__ == "__main__":
    in_array = []
    rule_1 = []
    rule_2 = []
    rule_2_chars = []
    infile = open('B-small-attempt0.in', 'rU')
    outfile = open('out', 'w')
    inputs = int(infile.readline())
    for i in xrange(0,inputs):
        in_array.append([])
        rule_1.append({})
        rule_2.append({})
        rule_2_chars.append([])
        input = infile.readline().split()
        r = 0
        for j in xrange(1, int(input[r])+1):
            rule_1[i][input[j][0]+input[j][1]] = input[j][2]
            rule_1[i][input[j][1]+input[j][0]] = input[j][2]
        r += int(input[r]) + 1
        for j in xrange(r+1, r + int(input[r]) + 1):
            rule_2[i][input[j][0]+input[j][1]] = ''
            rule_2[i][input[j][1]+input[j][0]] = ''
            rule_2_chars[i].append(input[j][0])
            rule_2_chars[i].append(input[j][1])
                           
        r += int(input[r]) + 1
        for j in xrange(0, int(input[r])):
            in_array[i].append(input[r+1][j])
            
    infile.close()

    results = main(in_array, rule_1, rule_2, rule_2_chars)
    for i in xrange(0, inputs):
        result = ''.join(results[i])
        str_o = ''
        if result != '':
            str_o = reduce(lambda x, y: x + ', '+y, result)
        str_o = '[' + str_o + ']'
        outfile.write(("Case #%d: %s\n") % (i+1, str_o))
    outfile.close()
