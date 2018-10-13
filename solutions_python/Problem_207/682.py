


import operator



def compute_sequence(N, R, O, Y, G, B, V):
    final_sequence=['' for i in range(N)]
    i=-2
    list_seq=[R, O, Y, G, B, V]
    list_primary=[0,2,4]
    list_secondary=[1,3,5]
    impossible='IMPOSSIBLE'
    checked=0
    previous_put=1
    while (list_seq[list_secondary[0]]+list_seq[list_secondary[1]]+list_seq[list_secondary[2]])>0:
        if list_seq[list_secondary[checked]]>0:
            if previous_put==list_secondary[checked]:
                i=(i+2)%N
            else:
                 i=(i+3)%N
            final_sequence[i]=list_secondary[checked]
            list_seq[list_secondary[checked]]-=1
            previous_put=list_secondary[checked]
            # i=next_i
        checked=(checked+1)%3

    # checking placement of primary
    for j,fs in enumerate(final_sequence):
        if fs==1:
            if list_seq[4]<2:
                if final_sequence[(j-1)%N] ==4 and final_sequence[(j+1)%N]==4:
                    break
                return impossible
            final_sequence[(j-1)%N]=4
            final_sequence[(j+1)%N]=4
            list_seq[4]-=2
        if fs==3:
            if list_seq[0]<2:
                if final_sequence[(j-1)%N] ==0 and final_sequence[(j+1)%N]==0:
                    break
                return impossible
            final_sequence[(j-1)%N]=0
            final_sequence[(j+1)%N]=0
            list_seq[0]-=2

        if fs==5:
            if list_seq[2]<2:
                if final_sequence[(j-1)%N] ==2 and final_sequence[(j+1)%N]==2:
                    break
                return impossible
            final_sequence[(j-1)%N]=2
            final_sequence[(j+1)%N]=2
            list_seq[2]-=2

    # checking primary
    for i,f in enumerate(final_sequence):
        if f=='':
            break
    primary_dict={0:list_seq[list_primary[0]], 2:list_seq[list_primary[1]], 4:list_seq[list_primary[2]]}
    while sum(primary_dict.values())>0:
        items1=primary_dict.items()
        items1.sort(key=operator.itemgetter(1), reverse=True)
        if items1[0][0]==final_sequence[i-1]:
            if items1[1][1]==0:
                return impossible
            final_sequence[i]=items1[1][0]
            primary_dict[items1[1][0]]-=1
        else:
            final_sequence[i]=items1[0][0]
            primary_dict[items1[0][0]]-=1
        i+=1
    # final_sequence
    fss=''
    fss_ss='ROYGBV'
    for i in final_sequence:
            if i!='':
                fss+=fss_ss[int(i)]
    return fss

def main():
    t = int(raw_input())
    for i in xrange(1, t + 1):
      N, R, O, Y, G, B, V = [int(s) for s in raw_input().split(" ")]
      final_sequence=compute_sequence(N, R, O, Y, G, B, V)

      if final_sequence[0]==final_sequence[-1]:
          if final_sequence[-3]!=final_sequence[-1]:
              final_sequence=[j for j in final_sequence]
              final_sequence[-1]=final_sequence[-2]
              final_sequence[-2]=final_sequence[0]
              final_sequence=''.join(final_sequence)
          else:
            final_sequence='IMPOSSIBLE'
      print "Case #{}: {}".format(i, final_sequence)

main()