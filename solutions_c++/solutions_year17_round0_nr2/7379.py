#include <string.h>
#include <algorithm>
#include <iostream>
#include <string>
#include <vector>
using namespace std;
typedef int64_t ll;
ll d[20][10][3];
ll N;
int len = 0;
vector<int> ar;
const char E = 0, F = 1, S = 2;
ll get(int pos, int num, int flag) {
  if (d[pos][num][flag] != -1) return d[pos][num][flag];
  if (pos == 0) {
    if (flag == F) return 0;
    if (flag == S) return 1;
    if (flag == E) return 1;
  }
  if (flag == F) {
    return 0;
  }
  ll& r = d[pos][num][flag];
  r = 0;
  for (int dig = num; dig <= 9; ++dig) {
    if (flag == E) {
      int nflag;
      if (dig == ar[pos - 1]) nflag = E;
      if (dig < ar[pos - 1]) nflag = S;
      if (dig > ar[pos - 1]) nflag = F;

      r += get(pos - 1, dig, nflag);
    }
    if (flag == S) {
      int nflag = S;
      r += get(pos - 1, dig, nflag);
    }
  }
  return r;
}

void find(int pos, int num, int flag, ll cur) {
  if (pos == 0) {
    std::cout << cur;
    return;
  }
  for (int dig = 9; dig >= num; --dig) {
    if (flag == E) {
      int nflag;
      if (dig == ar[pos - 1]) nflag = E;
      if (dig < ar[pos - 1]) nflag = S;
      if (dig > ar[pos - 1]) nflag = F;
      if (get(pos - 1, dig, nflag)) {
        find(pos - 1, dig, nflag, cur * 10 + dig);
        return;
      }
    }
    if (flag == S) {
      int nflag = S;
      if (get(pos - 1, dig, nflag)) {
        find(pos - 1, dig, nflag, cur * 10 + dig);
        return;
      }
    }
  }
  return;
}
void solve() {
  memset(d, -1, sizeof d);
  cin >> N;
  ll k = N;
  ar.clear();
  while (k) ar.push_back(k % 10), k /= 10;
  // reverse(ar.begin(), ar.end());
  get(ar.size(), 0, E) - 1;
  find(ar.size(), 0, E, 0);
}
int main() {
  int t;
  cin >> t;
  for (int i = 1; i <= t; ++i) {
    cout << "Case #" << i << ": ";
    solve();
    cout << endl;
  }
}
