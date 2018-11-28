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

int nb_case, r, c;
char a[13][13], frs[13], lst[13];
bool no[13];

int main(int argc, char const *argv[]) {
#ifndef ONLINE_JUDGE
  freopen("A-small-attempt1.in", "r", stdin);
  freopen("A-small-attempt1.out", "w", stdout);
#endif
  ios_base::sync_with_stdio(0);
  cin.tie(0);

  cin >> nb_case;
  range(tcase, 1, nb_case + 1, 1) {
    cin >> r >> c;

    memset(no, true, sizeof(no));

    range(i, 0, r, 1) {
      range(j, 0, c, 1) { cin >> a[i][j]; }
    }

    range(i, 0, r, 1) {
      range(j, 0, c, 1) {
        if (a[i][j] != '?') {
          no[i] = false;
          break;
        }
      }
    }

    range(i, 0, r, 1) {
      if (!no[i]) {
        range(j, 0, c, 1) {
          if (a[i][j] != '?') {
            lst[i] = a[i][j];
          }
        }
      } else {
        lst[i] = '?';
      }
    }

    range(i, 0, r, 1) {
      if (!no[i]) {
        range(j, c - 1, -1, -1) {
          if (a[i][j] != '?') {
            frs[i] = a[i][j];
          }
        }
      } else {
        frs[i] = '?';
      }
    }

    range(i, 0, r, 1) {
      if (!no[i]) {
        char last = frs[i];
        range(j, 0, c, 1) {
          if (a[i][j] == '?') {
            a[i][j] = last;
          } else {
            last = a[i][j];
          }
        }
      }
    }

    range(i, 0, r, 1) {
      if (!no[i]) {
        char last = lst[i];
        range(j, c - 1, -1, -1) {
          if (a[i][j] == '?') {
            a[i][j] = last;
          } else {
            last = a[i][j];
          }
        }
      }
    }

    range(i, 1, r, 1) {
      if (no[i] && !no[i - 1]) {
        range(j, 0, c, 1) {
          a[i][j] = a[i - 1][j];
          no[i] = false;
        }
      }
    }

    range(i, r - 2, -1, -1) {
      if (no[i] && !no[i + 1]) {
        range(j, 0, c, 1) {
          a[i][j] = a[i + 1][j];
          no[i] = false;
        }
      }
    }

    // range(i, 0, r, 1) cout << frs[i] << ", ";
    // cout << endl;
    // range(i, 0, r, 1) cout << lst[i] << ", ";
    // cout << endl;

    cout << "Case #" << tcase << ":" << endl;
    range(i, 0, r, 1) {
      range(j, 0, c, 1) { cout << a[i][j]; }
      cout << endl;
    }
  }

  return 0;
}