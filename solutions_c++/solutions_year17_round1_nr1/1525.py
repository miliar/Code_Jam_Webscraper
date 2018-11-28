// ya rab
#include <bits/stdc++.h>

using namespace std;

#define FOR(i,a,b) for(int i=(a);i<(b);i++)
#define mp make_pair
#define pb push_back
#define oo (1<<30)
#define sz(v) (int)v.size()
#define all(c) (c).begin(),(c).end()
#define rall(c) (c).rbegin(),(c).rend()
#define mem(s,v) memset(s,v,sizeof(s))
#define ppc(x) __builtin_popcount((x))
#define mt make_tuple // you can ignore
#define eb emplace_back

typedef long long ll;
typedef vector<int> vi;
typedef vector<ll> vll;
typedef vector<double> vd;
typedef vector<string> vs;
typedef pair<int, int> pi;
typedef vector<pi> vpi;

//int dx[] = { 0, 0, 1, -1 };
//int dy[] = { 1, -1, 0, 0 };

int main() {

  ios::sync_with_stdio(false), cin.tie(NULL), cout.tie(NULL);
#ifndef ONLINE_JUDGE
  freopen("test.in", "rt", stdin);
  freopen("o.txt", "wt", stdout);
#endif
  int t;
  cin >> t;
  FOR (cs, 1 , t + 1)
  {
    int r, c;
    cin >> r >> c;
    string g[30];
    FOR (i , 0 , r)
      cin >> g[i];
    FOR (i , 0 , r)
    {
      FOR (j , 0 , c)
      {
        if (g[i][j] != '?') {
          int k = j - 1;
          while (k >= 0 && g[i][k] == '?')
            g[i][k--] = g[i][j];
          k = j + 1;
          while (k < c && g[i][k] == '?')
            g[i][k++] = g[i][j];
        }
      }
    }
    FOR (i , 0 , r)
    {
      if (g[i][0] != '?') {
        int k = i - 1;
        while (k >= 0 && g[k][0] == '?')
          g[k--] = g[i];
        k = i + 1;
        while (k < r && g[k][0] == '?')
          g[k++] = g[i];
      }
    }
    printf("Case #%d:\n", cs);
    FOR (i , 0 , r)
      printf("%s\n", g[i].c_str());
  }
  return 0;
}
