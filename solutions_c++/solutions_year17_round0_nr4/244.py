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
#define N 111
using namespace std;
int T;
vector<int> e[2 * N];
bool visit[2 * N];
int match[2 * N];
bool bancol[2 * N];
bool banrow[2 * N];
bool bandplus[2 * N];
bool bandminus[2 * N];
char ori[2 * N][2 * N];
char cur[2 * N][2 * N];
bool dfs(int u) {
    int sz = e[u].size();
    for (int i = 0; i < sz; i++) {
        int v = e[u][i];
        if (!visit[v]) {
            visit[v] = true;
            if(match[v] == -1 || dfs(match[v])) {
                match[v] = u;
                return true;
            }
        }
    }
    return false;
}

int MaxMatch(int n) {
    int sum = 0;
    memset(match, -1, sizeof match);
    for(int i = 1; i <= n; i++) {
        memset(visit, false, sizeof visit);
        if (dfs(i))
            sum++;
    }
    return sum;
}
int n, m;
void ClearEdge() {
  for (int i = 0; i < 2 * N; i++)
    e[i].clear();
}
void work() {
  cin >> n >> m;
  memset(bancol, 0, sizeof bancol);
  memset(banrow, 0, sizeof banrow);
  memset(bandplus, 0, sizeof bandplus);
  memset(bandminus, 0, sizeof bandminus);
  memset(ori, 0, sizeof ori);
  memset(cur, 0, sizeof cur);
  ClearEdge();
  for (int i = 0; i < m; i++) {
    char ch;
    int x, y;
    cin >> ch >> x >> y;
    cur[x][y] = ori[x][y] = ch;
    if (ch == 'o') {
      bancol[x] = banrow[y] = bandplus[x + y] = bandminus[x - y + n] = true;
    }
    if (ch == '+') {
      bandplus[x + y] = bandminus[x - y + n] = true;
    }
    if (ch == 'x') {
      bancol[x] = banrow[y] = true;
    }
  }
  for (int i = 1; i <= n; i++)
    for (int j = 1; j <= n; j++)
      if (bancol[i] == false && banrow[j] == false)
        e[i].pb(j);
  MaxMatch(n);
  for (int j = 1; j <= n; j++)
    if (match[j] != -1) {
      int i = match[j];
      if (cur[i][j] == '+')
        cur[i][j] = 'o';
      else
        if (cur[i][j] != 'o')
          cur[i][j] = 'x';
    }
  ClearEdge();
  for (int i = 1; i <= n; i++)
    for (int j = 1; j <= n; j++)
      if (bandplus[i + j] == false && bandminus[i - j + n] == false)
        e[i + j].pb(i - j + n);
  MaxMatch(2 * n);
  for (int i = 1; i <= 2 * n; i++)
    if (match[i] != -1) {
      int j = match[i];
      int x = (j + i - n) / 2;
      int y = (j + n - i) / 2;
      //printf("i = %d j = %d\n", i, j);
      //printf("x = %d y = %d\n", x, y);
      if (cur[x][y] == 'x')
        cur[x][y] = 'o';
      else
        if (cur[x][y] != 'o')
          cur[x][y] = '+';
    }
    vector<pair<char, pair<int, int> > > sol;
    int ans = 0;
    for (int i = 1; i <= n; i++)
      for (int j = 1; j <= n; j++) {
        if (cur[i][j] == 'o') ans += 2;
        if (cur[i][j] == '+') ans ++;
        if (cur[i][j] == 'x') ans ++;
        if (cur[i][j] != ori[i][j]) {
          sol.pb(mp(cur[i][j], mp(i, j)));
        }
      }
    int len = sol.size();
    cout << ans << " " << len << endl;
    for (int i = 0; i < len; i++)
      cout << sol[i].first << " " << sol[i].second.first << " " << sol[i].second.second << endl;
}
int main() {
  freopen("in.txt", "r", stdin);
  freopen("out.txt", "w", stdout);
  scanf("%d", &T);
  for (int cas = 1; cas <= T; cas ++) {
    cout << "Case #" << cas << ": " ;
    work();
  }

}
