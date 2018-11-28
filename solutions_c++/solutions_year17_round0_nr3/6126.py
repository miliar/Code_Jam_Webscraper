#include <bits/stdc++.h>
#define f first
#define s second
#define mp make_pair
#define pb push_back
#define all(c) (c).begin(), (c).end()
#define sqr(x) ((x)*(x))
#define fname ""

using namespace std;

typedef long long ll;
const double eps = 1e-9;
const double PI = acos(-1.0);
const int inf = (int) 1e9 + 7;
const ll INF = (ll) 1e18 + 7;
const int mod = (int) 1e9 + 7;
const int N = (int) 2e5 + 7;

int t, n, k, ans1, ans2;

void f() {
	multiset <int> s;
	s.insert(n);
	for(int i = 0; i < k; i ++) {
		int x = *s.rbegin();
		s.erase(--s.end());
		ans1 = x / 2;
		ans2 = (x - 1) / 2;
		s.insert(x / 2);
		s.insert((x - 1) / 2);
	}
}

int main () {
   	//freopen(fname".in", "r", stdin);
   	freopen("output.txt", "w", stdout);
   	ios_base::sync_with_stdio(0);

   	cin >> t;
   	for(int i = 0; i < t; i ++) {
   	 	cin >> n >> k;
   	 	f();
   	 	cout << "Case #" << i + 1 << ": " << ans1 << ' ' << ans2 << '\n';
   	}
   	return 0;
}   