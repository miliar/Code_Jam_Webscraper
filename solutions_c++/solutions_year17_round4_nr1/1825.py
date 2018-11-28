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

void single(int case_id, bool run) {
  // Input
  int N, P;
  cin >> N >> P;
  vector<int> G;
  for (int i = 0; i < N; i++) {
    int g;
    cin >> g;
    G.push_back(g);
  }

  if (! run) return;
  // Solve
  vector<int> C(P, 0);
  for (int i = 0; i < N; i++) {
    C[G[i] % P] += 1;
  }
  int happy = 0;
  happy += C[0];
  if (P == 2) {
    happy += (C[1] + 1) / 2;
  }
  if (P == 3) {
    int match2 = min(C[1], C[2]);
    happy += match2;
    C[1] -= match2;
    C[2] -= match2;
    happy += (max(C[1], C[2]) + 2) / 3;
  }
  cout << "Case #" << case_id << ": ";
  // Output
  cout << happy;
 
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
