#include <iostream>
#include <string>
#include <vector>
#include <map>

using namespace std;

struct q {
	long long l, r, i;
	q(long long l = 0, long long r = 0, long long i = 0) : l(l), r(r), i(i) {}
	bool operator < (const q& other) const {
		vector < long long > a = {-min(l, r), -max(l, r), i};
		vector < long long > b = {-min(other.l, other.r), -max(other.l, other.r), other.i};
		return a < b;
	}
	void print() const {
		cout << l << " " << r << " " << i << endl;
	}
};

const int maxn = 1e6 + 10;
bool used[maxn];

pair < long long, long long > got(long long n) {
	long long l = (n - 1) / 2;
	long long r = n - 1 - l;
	if (l < r) {
		swap(l, r);
	}
	return {l, r};
}

void solve() {
	long long n = 0;
	long long k = 0;
	cin >> n >> k;
	map < pair < long long, long long>, long long> cnt1, cnt2;
	cnt1[got(n)] += 1;
	while (k > 0) {
		cnt2.clear();
		vector < q > a;
		for (const auto& it: cnt1) {
			long long n1 = it.first.first;
			long long n2 = it.first.second;
			long long ct = it.second;
			a.push_back(q(n1, n2, ct));
			if (n1)
				cnt2[got(n1)] += ct;
			if (n2)
				cnt2[got(n2)] += ct;
		}
		sort(a.begin(), a.end());
		for (int i = 0; i < a.size(); i++) {
			k -= a[i].i;
			if (k <= 0) {
				cout << a[i].l << " " << a[i].r << endl;
				return;
			}
		}
		swap(cnt1, cnt2);
	}
}

int main() {
	int test = 0;
	cin >> test;
	for (int i = 1; i <= test; i++) {
		cout << "Case #" << i << ": ";
		solve();
	}
	return 0;
}