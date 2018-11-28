#include <bits/stdc++.h>
using namespace std;
typedef long long ll;
#define DEBUG
#ifdef DEBUG
#define TRACE(x) cerr << #x << " = " << x << endl;
#define _ << " _ " <<
#else
#define TRACE(x) ((void)0)
#endif

int ans[1005];
int cnts[3][3];
pair<int, char> mp[3];
char cs[3][2] =
{{'R', 'G'},
 {'Y', 'V'},
 {'B', 'O'}};

int main() {
  ios_base::sync_with_stdio(false); cin.tie(NULL); cout.tie(NULL);
  int T;
  cin >> T;
  for (int tt = 1; tt <= T; tt++) {
    cout << "Case #" << tt << ": ";
    int n, R, O, Y, G, B, V, gaps;
    cin >> n >> R >> O >> Y >> G >> B >> V;
    fill(&cnts[0][0], &cnts[0][0] + sizeof(cnts) / sizeof(cnts[0][0]), 0);
    cnts[0][0] = R - 2 * G;
    cnts[0][1] = G;
    cnts[1][0] = Y - 2 * V;
    cnts[1][1] = V;
    cnts[2][0] = B - 2 * O;
    cnts[2][1] = O;
    for (int i = 0; i < 3; i++) {
      if (cnts[i][0] < 0) {
        if (cnts[i][1] <= -cnts[i][0]) {
          if (-cnts[i][0] == cnts[i][1]) { // special case
            bool good = true;
            for (int j = 0; j < 3; j++)
              if (j != i && (cnts[j][0] != 0 || cnts[j][1] != 0))
                good = false;
            if (good) {
              for (int j = 0; j < n; j++)
                cout << cs[i][j % 2];
              cout << '\n';
              goto skipcase;
            } else {
              cout << "IMPOSSIBLE\n";
              goto skipcase;
            }
          } else {
            cout << "IMPOSSIBLE\n";
            goto skipcase;
          }
        }
        cnts[i][1] -= -cnts[i][0];
        cnts[i][2] += -cnts[i][0];
        cnts[i][0] = 0;
      }
    }

    n = 0;
    for (int i = 0; i < 3; i++)
      n += cnts[i][0] + cnts[i][1];

    mp[0] = {cnts[0][0] + cnts[0][1], 0};
    mp[1] = {cnts[1][0] + cnts[1][1], 1};
    mp[2] = {cnts[2][0] + cnts[2][1], 2};
    sort(mp, mp + 3);
    gaps = n - mp[2].first * 2;
    if (gaps < 0) {
      cout << "IMPOSSIBLE\n";
      continue;
    }
    fill(ans, ans + n + 1, 0);
    for (int i = 0; i < n;) {
      ans[i] = 2;
      if (mp[1].first > 0) {
        ans[i + 1] = 1;
        mp[1].first--;
      }
      i += 2;
      if (gaps > 0) {
        gaps--;
        i++;
      }
    }
    for (int ii = 0; ii < n; ii++) {
      const int id = mp[ans[ii]].second;
      if (cnts[id][1] > 0) {
        cout << cs[id][0] << cs[id][1] << cs[id][0];
        if (cnts[id][2] > 0) {
          for (int i = 0; i < cnts[id][2]; i++)
            cout << cs[id][1] << cs[id][0];
          cnts[id][2] = 0;
        }
        cnts[id][1]--;
      } else {
        assert(cnts[id][0] > 0);
        cout << cs[id][0];
        cnts[id][0]--;
      }
    }
    cout << '\n';
skipcase:;
  }

  return 0;
}
