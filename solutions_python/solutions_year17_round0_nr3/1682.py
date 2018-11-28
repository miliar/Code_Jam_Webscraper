__author__ = 'tegjyot'
import math

def find_empty(n,m):
    tree=[]
    tree.append(n)
    for i in range(m):
      current=tree.pop(0)-1
      v2,v1 = int(math.ceil(float(current)/2)), int(math.floor(float(current)/2))
      if v1==v2 and v1==0:
          return [v1,v2]
      if tree!=[]:
          if tree[0]>v1:
              tree.append(v1)
          else:
              tree.insert(0,v1)
          if tree[0]>v2:
              tree.append(v2)
          else:
              tree.insert(0,v2)
      else:
          tree.append(v1)
          tree.append(v2)
      tree.sort(reverse=True)
    return [v1,v2]
    # return [tree[2*(m-1)+1],tree[2*(m-1)+2]]

def find_empty2(n,m):
    counts={}
    counts[n]=1
    current=n
    preivous=n
    while m>0:
        v2,v1 = int(math.ceil(float(current-1)/2)), int(math.floor(float(current-1)/2))
        v2, v1= max(v2, 0), max(v1,0)
        if current in counts:
            # print current, counts, m
            if counts[current]<=m:
                m-=counts[current]
                if v2 not in counts:
                    counts[v2]=0
                if v1 not in counts:
                    counts[v1]=0
                counts[v2]+=counts[current]
                counts[v1]+=counts[current]
            else:
                return [v1,v2]
        else:
            print'something is wrong'
        previous=current
        j=current-1
        while True:
            if j in counts:
                current=j
                break
            else:
                j-=1
    return [v1, v2]



def main():
  t = int(raw_input())  # read a line with a single integer
  for i in xrange(1, t + 1):
    # print i
    n, m = [int(s) for s in raw_input().split(" ")]  # read a list of integers, 2 in this case
    output=find_empty2(n,m)
    print "Case #{}: {} {}".format(i, str(max(output[0],output[1])), str(min(output[0],output[1])))

main()
