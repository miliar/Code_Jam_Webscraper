import math
import sys

def get_ints(infile):
  return [int(x) for x in infile.readline().strip().split()]


def get_int(infile):
  return int(infile.readline().strip())


def read_case(infile):
  N = get_int(infile)
  vels = []
  starts = []
  for i in range(N):
    x,y,z,vx,vy,vz = get_ints(infile)
    vels.append((vx,vy,vz))
    starts.append((x,y,z))
  return {'N': N, 'vels': vels, 'starts': starts}


def solve_case(data):
  N = float(data['N'])
  vels = data['vels']
  starts = data['starts']
  vel_cm = [0.0, 0.0, 0.0]
  start_cm = [0.0, 0.0, 0.0]
  for i in range(data['N']):
    vel_cm[0] += vels[i][0] / N
    vel_cm[1] += vels[i][1] / N
    vel_cm[2] += vels[i][2] / N
    start_cm[0] += starts[i][0] / N
    start_cm[1] += starts[i][1] / N
    start_cm[2] += starts[i][2] / N
  
  num = vel_cm[0]*start_cm[0] + vel_cm[1]*start_cm[1] + vel_cm[2]*start_cm[2]
  denom = vel_cm[0]*vel_cm[0] + vel_cm[1]*vel_cm[1] + vel_cm[2]*vel_cm[2]
  if denom < 0.000001:
    t = 0.0
  else:
    t = max(0.0, -num/denom)
    
  
  
  dist = 0.0
  dist += (start_cm[0] + vel_cm[0]*t)*(start_cm[0] + vel_cm[0]*t)
  dist += (start_cm[1] + vel_cm[1]*t)*(start_cm[1] + vel_cm[1]*t)
  dist += (start_cm[2] + vel_cm[2]*t)*(start_cm[2] + vel_cm[2]*t)
  dist = math.sqrt(dist)
  return {'t': t, 'dist': dist}    


def print_solution(solution, outfile):
  outfile.write(' %f %f\n' % (solution['dist'], solution['t']))


def main():
  if len(sys.argv) < 2:
    infile = sys.stdin
  else:
    infile = open(sys.argv[1], 'r')
    
  outfile = sys.stdout
  
  num_trials = get_int(infile)
  
  for case in range(num_trials):
    data = read_case(infile)
    solution = solve_case(data)
    outfile.write('Case #%d:' % (case+1))
    print_solution(solution, outfile)


if __name__ == '__main__':
  main()