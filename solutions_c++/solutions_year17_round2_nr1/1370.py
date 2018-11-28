#include<cstdio>
#include<cstdint>
#include<cassert>
#include<cmath>
#include<iostream>
#include<iomanip>
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

void single(int i, bool run) {
  // Input
  int D, N;
  cin >> D >> N;
  vector<int> K, S;
  for (int i = 0; i < N; i++) {
    int k, s;
    cin >> k >> s;
    K.push_back(k);
    S.push_back(s);
  }
  if (! run) return;
  // Solve
  double y = 0;
  vector<double> reached_at(N);
  for (int i = N - 1; i >= 0; i--) {
    reached_at[i] = (D - K[i]) * 1.0 / S[i];
    if (i == N - 1) continue;
    if (reached_at[i] < reached_at[i + 1])
      reached_at[i] = reached_at[i+1];
  }
  y = D * 1.0 / reached_at[0];
  // Output
  cout << "Case #" << i << ": ";
  cout << setprecision(9) << y;
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
