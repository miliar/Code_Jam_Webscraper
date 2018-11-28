import csv
import itertools

def jam(filename, mapper, num_args):
   " Generic helper to process Google Code Jam input file "
   with open(filename, 'rb') as f:
       reader = csv.reader(f)
       N = int(reader.next()[0])
       c = 0
       for arg0 in reader:
           c += 1
           args = arg0 + [reader.next() for _ in range(1, num_args)]
           yield mapper(*args)
       assert N == c, "Expected %s cases but found only %s" % (N, c)

sample_in = [
    "ejp mysljylc kd kxveddknmc re jsicpdrysi",
    "rbcpc ypc rtcsra dkh wyfrepkym veddknkmkrkcd",
    "de kr kd eoya kw aej tysr re ujdr lkgc jv"
    ]

sample_out = [
    "our language is impossible to understand",
    "there are twenty six factorial possibilities",
    "so it is okay if you want to just give up",
    ]

dictionary = dict(zip("".join(sample_in), "".join(sample_out)))
dictionary['z'] = 'q'
dictionary['q'] = 'z'
for v,k in dictionary.items():
 print v,k

def translate(arg0):
    return "".join(dictionary[x] for x in arg0) 

with open('A.out', 'wb') as f:
    for i, r in enumerate(jam('sample.in', translate, 1)):
        response = "Case #%s: %s\n" % (i+1, r)
        print response
        f.write(response)
    
