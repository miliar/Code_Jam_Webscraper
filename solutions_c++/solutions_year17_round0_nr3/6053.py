#include <bits/stdc++.h>
using namespace std;

typedef long long ll;
const int N = 1005;
const int M = 100000007;

ll n, k;

int main() {
	freopen("C-small-2-attempt0.in", "r", stdin);
	freopen("out", "w", stdout);
    int C = 0, T;
    scanf("%d", &T);
    while (++C <= T) {
        scanf("%lld%lld", &n, &k);
		priority_queue<ll> que;
		que.push(n);
		ll x, y1, y2;
		while (k--) {
			x = que.top();
			que.pop();
			y1 = y2 = x / 2;
			if (~x & 1) { y1--; }
			//cout << x << ' ' << y1 << ' ' << y2 << endl;
			que.push(y1);
			que.push(y2);
		}
		printf("Case #%d: ", C);
		printf("%lld %lld\n", y2, y1);
	}
}
