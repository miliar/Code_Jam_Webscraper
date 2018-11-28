import sys, math
import fileinput
input_file=sys.argv[1]
print input_file




encoded = "ejp mysljylc kd kxveddknmc re jsicpdrysi rbcpc ypc rtcsra dkh wyfrepkym veddknkmkrkcd de kr kd eoya kw aej tysr re ujdr lkgc jv azq"
decoded = "our language is impossible to understand there are twenty six factorial possibilities so it is okay if you want to just give up yqz"

encoded_list = list(encoded)
decoded_list = list(decoded)

alphabets="abcdefghijklmnopqrstuvwxyz"
alphabets_list= list(alphabets)

#print len(encoded_list)

i=0

d = dict(zip(encoded_list, decoded_list))


line_count=0
input_count=0

fo = open("result.txt", "wb")

for line in fileinput.input(input_file):

    if line_count > 0:
        fo.write( "Case #" + str(line_count) + ": ")
        for j in line.rstrip('\n\r'):
            print j
            fo.write(d[j])
        fo.write("\n")

    line_count = line_count+1

    #if line_count > 1:
        #fo.write( "case # + line_count:")
		#out=""
        

			

fo.close()

