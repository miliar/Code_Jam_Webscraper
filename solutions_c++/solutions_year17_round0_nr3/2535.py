#include <bits/stdc++.h>
using namespace std;
#define FOR(i,a,b) for (int i = (a); i <= (b); i++)
#define FORD(i,a,b) for (int i = (a); i >= (b); i--)
#define REP(i,a) FOR(i,0,(int)(a)-1)
#define reset(a,b) memset(a,b,sizeof(a))
#define BUG(x) cout << #x << " = " << x << endl
#define PR(x,a,b) {cout << #x << " = "; FOR (_,a,b) cout << x[_] << ' '; cout << endl;}
#define CON(x) {cout << #x << " = "; for(auto i:x) cout << i << ' '; cout << endl;}
#define mod 1000000007
#define pi acos(-1)
#define eps 0.00000001
#define pb push_back
#define sqr(x) (x) * (x)
#define _1 first
#define _2 second

long long t, n, k;

long long solve(long long tot, long long high, long long low, long long rem) {
	if (rem <= high) return tot;
	else if (rem <= high + low) return tot - 1;
	if (tot & 1) return solve(tot / 2, high * 2 + low, low, rem - high - low);
	else return solve(tot / 2, high, high + low * 2, rem - high - low);
}

int main() {
  ios::sync_with_stdio(false);
  cin >> t;
  FOR (cas, 1, t) {
  	cout << "Case #" << cas << ": ";
  	cin >> n >> k;
  	long long ans = solve(n, 1, 0, k);
  	if (ans & 1) cout << ans / 2 << ' ' << ans / 2 << endl;
  	else cout << ans / 2 << ' ' << ans / 2 - 1 << endl;
  }
}
