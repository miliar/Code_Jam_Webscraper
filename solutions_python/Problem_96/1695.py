'''
Created on 14 Apr 2012

@author: oracal
'''

def maximum_best(number, limit):
    for maximum_best in xrange(10,-1,-1):
        remainder = number - maximum_best
        top_limit = maximum_best + limit
        if top_limit > 10:
            top_limit = 10
        bottom_limit = maximum_best - limit
        if bottom_limit < 0:
            bottom_limit = 0
        for remainder1 in xrange(top_limit,bottom_limit-1,-1):
            for remainder2 in xrange(top_limit,bottom_limit-1,-1):
                if abs(remainder1 - remainder2) > limit:
                    continue
                if (remainder1 + remainder2) == remainder:
                    return maximum_best
    return None

def maximum_surprised(number):
    return maximum_best(number,2)

def maximum_unsurprised(number):
    return maximum_best(number,1)
    

if __name__ == '__main__':
    output_list = []
    with open('B-large.in') as f:
        f.next()
        surprised_cache = {}
        unsurprised_cache = {}
        count = 0
        for line in f:
            count +=1
            surprised_count = 0
            unsurprised_count = 0
            input_list = line.split()
            surprised_number = int(input_list[1])
            lower_limit = int(input_list[2])
            score_list = [int(x) for x in input_list[3:]]
            for score in score_list:
                try:
                    surprised_score =  surprised_cache[score]
                except:
                    surprised_score = maximum_surprised(score)
                    surprised_cache[score] = surprised_score
                if surprised_score>=lower_limit:
                    surprised_count+=1
                try:
                    unsurprised_score =  unsurprised_cache[score]
                except:
                    unsurprised_score = maximum_unsurprised(score)
                    unsurprised_cache[score] = unsurprised_score
                if unsurprised_score>=lower_limit:
                    unsurprised_count+=1
            if surprised_count - unsurprised_count < surprised_number:
                output_list.append(surprised_count)
            else:
                output_list.append(unsurprised_count + surprised_number)
    with open('output.txt','w') as o:
        for count,output in enumerate(output_list,start=1):
            o.write('Case #%s: %s\n' % (count,output))
        
            
            
                    