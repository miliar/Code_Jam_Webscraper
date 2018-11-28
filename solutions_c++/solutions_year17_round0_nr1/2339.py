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

int t;      
string s;
bool ok[1111];
int k;

void solve(int test) {
	cin >> s >> k;
	for(int i = 0; i < sz(s); i ++) {
		ok[i] = 1;
		if(s[i] == '-') ok[i] = 0;
	}
	int l = 0, r = k - 1, cnt = 0;
	while(r < sz(s)) {
		if(!ok[l]) {
			cnt ++;
			for(int j = l; j <= r; j ++)
				ok[j] ^= 1;
		}
		l ++, r ++;
	}
	bool imp = 0;
	for(int i = 0; i < sz(s); i ++)
		if(!ok[i]) imp = 1;
	cout << "Case #" << test << ": ";
	if(imp) cout << "IMPOSSIBLE\n";
	else cout << cnt << "\n";
}

int main() {
	freopen(".in", "r", stdin);
	freopen(".out", "w", stdout);
	ios_base::sync_with_stdio(0);
	cin.tie(0);
	unsigned int FOR;
 	asm("rdtsc" : "=A"(FOR));
  	srand(FOR);
	cin >> t;
	for(int it = 1; it <= t; it ++)
		solve(it);	
	return 0;
}
