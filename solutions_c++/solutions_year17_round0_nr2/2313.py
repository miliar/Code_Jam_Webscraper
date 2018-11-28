#include <stdio.h>
#include <bits/stdc++.h>			

#define pb push_back
#define pp pop_back
#define sz(a) (int)(a.size())
#define mp make_pair
#define F first
#define S second
#define next _next
#define prev _prev
#define left _left
#define right _right
#define y1 _y1
#define all(x) x.begin(), x.end()

using namespace std;

typedef long long ll;
typedef unsigned long long ull;
typedef long double ld;
typedef pair<int, int> pii;
typedef pair<ll, ll> pll;

const int N = (int)1e6 + 123;
const ll INF = (ll)1e18 + 123;
const int inf = (int)1e9 + 123;
const int MOD = (int)1e9 + 7;

ll n;
vector<int> v, g;

void solve(int test) {
	g.clear(), v.clear();
	cin >> n;
	while(n > 0) v.pb(n % 10), n /= 10;
	reverse(all(v));
	for(int i = 0; i < sz(v); i ++) {
		if(sz(g) && g.back() > v[i]) {
			int tmp = g.back();
			while(sz(g) && g.back() == tmp)
				g.pp();
			if(tmp - 1 > 0) g.pb(tmp - 1);
			break;
		}
		g.pb(v[i]);
	}
	int to = sz(v);
	if(!sz(g)) to --;
	while(sz(g) < to) g.pb(9);
	cout << "Case #" << test << ": ";
	for(auto i : g) cout << i;
	cout << "\n";
}

int main() {
	freopen(".in", "r", stdin);
	freopen(".out", "w", stdout);
	ios_base::sync_with_stdio(0);
	cin.tie(0);
	unsigned int FOR;
 	asm("rdtsc" : "=A"(FOR));
  	srand(FOR);
	int t;
	cin >> t;
	for(int it = 1; it <= t; it ++)
		solve(it);	
	return 0;
}
