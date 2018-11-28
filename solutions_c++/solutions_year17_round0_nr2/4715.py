#include <iostream>
#include <stdio.h>
#include <algorithm>
#include <vector>

using namespace std;
int tt;
typedef long long ll;

ll get(ll N) {
	if ((0 <= N) && (N < 10)) return N;
	string str;
	for(ll n = N; n > 0; n /= 10) {
		str += char((n % 10) + '0');
	}
	reverse(str.begin(), str.end());
	int total = str.size(); int start = 0;
	for(start = 1; start < total; start++) {
		if (str[start] < str[start - 1]) break;
	}
	if (start == total) return N;
	ll rem = 0;
	for(int i = 0; i < start; i++) rem = (rem * 10LL) + (str[i] - '0');
	for(int i = start; i < total; i++) rem = rem * 10LL;
	return get(rem - 1);
}

void solve() {
	ll N; scanf("%lld", &N);
	printf("Case #%d: %lld\n", tt, get(N));
}
int main() {
	int t; scanf("%d", &t);
	for(tt=1; tt <= t; tt++) solve();
}
