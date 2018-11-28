#include <algorithm>
#include <cmath>
#include <cstdio>
#include <cstring>
#include <iostream>
#include <numeric>

#include <deque>
#include <map>
#include <queue>
#include <stack>
#include <vector>

using namespace std;

typedef long long lint;

#define range(i, a, b, step)                                                   \
  for (int i = (a); i != (int)(b) && ((i - (int)(b)) ^ (int)(step)) < 0;       \
       i += (int)(step))
#define cache(i, a, b, step)                                                   \
  for (int i = (a), i##b = (int)(b), i##step = (int)(step);                    \
       i != i##b && ((i - i##b) ^ i##step) < 0; i += i##step)

const int maxv = 20;

string s;
int t, a[maxv];

bool solve(int i) {
  if (i < s.length() + 1) {
    if (a[i - 1] > a[i]) {
      a[i] = -9;
      return true;
    } else {
      if (solve(i + 1)) {
        if (a[i] == 0) {
          a[i] = -9;
          return true;
        } else {
          a[i] -= 1;
          if (a[i - 1] > a[i]) {
            a[i] = -9;
            return true;
          } else {
            return false;
          }
        }
      }
    }
  }
  return false;
}

int main(int argc, char const *argv[]) {
#ifndef ONLINE_JUDGE
  freopen("B-large.in", "r", stdin);
  freopen("B-large.out", "w", stdout);
#endif
  ios_base::sync_with_stdio(0);
  cin.tie(0);

  cin >> t;
  range(tcase, 1, t + 1, 1) {
    cin >> s;
    a[0] = -1;
    int len = s.length() + 1;

    range(i, 1, len, 1) { a[i] = s[i - 1] - '0'; }
    solve(1);

    // range(i, 1, len, 1) { cout << (int)a[i] << ", "; }
    // cout << endl;

    int i = 1;
    while (i < len) {
      if (a[i] != 0) {
        break;
      }
      i += 1;
    }
    cout << "Case #" << tcase << ": ";
    bool all_nice = false;
    while (i < len) {
      if (a[i] == -9)
        all_nice = true;

      if (all_nice)
        cout << 9;
      else
        cout << a[i];

      i += 1;
    }
    cout << endl;
  }

  return 0;
}