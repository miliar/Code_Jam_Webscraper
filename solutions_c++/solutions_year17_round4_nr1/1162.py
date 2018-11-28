#include <bits/stdc++.h>
using namespace std;

int transition(int x, int d, int P) {
	x -= d;
	x += P;
	x %= P;
	return x;
}


map<long long, int> mem;
int solve(int a, int b, int c, int d, int rem, int P) {
	if (a == 0 && b == 0 && c == 0 && d == 0)
		return 0;
	long long state = P;
	state += rem * 10LL;
	state += d * 100LL;
	state += c * 100000LL;
	state += b * 100000000LL;
	state += a * 100000000000LL;
	if (mem.find(state) != mem.end())
		return mem[state];
	int ans = 0;
	if (a)
		ans = max(ans, solve(a - 1, b, c, d, rem, P));
	if (b)
		ans = max(ans, solve(a, b - 1, c, d, transition(rem, 1, P), P));
	if (c)
		ans = max(ans, solve(a, b, c - 1, d, transition(rem, 2, P), P));
	if (d)
		ans = max(ans, solve(a, b, c, d - 1, transition(rem, 3, P), P));
	ans += (rem == 0);
	return mem[state] = ans;
}


int main() {
	ios::sync_with_stdio(0);
	freopen("/home/ahmed/Desktop/r9ound 2/A-large.in", "r", stdin);
	freopen("/home/ahmed/Desktop/r9ound 2/A-large.out", "w", stdout);
	int id = 1;
	int t; cin >> t;
	while (t--) {
		int n, p; cin >> n >> p;
		int cnt[4] = {0, 0, 0, 0};
		for (int i = 0; i < n; i++) {
			int x; cin >> x;
			cnt[x % p] += 1;
		}
		cout << "Case #" << id++ << ": " << solve(cnt[0], cnt[1], cnt[2], cnt[3], 0, p) << endl;
	}


	return 0;
}

