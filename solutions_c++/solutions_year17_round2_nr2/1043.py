
#include <map>
#include <set>
#include <cmath>
#include <queue>
#include <vector>
#include <string>
#include <cstdio>
#include <cstdlib>
#include <cstring>
#include <cassert>
#include <numeric>
#include <algorithm>
#include <iostream>
#include <fstream>
#include <sstream>
#include <ctime>
#include <limits>
using namespace std;

// #pragma warning(disable: 4018)
// #include "../my_header.h"


struct solver
{
  string solve(int N, int R, int O, int Y, int G, int B, int V)
  {
    assert(O == 0);
    assert(G == 0);
    assert(V == 0);

    int N1 = R;
    int N2 = Y;
    int N3 = B;
    char C1 = 'R';
    char C2 = 'Y';
    char C3 = 'B';

    if (N3 > N2) {
      swap(N2, N3);
      swap(C2, C3);
    }

    if (N2 > N1) {
      swap(N1, N2);
      swap(C1, C2);
      if (N3 > N2) {
        swap(N2, N3);
        swap(C2, C3);
      }
    }

    if (N1 > N2 + N3)
      return "IMPOSSIBLE";

    assert(N1 >= N2);
    assert(N2 >= N3);

    int left3 = N3 - (N1 - N2);

    string res;
    for (int i=0 ; i < N1 ; i++) {
      res += C1;
      if (i < N2)
        res += C2;
      else
        res += C3;
      if (i < left3)
        res += C3;
    }

    return res;
  }
};

////////////////////////////////////////////////////////////////////////////////
////////////////////////////////////////////////////////////////////////////////

void process_test_case(int case_num)
{
  int N, R, O, Y, G, B, V;

  cin >> N >> R >> O >> Y >> G >> B >> V;

  solver a_solver;

  string res = a_solver.solve(N, R, O, Y, G, B, V);

  cout << "Case #" << case_num << ": " << res << endl;
}

////////////////////////////////////////////////////////////////////////////////

int main(int argc, char **argv)
{
  cout.precision(8);
  cout << fixed;

  int T;
  cin >> T;
  // assert(T > 0 && T < 200);

  for (int i=0 ; i < T ; i++)
  {
    // if (i > 0)
    //  cout << "\n---------------------------------------------\n\n";
    process_test_case(i+1);
  }

  return 0;
}
