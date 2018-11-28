//
// Created by huklee on 08/04/2017.
//
// google code jam 2017 round 1C A

#include <algorithm>
#include <map>
#include <queue>
#include <string>
#include <bitset>
#include <fstream>
#include <iostream>
using namespace std;

const int MAX_N = 10;
const double MATH_PI = 3.1415926535897;

int A[MAX_N];
int B[MAX_N];

int get1Count(int i){
  int count = 0;
  while (i){
    i &=  (i - 1);
    count++;
  }
  return count;
}

double solve(int N, int K){
  double global_max = 0;
  for (int i=0; i < (1<<10); i++){
    vector<pair<double, double>> vpi;
    if (get1Count (i) != K) continue;
    for (int j=0; j < N; j++) {
      if (i & (1 << j))
        vpi.push_back(pair<double, double>{A[j], B[j]});
    }

    double max_r = 0, sum_area = 0;
    for (pair<double, double> pi : vpi){
      sum_area += 2*pi.second*pi.first;
      max_r = max(pi.first, max_r);
    }

    double local_val = (max_r*max_r + sum_area)*MATH_PI;
    global_max = max(local_val, global_max);
  }

  return global_max;
}

int main() {
  // freopen("/Users/huklee/ClionProjects/Algorithm_Study/input.txt", "r", stdin);
  int T, k;
  cin >> T;
  cout.precision(9);
  for (int tc=1; tc <= T; tc++){
    int N, K;
    cin >> N >> K;
    for (int j=0; j < N; j++){
      cin >> A[j] >> B[j];
    }
    cout << "Case #" << tc << ": ";
    cout << fixed << solve(N, K) << endl;
  }
}
