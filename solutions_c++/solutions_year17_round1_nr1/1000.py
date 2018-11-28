#include <iostream>
#include <cstdio>
#include <cstring>
#include <cstdlib>
#include <cmath>
#include <algorithm>
#include <string>
#include <vector>
#include <map>
#include <set>
#include <queue>
#include <stack>
#include <bitset>
#include <list>
#include <sstream>
#include <ctime>
#include <functional>
#define pi 3.14159265358979323846264338327950288
#define pb push_back
#define mp make_pair
#define X first
#define Y second
#define LL long long
#define LD long double
#define INF 1000000000
#define INFll 1000000000000000000ll
#define Vi vector<int>
#define VI Vi::iterator
#define Mi map<int, int>
#define MI Mi::iterator
#define Si set<int>
#define SI Si::iterator
#define FOR(i,s,e) for (int i=(s); i<(e); i++)
#define FOE(i,s,e) for (int i=(s); i<=(e); i++)
#define FOD(i,s,e) for (int i=(s)-1; i>=(e); i--)
#define CLR(a,x) memset(a, x, sizeof(a))
#define SZ(x) ((int)x.size())
#define mid (l + r) / 2
#define Left k * 2, l, mid
#define Right k * 2 + 1, mid + 1, r
#define N 1111
using namespace std;
int T;
int n, m;
vector<char> alpha;
vector<pair<int, int> > pos;
char a[N][N];
bool stop;
int k, sz;
int minx[N], miny[N], maxx[N], maxy[N];
bool check() {
  memset(minx, 0x3f, sizeof minx);
  memset(miny, 0x3f, sizeof miny);
  memset(maxx, 0, sizeof maxx);
  memset(maxy, 0, sizeof maxy);
  for (int i = 0; i < n; i++)
    for (int j = 0; j < m; j++) {
      minx[a[i][j]] = min(minx[a[i][j]], i);
      maxx[a[i][j]] = max(maxx[a[i][j]], i);
      miny[a[i][j]] = min(miny[a[i][j]], j);
      maxy[a[i][j]] = max(maxy[a[i][j]], j);
    }
  for (int c = 0; c < k; c++) {
    char ch = alpha[c];
    for (int i = minx[ch]; i <= maxx[ch]; i++)
      for (int j = miny[ch]; j <= maxy[ch]; j++)
        if (a[i][j] != ch) return false;
  }
  return true;
}
void dfs(int depth) {
  if (depth == sz) {
    if (check()) {
      stop = true;
      for (int i = 0; i < n; i++) {
        for (int j = 0; j < m; j++)
          cout << a[i][j];
        cout << endl;
      }

    }
    return;
  }
  for (int i = 0; i < k; i++) {
    a[pos[depth].X][pos[depth].Y] = alpha[i];
    dfs(depth + 1);
    if (stop) return;
  }
}
void work() {
  cin >> n >> m;
  alpha.clear();
  pos.clear();
  stop = false;
  for (int i = 0; i < n; i++)
    for (int j = 0; j < m; j++) {
      cin >> a[i][j];
      if (a[i][j] == '?') {
        pos.pb(mp(i, j));
      }
      else
        alpha.pb(a[i][j]);
    }
  alpha.erase(unique(alpha.begin(), alpha.end()), alpha.end());
  k = alpha.size();
  sz = pos.size();
  dfs(0);
}
int main() {
  freopen("in.txt", "r", stdin);
  freopen("out.txt", "w", stdout);
  scanf("%d", &T);
  for (int cas = 1; cas <= T; cas ++) {
    cout << "Case #" << cas << ": "  << endl;
    work();
  }

}
