// ya rab
#include <bits/stdc++.h>
#include <ext/hash_map>

using namespace std;
using namespace __gnu_cxx;

#define FOR(i,a,b) for(int i=(a);i<(b);i++)
#define mp make_pair
#define pb push_back
#define oo (1<<29)
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

int main() {
  ios::sync_with_stdio(false), cin.tie(NULL), cout.tie(NULL);
  freopen("test.in", "rt", stdin);
  freopen("o.txt", "wt", stdout);
  int t;
  cin >> t;
  FOR (cs, 1 , t + 1)
  {
    cout << "Case #" << cs << ": ";
    ll n, k;
    cin >> n >> k;
    ll c = 1;
    while (k) {
      if (k > c) {
        k -= c, n -= c;
      } else if (k == c) {
        ll r = n / c;
        r --, cout << (r + 1) / 2 << " " << r / 2 << endl;
        k = 0;
      } else {
        ll r = n / c + (n % c >= k);
        r --, cout << (r + 1) / 2 << " " << r / 2 << endl;
        k = 0;
      }
      c <<= 1LL;
    }
  }
  return 0;
}
