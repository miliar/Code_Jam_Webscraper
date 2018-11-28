#include <iostream>
#include <vector>
#include <set>
#include <map>
#include <algorithm>

using namespace std;
using i64 = long long;

struct E {
	i64 l, r;
};

bool operator < (const E &a, const E &b) {
	if (a.r - a.l != b.r - b.l)
		return a.r - a.l > b.r - b.l;
	return a.l < b.l;
}

void s_add(set <E> *arr, const E &e) {
	if (e.l <= e.r)
		arr->insert(e);
}

void solve(int t, i64 n, i64 k) {
	set <E> arr;
	arr.insert({ 1, n });
	for (int i = 0; i < k - 1; ++i) {
		auto e = *arr.begin();
		arr.erase(arr.begin());
		i64 mid = (e.l + e.r) / 2;
		s_add(&arr, { e.l, mid - 1 });
		s_add(&arr, { mid + 1, e.r });
	}

	auto e = *arr.begin();
	arr.erase(arr.begin());
	i64 mid = (e.l + e.r) / 2;
	i64 a = max(mid - e.l, e.r - mid);
	i64 b = min(mid - e.l, e.r - mid);
	cout << "Case #" << t << ": " << a << " " << b << endl;
}

void solve_fast(int t, i64 n, i64 k) {
	map <i64, i64> cnt;
	cnt[n / 2] = 1;
	++cnt[n - n / 2 - 1];
	--k;
	while (true) {
		i64 sum = 0;
		for (const auto &p : cnt)
			sum += p.second;
		sum /= 2;
		if (k < sum) {
			i64 a = k;
			i64 b = sum + k;
			i64 sa = -1;
			i64 sb = -1;
			i64 cur = 0;
			for (auto it = cnt.rbegin(); it != cnt.rend(); ++it) {
			//for (const auto &p : cnt) {
				auto p = *it;
				cur += p.second;
				if (cur > a && sa == -1)
					sa = p.first;
				if (cur > b && sb == -1)
					sb = p.first;

			}

			cout << "Case #" << t << ": " << sa << " " << sb << endl;
			return;
		}

		k -= sum;

		map <i64, i64> ncnt;
		for (const auto &p : cnt) {
			i64 a = p.first / 2;
			i64 b = p.first - p.first / 2 - 1;
			ncnt[a] += p.second;
			ncnt[b] += p.second;
		}
		cnt = ncnt;
	}
}

int main() {
	
	freopen("input.txt", "r", stdin);
	freopen("output.txt", "w", stdout);
	int tc;
	cin >> tc;
	for (int t = 1; t <= tc; ++t) {
		i64 n, k;
		cin >> n >> k;
		solve_fast(t, n, k);
	}
	
	//for (int i = 1; i <= 100; ++i) {
	//	solve(i, 100, i);
	//	solve_fast(i, 100, i);
	//}
}