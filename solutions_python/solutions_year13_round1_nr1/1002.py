import math,sys

def main():
  input_file = sys.argv[1]
  output_file = sys.argv[2]
  ip = open(input_file, 'rU')
  casenums = int(ip.readline())
  solution=''
  for case in range(1,casenums+1):
    solution = solution + 'Case #'+str(case)+": "
    rad, t = map(long, ip.readline().split())
    blackrings = 0 
    black_ring_area = 2*rad+1
    while black_ring_area <= t:
      blackrings = blackrings + 1
      t = t - black_ring_area
      rad = rad + 2
      black_ring_area = 2*rad+1
    solution = solution + str(blackrings) + '\n'
  ip.close()
  op = open(output_file, 'w')
  op.write(solution)
  op.close()  

if __name__ == '__main__':
  main()
