#include<bits/stdc++.h>
using namespace std;
typedef long long ll;
#define sz(x) ((int)(x).size())
#define rep(i,l,r) for(int i=(l);i<(r);++i)
//-------
const int N = 1007;
const int INF = 1e9 + 7;
int n, D, k[N], s[N];
struct Node {
	ll x, y;
	Node() {
	}
	Node(ll _x, ll _y) {
		x = _x, y = _y;
		ll g = __gcd(x, y);
		if (g)
			x /= g, y /= g;
	}
	bool operator<(const Node &p) const {
		return x * p.y < y * p.x;
	}
};
int main() {
	freopen("A.out", "w", stdout);
	int T;
	scanf("%d", &T);
	rep(cas, 0, T) {
		scanf("%d%d", &D, &n);	
		Node mx = Node(0, 1);	
		rep(i, 0, n) {
			scanf("%d%d", &k[i], &s[i]);
			Node ti = Node(D - k[i], s[i]);
			if (mx < ti)
				mx = ti;
		}
//		printf("mx = %lld / %lld\n", mx.x, mx.y);
		double ans = 1.0 * D * mx.y / mx.x;	
		printf("Case #%d: %.12f\n", cas + 1, ans);
	}
	return 0;
}
