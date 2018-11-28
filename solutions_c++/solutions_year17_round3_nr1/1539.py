
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

const double PI = 3.141592653589793;


struct solver
{
  double solve(int N, int K, vector<long long> &Rs, vector<long long> &Hs)
  {
    vector<int> idxs_by_inc_rad(N);
    for (int i=0 ; i < N ; i++)
      idxs_by_inc_rad[i] = i;
    sort(idxs_by_inc_rad.begin(), idxs_by_inc_rad.end(), [&](int i, int j) -> bool {return Rs[i] > Rs[j];});

    vector<long long> side_areas(N);
    for (int i=0 ; i < N ; i++)
      side_areas[i] = Rs[i] * Hs[i];

    vector<int> idxs_by_side_area(N);
    for (int i=0 ; i < N ; i++)
      idxs_by_side_area[i] = i;
    sort(
      idxs_by_side_area.begin(),
      idxs_by_side_area.end(),
      [&] (int i, int j) -> bool {return side_areas[i] > side_areas[j];}
    );

    double max_area = 0;

    for (int i=0 ; i <= N - K ; i++) {
      int idx_largest = idxs_by_inc_rad[i];
      int max_rad = Rs[idx_largest];

      vector<int> selected_idxs;
      selected_idxs.push_back(idx_largest);
      for (int j=0 ; selected_idxs.size() < K ; j++) {
        assert(j < N);
        int curr_idx = idxs_by_side_area[j];
        if (curr_idx != idx_largest && Rs[curr_idx] <= max_rad)
          selected_idxs.push_back(curr_idx);
      }

      double area = PI * ((double) max_rad) * ((double) max_rad);
      for (int j=0 ; j < K ; j++) {
        int idx = selected_idxs[j];
        area += 2.0 * PI  * side_areas[idx];
      }

      if (area > max_area)
        max_area = area;
    }

    return max_area;
  }
};

////////////////////////////////////////////////////////////////////////////////
////////////////////////////////////////////////////////////////////////////////

void process_test_case(int case_num)
{
  int N, K;
  cin >> N >> K;

  vector<long long> Rs(N);
  vector<long long> Hs(N);

  for (int i=0 ; i < N ; i++)
    cin >> Rs[i] >> Hs[i];

  solver a_solver;

  double res = a_solver.solve(N, K, Rs, Hs);

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
