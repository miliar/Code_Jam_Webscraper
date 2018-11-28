def solve(N, Q, ESs, Dss, UVs):
  Ds = [Dss[i][i+1] for i in range(N-1)]

  cum_Ds = [0]
  for i in range(1, N):
    cum_Ds.append(cum_Ds[-1] + Ds[i-1])

  best_results = [(0.0, None)]
  for i_e in range(1, N):
    best_time = None
    best_prev = None
    for i_s in range(i_e):
      time, prev = best_results[i_s]
      E, S = ESs[i_s]

      # Distance between i_s and i_e
      Dse = cum_Ds[i_e] - cum_Ds[i_s]

      if E >= Dse:
        new_time = time + float(Dse) / float(S)
        if best_time == None or new_time < best_time:
          best_time = new_time
          best_prev = prev
    best_results.append((best_time, best_prev))

  best_final_time, best_final_prev = best_results[-1]
  return best_final_time

################################################################################

from sys import argv, exit

if len(argv) != 3:
  print "Usage: python main.py <input file> <output file>";
  exit(1);

ifile = open(argv[1])
ofile = open(argv[2], "w")

T = int(ifile.readline())

# print T

for i_T in range(1, T+1):
  # N = int(ifile.readline().strip());
  # ms = [int(s) for s in ifile.readline().strip().split()]

  N, Q = [int(s) for s in ifile.readline().strip().split()]
  ESs = []
  for i in range(N):
    E, S = [int(s) for s in ifile.readline().strip().split()]
    ESs.append((E, S))
  Dss = []
  for i in range(N):
    Ds = [int(s) for s in ifile.readline().strip().split()]
    Dss.append(Ds);
  UVs = []
  for i in range(Q):
    U, V = [int(s) for s in ifile.readline().strip().split()]
    UVs.append((U, V))

  res = solve(N, Q, ESs, Dss, UVs)

  output = 'Case #' + str(i_T) + ': ' + str(res)

  # print output

  ofile.write(output)
  ofile.write('\n')
