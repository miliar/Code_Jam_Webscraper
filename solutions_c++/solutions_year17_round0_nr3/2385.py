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

set<ll> st;
map<ll, ll> cnt;
ll n, k;

void solve(int test) {
	st.clear(), cnt.clear();
	cin >> n >> k;
	st.insert(n);  
	cnt[n] = 1;
	ll mn = inf, mx = -inf, added = 0;
	while(1) {
		ll len = *--st.end();
		st.erase(--st.end());
		added += cnt[len];
		ll len1 = len / 2 + len % 2;
		ll len2 = len - len1;
		len1 --;
		if(added >= k) {
			mn = min(len1, len2), mx = max(len1, len2);
			break;			
		}
		if(len1 > 0) cnt[len1] += cnt[len], st.insert(len1);
		if(len2 > 0) cnt[len2] += cnt[len], st.insert(len2);
	}
	cout << "Case #" << test << ": " << mx << " " << mn << "\n";
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
