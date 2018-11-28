// ya rab
#include <bits/stdc++.h>
#include <ext/hash_map>
#include <ext/numeric>

using namespace std;
using namespace __gnu_cxx;

#define FOR(i,a,b) for(int i=(a);i<(b);i++)
#define mp make_pair
#define pb push_back
#define oo (1 << 29)
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

//int dx[] = { 0, 0, 1, -1 };
//int dy[] = { 1, -1, 0, 0 };

const int N = 1500;
bool him[N], her[N], st;
int n, m, day = 24 * 60, period = 720, memo[N][N][2];

int rec(int c1, int c2, bool trn) {
  int cur = c1 + c2;
  if (cur == day)
    return c1 == period ? trn != st : oo;
  int &res = memo[c1][c2][trn];
  if (~res)
    return res;
  res = oo;
  if (trn) {
    if (!him[cur])
      res = min(res, rec(c1 + 1, c2, trn));
    if (!her[cur])
      res = min(res, rec(c1, c2 + 1, !trn) + 1);
  } else {
    if (!her[cur])
      res = min(res, rec(c1, c2 + 1, trn));
    if (!him[cur])
      res = min(res, rec(c1 + 1, c2, !trn) + 1);
  }
  return res;
}

int main() {
  ios::sync_with_stdio(false), cin.tie(NULL), cout.tie(NULL);
#ifndef ONLINE_JUDGE
  freopen("test.in", "rt", stdin);
  freopen("o.txt", "wt", stdout);
#endif
  int t;
  cin >> t;
  FOR (cs , 1 , t + 1)
  {
    cin >> n >> m;
    mem(him, 0), mem(her, 0);
    FOR (i , 0 , n)
    {
      int a, b;
      cin >> a >> b;
      FOR (j , a , b)
        him[j] = 1;
    }
    FOR (i , 0 , m)
    {
      int a, b;
      cin >> a >> b;
      FOR (j , a , b)
        her[j] = 1;
    }
    mem(memo, -1);
    st = 1;
    int res = rec(0, 0, 1);
    mem(memo, -1);
    st = 0;
    res = min(res, rec(0, 0, 0));
    printf("Case #%d: %d\n", cs, res);
  }
  return 0;
}
