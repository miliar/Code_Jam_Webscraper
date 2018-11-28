#include <vector>
#include <list>
#include <map>
#include <set>
#include <deque>
#include <queue>
#include <stack>
#include <bitset>
#include <algorithm>
#include <functional>
#include <numeric>
#include <utility>
#include <sstream>
#include <iostream>
#include <iomanip>
#include <cstdio>
#include <cmath>
#include <cstdlib>
#include <cctype>
#include <string>
#include <cstring>
#include <ctime>
#include <iterator>

#if DEBUG
#include "prettyprint.hpp"
#define print_container(c) cout << c << endl;
#endif

using namespace std;

string FILENAME = "C-small-1-attempt0";

vector<int> read(string s){
  vector<int> ret;
  int n;
  istringstream sin(s);
  while(sin>>n)
    ret.push_back(n);
  return ret;
}

struct stall_info {
  int ls;
  int rs;
  int index;
};

bool cmp(stall_info& a, stall_info&b) {
  int a_min = min(a.ls, a.rs);
  int b_min = min(b.ls, b.rs);
  if (a_min < b_min) {
    return true;
  }
  if (a_min > b_min) {
    return false;
  }
  int a_max = max(a.ls, a.rs);
  int b_max = max(b.ls, b.rs);
  if (a_max < b_max) {
    return true;
  }
  if (a_max > b_max) {
    return false;
  }

  return a.index > b.index;
}

stall_info get_index(const vector<bool>& stalls) {
  vector<stall_info> stall_infos;
  for (int i = 0; i < stalls.size(); i++) {
    if (!stalls[i]) {
      stall_info info;
      info.index = i;
      for (int j = 1; j < stalls.size(); j++) {
        if (stalls[i - j]) {
          info.ls = j - 1;
          break;
        }
      }
      for (int j = 1; j < stalls.size(); j++) {
        if (stalls[i + j]) {
          info.rs = j - 1;
          break;
        }
      }
      stall_infos.push_back(info);
    }
  }
  sort(stall_infos.rbegin(), stall_infos.rend(), cmp);
  return stall_infos[0];
}

int main () {
  setvbuf(stdout, NULL, _IONBF, 0);
  freopen((FILENAME + ".in").c_str(), "r", stdin);
  freopen((FILENAME + ".out").c_str(), "w", stdout);
  int testcases;
  scanf("%d", &testcases);
  for (int case_id = 1; case_id <= testcases; case_id++) {
    printf("Case #%d: ", case_id);
    int n, k;
    scanf("%d %d", &n, &k);
    vector<bool> stalls(n + 2);
    stalls[0] = true;
    stalls[n + 1] = true;
    for (int i = 0; i < k; i++) {
      stall_info info = get_index(stalls);
      stalls[info.index] = true;
      if (i == k - 1) {
        printf("%d %d\n", max(info.ls, info.rs), min(info.rs, info.ls));
      }
    }
  }
  fflush(stdout);
}
