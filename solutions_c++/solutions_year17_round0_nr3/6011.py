#include <bits/stdc++.h>
#define ull unsigned long long
#define PB push_back
#define MOD 1000000007
using namespace std;

struct sol {
	ull left;
	ull right;
	sol(ull l, ull r) : left{l}, right{r} {}
};


string solve(ull N, ull K) {
	string ans = "";
	priority_queue<int> pq;
	pq.push(N);

	for (ull i = 0; i < (K - 1); i++) {

		ull n = pq.top(); pq.pop();
		ull a, b;

		if (n & 1) {
			a = b = (n >> 1);
		} else {
			b = (n >> 1);
			a = b - 1;
		}

		pq.push(a); pq.push(b);
	}

	ull n = pq.top();
	ull a, b;
	if (n & 1) {
		a = b = (n >> 1);
	} else {
		b = (n >> 1);
		a = b - 1;
	}

	ostringstream oss;
	oss << b << " " << a;
	ans = oss.str();

	return ans;
}

int main() {
	ios::sync_with_stdio(false);
	int T; cin >> T;
	for (int i = 0; i < T; i++) {
		ull N, K; cin >> N >> K;

		cout << "Case #" << (i+1) << ": " << solve(N, K) << "\n"; 
	}
	return 0;
}
