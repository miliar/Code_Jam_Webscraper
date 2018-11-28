def process_input(A,B,K):
  result = 0
  for i in range(A):
      for j in range(B):
          if(i&j < K):
              result += 1
  return result
    

def main() :
    T = int(input())
    for i in range(T):
        (A,B,K) = [int(e) for e in input().split()]
        print( 'Case #'+str(i+1)+':',process_input(A,B,K))
    

if __name__ == '__main__':
    main()
