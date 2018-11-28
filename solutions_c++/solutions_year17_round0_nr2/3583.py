#include <algorithm>
#include <array>
#include <bitset>
#include <cassert>
#include <cinttypes>
#include <cmath>
#include <cstdio>
#include <cstring>
#include <deque>
#include <functional>
#include <iostream>
#include <limits>
#include <list>
#include <map>
#include <numeric>
#include <queue>
#include <set>
#include <sstream>
#include <tuple>
#include <unordered_map>
#include <unordered_set>
#include <vector>
using namespace std;

string PrevGood(string S) {
  int N = S.size();
  int idx = -1;
  for (int i = 1; i < N; ++i) {
    if (S[i - 1] > S[i]) {
      idx = i - 1;
      break;
    }
  }

  if (idx == -1) {
    return S;
  }

  assert(S[idx] > '0');
  for (int i = idx + 1; i < N; ++i) {
    S[i] = '9';
  }
  --S[idx];
  while (idx > 0 && S[idx - 1] > S[idx]) {
    S[idx] = '9';
    --S[idx - 1];
    --idx;
  }

  if (idx == 0 && S[0] == '0') {
    S = S.substr(1);
    assert(count(S.begin(), S.end(), '9') == S.size());
  }

  assert(!S.empty());
  assert(S[0] > '0');
  return S;
}

void Test() {
  int N = 100001;
  vector<char> good(N, false);
  for (int i = 1; i < N; ++i) {
    char buf[20];
    sprintf(buf, "%d", i);
    good[i] = is_sorted(buf, buf + strlen(buf));
  }

  vector<int> near(N, -1);
  int last = -1;
  for (int i = 1; i < N; ++i) {
    if (good[i]) {
      last = i;
    }

    near[i] = last;
  }

  for (int i = 1; i < N; ++i) {
    char buf[20];
    sprintf(buf, "%d", i);

    int result = atoi(PrevGood(buf).c_str());
    assert(result == near[i]);
  }
  cout << "Done" << endl;
}

void Solve() {
  string S;
  cin >> S;
  cout << PrevGood(S) << endl;
}

int main() {
//  freopen("../Console/1.txt", "rb", stdin);
  freopen("../Console/B-large.in", "rb", stdin);
  freopen("../Console/B-large.out", "wb", stdout);
  ios_base::sync_with_stdio(false);
  cin.tie(nullptr);

//  Test();
//  return 0;

  int T;
  cin >> T;

  for (int tc = 0; tc < T; ++tc) {
    cout << "Case #" << tc + 1 << ": ";
    Solve();
  }

  return 0;
}
