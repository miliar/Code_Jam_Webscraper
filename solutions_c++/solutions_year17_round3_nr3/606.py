#include<cstdio>
#include<cstdint>
#include<cassert>
#include<cmath>
#include<iomanip>
#include<iostream>
#include<vector>
#include<map>
#include<set>
#include<unordered_map>
#include<unordered_set>
#include<string>
#include<algorithm>
#include<utility>
#include<functional>

using namespace std;

void single(int case_id, bool run) {
  // Input
  int N, K;
  cin >> N >> K;
  double U;
  cin >> U;
  vector<double> P;
  for (int i = 0; i < N; i++) {
    double p;
    cin >> p;
    P.push_back(p);
  }
  sort(P.begin(), P.end());

  if (! run) return;
  // Solve
  for (int i = 0; i < N; i++) {
    double gift = 0;
    if (i == N - 1) {
      gift = U;
    } else {
      gift = (i + 1) * (P[i+1] - P[i]);
    }
    if (gift > U) gift = U;
    for (int j = 0; j <= i; j++) {
      P[j] += gift / (i + 1);
    }
    U -= gift;
  }
  double prob = 1;
  for (int i = 0; i < N; i++) {
    prob *= P[i];
  }

  cout << "Case #" << case_id << ": ";
  // Output
  cout << setprecision(20) << prob;
 
  cout << endl;
}

int main(int argc, char ** argv) {
  FILE * ret;
  ret = freopen(argv[1], "r", stdin);
  assert(ret != nullptr);
  int testcases;
  cin >> testcases;
  int first_testcase = 1;
  int last_testcase = testcases;
  if (argc >= 3) first_testcase = atoi(argv[2]);
  if (argc >= 4) last_testcase = atoi(argv[3]);
  for (int i = 1; i <= testcases; i++) {
    single(i, i >= first_testcase && i <= last_testcase);
  }
  return EXIT_SUCCESS;
}
