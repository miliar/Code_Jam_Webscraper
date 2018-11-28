#include <cstdio>
#include <string>
#include <iostream>
using namespace std;
#define ll long long
#define mp make_pair
FILE *fi = freopen("C-large.in", "r", stdin);
FILE *fo = freopen("outCL.txt", "w", stdout);
int test;
ll n, k;
pair<ll, ll> go()
{
	ll base = 1;
	ll node = n;
	ll a = 1;//Max node cnt
	while (1) {
		if (base <= k && k <= base + a - 1) {
			return mp(node / 2, node / 2 - (node % 2 == 0));
		}
		if (base + a <= k && k <= base * (ll)2 - 1) {
			--node;
			return mp(node / 2, node / 2 - (node % 2 == 0));
		}
		if (node & 1)a = base + a;
		node /= (ll)2;
		base *= (ll)2;
	}
}
int main() {
	int lev = 0;
	scanf("%d", &test);
	while (test--) {
		++lev;
		scanf("%lld %lld", &n, &k);
		pair<ll, ll> ans = go();
		printf("Case #%d: %lld %lld\n", lev, ans.first, ans.second);
	}
	return 0;
}