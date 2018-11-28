#include <iostream>
#include <vector>
#include <string>
#include <set>
#include <map>
#include <algorithm>

using namespace std;

void solve(int t) {
	int n, p;
	cin >> n >> p;
	int ans = 0;
	vector <int> arr(p);
	for (int i = 0; i < n; ++i) {
		int x;
		cin >> x;
		arr[x % p]++;
	}
	ans += arr[0];
	int a = 1;
	int b = p - a;
	if (p == 2) {
		ans += (arr[1] + 1) / 2;
		cout << "Case #" << t << ": " << ans << endl;
		return;
	}
	int mi = min(arr[a], arr[b]);
	ans += mi;
	arr[a] -= mi;
	arr[b] -= mi;
	if (p == 4) {
		ans += arr[2] / 2;
		arr[2] %= 2;
	}
	vector <int> trials;
	for (int i = 1; i < p; ++i)
		for (int r = 0; r < arr[i]; ++r)
			trials.push_back(i);
	int ma = 0;
	do {
		int cur = 0;
		int now = 0;
		for (int x : trials) {
			if (cur == 0)
				++now;
			cur = (cur + x) % p;
		}
		if (ma < now)
			ma = now;
	} while (next_permutation(trials.begin(), trials.end()));
	cout << "Case #" << t << ": " << ans + ma << endl;
}

int main() {
	freopen("A-large.in", "r", stdin);
	//freopen("input.txt", "r", stdin);
	freopen("output.txt", "w", stdout);
	int tc;
	cin >> tc;
	for (int t = 1; t <= tc; ++t)
		solve(t);
	return 0;
}