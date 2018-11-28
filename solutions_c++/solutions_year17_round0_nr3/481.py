// O(log n) time solution, should be good for large...

#include <algorithm>
#include <iostream>
#include <utility>
#include <vector>

using namespace std;

typedef long long ll;
typedef pair<ll, ll> PII;

PII sit(ll stalls) {
	stalls--;
	PII ans;
	ans.second = stalls / 2;
	ans.first = stalls - ans.second;
	return ans;
}

int main() {
	int T; cin >> T;
	for (int test = 1; test <= T; ++test) {
		ll n, k; cin >> n >> k;

		PII nums = make_pair(n, n - 1);
		PII counts = make_pair(1, 0);

		PII pii;
		while (true) {
			PII aa = sit(nums.first);
			PII bb = sit(nums.second);
			PII new_nums = make_pair(max(aa.first, bb.first), min(aa.second, bb.second));
			PII new_counts = make_pair(0, 0);

			k -= counts.first;
			if (k <= 0) { pii = aa; break; }
			if (aa.first == new_nums.first) new_counts.first += counts.first;
			if (aa.first == new_nums.second) new_counts.second += counts.first;
			if (aa.second == new_nums.first) new_counts.first += counts.first;
			if (aa.second == new_nums.second) new_counts.second += counts.first;

			k -= counts.second;
			if (k <= 0) { pii = bb; break; }
			if (bb.first == new_nums.first) new_counts.first += counts.second;
			if (bb.first == new_nums.second) new_counts.second += counts.second;
			if (bb.second == new_nums.first) new_counts.first += counts.second;
			if (bb.second == new_nums.second) new_counts.second += counts.second;

			nums = new_nums;
			counts = new_counts;
		}
		cout << "Case #" << test << ": " << pii.first << " " << pii.second << endl;
	}
	return 0;
}