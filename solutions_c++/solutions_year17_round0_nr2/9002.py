#include <iostream>
typedef unsigned __int64 U64;
using namespace std;
unsigned __int64 calcM (unsigned __int64 N)
{
  if (N < 10) {
    return N;
  }
  U64 NN = N;
  int D = 10;
  U64 C = 1;
  U64 succNN = 0;
  int succD  = -1;
  U64 succC = 0;
  bool needCorr = false;
  while (NN) {
    int x = NN % 10;
    if (x > D || (succD >= 0 && x > succD - 1))
    {
      needCorr = true;
      succNN = NN;
      succD = x;
      succC = C;
    }
    NN = NN / 10;
    D = x;
    C *= 10;
  }
  if (!needCorr) {
    return N;
  }
  U64 M = (succNN - 1) * succC + (succC - 1);
  return M;
}


int main()
{
  int T = -1;

  cin >> T;
  unsigned __int64 N;
  for (int i = 0; i < T; ++i) {
    cin >> N;
    cout << "Case #" << (i + 1) << ": " << calcM(N) << endl;
  }
  return 0;
}