
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
  double solve(long long D, int N, vector<long long> &Ks, vector<long long> &Ss) {
    double max_time;
    for (int i=0 ; i < N ; i++) {
      double time = ((double) (D - Ks[i])) / ((double) Ss[i]);
      if (i == 0 || time > max_time)
        max_time = time;      
    }

    double speed = ((double) D) / max_time;

    return speed;
  }
};

////////////////////////////////////////////////////////////////////////////////
////////////////////////////////////////////////////////////////////////////////

void process_test_case(int case_num)
{
  long long D;
  int N;
  cin >> D >> N;
  vector<long long> Ks(N);
  vector<long long> Ss(N);
  for (int i=0 ; i < N ; i++) {
    cin >> Ks[i] >> Ss[i];
  }

  solver a_solver;

  double res = a_solver.solve(D, N, Ks, Ss);

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
