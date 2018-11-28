// CONTEST SOURCE
#include <iostream>
#include <sstream>
#include <set>
#include <cstdlib>
#include <cstring>
#include <cstdio>
#include <vector>
#include <cmath>
#include <algorithm>
#include <map>
#include <queue>
//#include <priority_queue>
using namespace std;
#define ll long long
#define x first
#define y second
#define pii pair<int, int>
#define pdd pair<double, double>
#define L(s) (int)(s).size()
#define VI vector<int>
#define all(s) (s).begin(), (s).end()
#define pb push_back
#define mp make_pair
#define ull unsigned ll
#define inf 1000000000
int t, n, m;
char a[55][55];
char col[55];
int f[55][1 << 5][1 << 5];
int main() {
  freopen("C-small-attempt1.in", "r", stdin);
  freopen("output.txt", "w", stdout);
  cin >> t;
  for(int tc = 1; tc <= t; ++tc) {
    cerr << tc << endl;
    cin >> n >> m;
    for(int i = 0; i < n; ++i) {
      for(int j = 0; j < m; ++j) {
        cin >> a[i][j];
      }
    }
    memset(f, -1, sizeof(f));
    f[0][0][0] = 0;
    for(int j = 0; j < m; ++j) {
      for(int mask = 0; mask < (1 << n); ++mask) {
        for(int need = 0; need < (1 << n); ++need) {
          if (f[j][mask][need] == -1) continue;
          for(int act = 0; act < (1 << n); ++act) {
            bool ok = 1;
            for(int i = 0; i < n; ++i) if (a[i][j] != '|' && a[i][j] != '-' && (act & (1 << i))) ok = 0;
            for(int i = 0; i < n; ++i) if ((a[i][j] == '|' || a[i][j] == '-') && (mask & (1 << i))) ok = 0;
            if (!ok) continue;
            for(int i = 0; i < n; ++i) {
              col[i] = a[i][j];
              if (a[i][j] == '|' && (act & (1 << i))) col[i] = '-';
              if (a[i][j] == '-' && (act & (1 << i))) col[i] = '|';
            }
            for(int i = 0; i < n; ++i) {
              if (col[i] == '|') {
                int pos;
                pos = i - 1; while(pos >= 0 && col[pos] == '.') --pos;
                if (pos >= 0 && (col[pos] == '|' || col[pos] == '-')) ok = 0;
                pos = i + 1; while(pos < n && col[pos] == '.') ++pos;
                if (pos < n && (col[pos] == '|' || col[pos] == '-')) ok = 0;
              }
              if (col[i] == '-') {
                int pos;
                pos = j - 1; while(pos >= 0 && a[i][pos] == '.') --pos;
                if (pos >= 0 && (a[i][pos] == '|' || a[i][pos] == '-')) ok = 0;
                pos = j + 1; while(pos < m && a[i][pos] == '.') ++pos;
                if (pos < m && (a[i][pos] == '|' || a[i][pos] == '-')) ok = 0;
              }

            }
            for(int i = 0; i < n; ++i) {
              if ((need & (1 << i)) && col[i] != '-' && col[i] != '.') ok = 0;
            }
            if (!ok) continue;
            //cerr << j << " " << mask << " " << act << endl;
            //for(int i = 0; i < n; ++i) cerr << col[i] << endl;
            int nask = mask;
            int nneed = 0;
            for(int i = 0; i < n; ++i) {
              if (col[i] == '#' && (nask & (1 << i))) nask -= (1 << i);
              if (col[i] == '-') nask |= (1 << i);
              if ((need & (1 << i)) && col[i] != '-') nneed |= (1 << i);
              if (col[i] == '.' && !(mask & (1 << i))) {
                int pos;
                pos = i - 1; while(pos >= 0 && col[pos] == '.') --pos;
                if (pos >= 0 && col[pos] == '|') continue;
                pos = i + 1; while(pos < n && col[pos] == '.') ++pos;
                if (pos < n && col[pos] == '|') continue;
                nneed |= (1 << i);
              }
            }
            if (f[j + 1][nask][nneed] == -1) {
              f[j + 1][nask][nneed] = (((mask << n) + need) << n) + act;
            }
          }
        }
      }
    }
    int mask = 0, need = 0;
    while(mask < (1 << n) && f[m][mask][need] == -1) ++mask;
    cout << "Case #" << tc << ": ";
    if (mask == (1 << n)) { cout << "IMPOSSIBLE\n"; continue; }
    cout << "POSSIBLE\n";
    for(int j = m; j > 0; --j) {
      int act = f[j][mask][need] % (1 << n);
      for(int i = 0; i < n; ++i) if (act & (1 << i)) {
        if (a[i][j - 1] == '-') a[i][j - 1] = '|'; else a[i][j - 1] = '-';
      }
      int tmp = f[j][mask][need] / (1 << n);
      mask = tmp / (1 << n);
      need = tmp % (1 << n);
    }
    for(int i = 0; i < n; ++i) {
      for(int j = 0; j < m; ++j) {
        cout << a[i][j];
      }
      cout << endl;
    }
  }
}
