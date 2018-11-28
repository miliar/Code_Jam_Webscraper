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

long long t, n;
vector<int> v, ans;

void toV(long long x) {
	v.clear();
	while (x) {
		v.pb(x % 10);
		x /= 10;
	}
	// reverse(v.begin(), v.end());
}

void solve() {
	toV(n);
	int id = 0;
	int lat = -1;
	while (id < v.size() - 1) {
		if (v[id] < v[id + 1]) {
			lat = id;
			v[id + 1]--;
		}
		id++;
	}
	REP (i, 1 + lat) v[i] = 9;
	while (!v.back()) v.pop_back();
	reverse(v.begin(), v.end());
	for (auto i: v) cout << i;
	cout << endl;
}


int main() {
  ios::sync_with_stdio(false);
  cin >> t;
  FOR (cas, 1, t) {
  	cout << "Case #" << cas << ": ";
  	cin >> n;
  	solve();
  }
}
