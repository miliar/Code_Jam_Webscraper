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
  vector<int> R, H;
  for (int i = 0; i < N; i++) {
    int r, h;
    cin >> r >> h;
    R.push_back(r);
    H.push_back(h);
  }

  if (! run) return;
  // Solve
  double total_exposed_area = 0;
  for (int i = 0; i < N; i++) {
    // assume this is bottom
    double exposed_area = R[i] * (double) R[i] * M_PI;
    exposed_area += H[i] * (double) R[i] * 2 * M_PI;
    vector<double> matching_heights;
    for (int j = 0; j < N; j++) {
      if (i != j && R[j] <= R[i])
        matching_heights.push_back(H[j] * (double) R[j] * 2 * M_PI);
    }
    if (matching_heights.size() < K - 1) continue;
    sort(matching_heights.begin(), matching_heights.end(), greater<double>());
    for (int j = 0; j < K - 1; j++) {
      exposed_area += matching_heights[j];
    }
    if (exposed_area > total_exposed_area) total_exposed_area = exposed_area;
  }

  cout << "Case #" << case_id << ": ";
  // Output
  cout << setprecision(20) << total_exposed_area;
 
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
