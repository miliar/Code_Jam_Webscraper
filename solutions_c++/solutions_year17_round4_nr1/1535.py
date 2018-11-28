#include <algorithm>
#include <iostream>
#include <iomanip>
#include <cstdio>
#include <vector>
#include <map>
using namespace std;
#define int long long

int brute(vector <int> arr, int n, int p) {
	int num = 1;
	for (int i = 0; i < n; i++) {
		num *= (i + 1);
	}
	sort(arr.begin(), arr.end());
	int ans = 0;
	for (int i = 0; i < num; i++) {
		int scnt = 0;
		int left = 0;
		for (int j = 0; j < n; j++) {
			if (left == 0) {
				scnt++;
				left = (p - (arr[j] - left) % p) % p;
			} else {
				if (arr[j] >= left) {
					left = (p - (arr[j] - left) % p) % p;
				} else {
					left -= arr[j];
				}
			}
		}
		ans = max(ans, scnt);
		next_permutation(arr.begin(), arr.end());
	}
	return ans;
}

void sol() {
	int n, p;
	cin >> n >> p;
	vector <int> arr(n);
	vector <int> cnt(p, 0);
	for (int i = 0; i < n; i++) {
		cin >> arr[i];
		arr[i] %= p;
		cnt[arr[i]]++;
	}
	if (p == 2) {
		cout << cnt[0] + (cnt[1] + 1) / 2 << endl;
	} else if (p == 3) {
		if (cnt[2] > cnt[1]) {
			cout << cnt[0] + (cnt[1]) + (cnt[2] - cnt[1] + 2) / 3 << endl;
		} else {
			cout << cnt[0] + (cnt[2]) + (cnt[1] - cnt[2] + 2) / 3 << endl;
		}
	} else {
		int ans = 0;
		if (cnt[2] % 2 == 0) {
			if (cnt[1] > cnt[3]) {
				ans = cnt[0] + (cnt[2]) / 2 + (cnt[3]) + (cnt[1] - cnt[3] + 3) / 4;
			} else {
				ans = cnt[0] + (cnt[2]) / 2 + (cnt[1]) + (cnt[3] - cnt[1] + 3) / 4;
			}
		} else {
			if (cnt[1] > cnt[3]) {
				ans = cnt[0] + (cnt[2]) / 2 + (cnt[3]);
				int num = abs(cnt[3] - cnt[1]);
				ans += max(1LL + (max(0LL, (num - 2)) + 3)/4, (num + 3) / 4);
			} else {
				ans = cnt[0] + (cnt[2]) / 2 + (cnt[1]);
				int num = abs(cnt[3] - cnt[1]);
				ans += max(1LL + (max(0LL, (num - 2)) + 3)/4, (num + 3) / 4);
			}
		}
		cout << ans << endl;
	}
}


signed main() {
	freopen("input.txt", "r", stdin);
	freopen("output.txt", "w", stdout);

	int t;
	cin >> t;
	for (int i = 0; i < t; i++) {
		cout << "Case #" << i + 1 << ": ";
		sol();
	}

	fclose(stdin);
	fclose(stdout);
}