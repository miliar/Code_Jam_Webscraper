#include<cstdio>
#include<cstdint>
#include<cassert>
#include<cmath>
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

const int MPD = 2 * 720;

int tdelta(int a, int b) {
  return (a - b + MPD) % MPD;
}

void single(int case_id, bool run) {
  // Input
  int A_c, A_j;
  cin >> A_c >> A_j;
  std::map<pair<int, int>, bool> intervals;
  vector<int> C, D, J, K;
  for (int i = 0; i < A_c; i++) {
    int c, d;
    cin >> c >> d;
    intervals[pair<int,int>(c, d)] = true;
    C.push_back(c);
    D.push_back(d);
  }
  for (int i = 0; i < A_j; i++) {
    int j, k;
    cin >> j >> k;
    intervals[pair<int,int>(j, k)] = false;
    C.push_back(j);
    D.push_back(k);
  }

  if (! run) return;
  // Solve
  int inherent_slack = 0;
  int num_switches = 0;
  map<bool, vector<int>> optional_slack;
  map<bool, int> inherent_time;
  int prev_end = intervals.rbegin()->first.second;
  int prev_kind = intervals.rbegin()->second;
  for (auto it : intervals) {
    inherent_time[it.second] += tdelta(it.first.second, it.first.first);
    if (prev_kind == it.second) {
      optional_slack[it.second].push_back(tdelta(it.first.first, prev_end));
      inherent_time[it.second] += tdelta(it.first.first, prev_end);
    } else {
      num_switches += 1;
      inherent_slack += tdelta(it.first.first, prev_end);
    }
    prev_kind = it.second;
    prev_end = it.first.second;
  }
  std::sort(optional_slack[true].begin(), optional_slack[true].end());
  std::sort(optional_slack[false].begin(), optional_slack[false].end());
  assert(inherent_time[true] + inherent_time[false] + inherent_slack == MPD);
  if (inherent_time[true] > 720 || inherent_time[false] > 720) {
    bool which = inherent_time[true] > 720;
    while (inherent_time[which] > 720) {
      int additional_slack = optional_slack[which].back();
      optional_slack[which].pop_back();
      inherent_time[which] -= additional_slack;
      inherent_slack += additional_slack;
      num_switches += 2;
    }
  }

  cout << "Case #" << case_id << ": ";
  // Output
  cout << num_switches;
 
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
