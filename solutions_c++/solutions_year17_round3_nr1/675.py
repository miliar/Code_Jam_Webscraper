// ya rab
#include <bits/stdc++.h>
#include <ext/hash_map>
#include <ext/numeric>

using namespace std;
using namespace __gnu_cxx;

#define FOR(i,a,b) for(int i=(a);i<(b);i++)
#define mp make_pair
#define pb push_back
#define oo 1e16
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
#define sqr(x) ((x)*(x))
const int N = 1001;
int n, k;
pi arr[N];
long double memo[N][N][2], PI = 3.141592653589793238L;

long double rec(int i, int rem, bool fir) {
  if (i == n)
    return rem == 0 ? 0 : -oo;
  if (rem < 0)
    return -oo;
  long double &res = memo[i][rem][fir];
  if (res == res)
    return res;
  res = rec(i + 1, rem, fir);
  long double del = 0, area = PI * sqr((ll)arr[i].first);
  if (fir)
    del = area;
  res = max(res, rec(i + 1, rem - 1, 1) + area + 2 * PI * arr[i].first * arr[i].second - del);
  return res;
}

int main() {
  ios::sync_with_stdio(false), cin.tie(NULL), cout.tie(NULL);
#ifndef ONLINE_JUDGE
  freopen("test.in", "rt", stdin);
  freopen("out.txt", "wt", stdout);
#endif
  int t;
  cin >> t;
  FOR (cs , 1 , t + 1) {
    cin >> n >> k;
    FOR (i , 0 , n)
      cin >> arr[i].first >> arr[i].second;
    sort(arr, arr + n), reverse(arr, arr + n);
    mem(memo, -1);
    long double res = rec(0, k, 0);
    printf ("Case #%d: %.7Lf\n", cs, res);
  }
  return 0;
}
