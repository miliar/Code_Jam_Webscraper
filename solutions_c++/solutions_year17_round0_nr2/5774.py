#define _CRT_SECURE_NO_WARNINGS
#ifdef _MSC_VER
#endif

#include <bits/stdc++.h>
#include <unordered_map>
#include<stack>
using namespace std;
#define OO ll(1e18)
#define MOD ll(100007)
typedef unsigned long long ull;
typedef long long ll;

vector<ll>N;

void gen(ll x) {
	if (x > 1e18)return;
	N.push_back(x);
	int a = x % 10;
	if (a == 0 && x == 0)a = 1;
	for (int i = a; i < 10; i++) {
		gen(x * 10 + i);
	}
}

int main() {
	freopen("B-large.in", "r", stdin);
	freopen("TextFile1.txt", "w", stdout);
	gen(0);
	sort(N.begin(), N.end());
	int T;
	scanf("%d", &T);
	for (int i = 1; i <= T; i++) {
		ll n;
		scanf("%lld", &n);
		int idx = lower_bound(N.begin(), N.end(), n) - N.begin();
		if (idx < N.size() && N[idx] == n)printf("Case #%d: %lld\n", i, n);
		else printf("Case #%d: %lld\n", i, N[idx - 1]);
	}
}