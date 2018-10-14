def main():
  with open("out.txt","w") as out:
    with open("in.txt","r") as file:
      num_tests = int(file.readline().rstrip())
      for b in range(num_tests):
        num = int(file.readline().rstrip())
        
        for orig in reversed(xrange(num+1)):

          i = orig
          last = 10
          flag = True
          while i > 0:
            if last >= i%10:
              last = i%10
            else:
              flag = False
              break
            i/=10

          if flag:
            out.write("Case #{}: {}\n".format(b+1, orig))
            break





if __name__ == '__main__':
  main()