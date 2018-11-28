#include <bits/stdc++.h>
using namespace std;

int freq[4];

int main() {

	freopen("readin.txt", "r", stdin);
	freopen("out.txt", "w", stdout);

	int t;
	scanf("%d", &t);
	while (t--) {
		memset(freq, 0, sizeof freq);
		int n, p;
		scanf("%d%d", &n, &p);
		for (int i = 0, a; i < n; i++) {
			scanf("%d", &a);
			freq[a % p]++;
		}
		vector<int> v;
		int ans = 0;
		if (p == 2) {
			while (freq[0]) {
				v.push_back(0);
				freq[0]--;
			}
			while (freq[1] >= 2) {
				freq[1] -= 2;
				v.push_back(1);
				v.push_back(1);
			}
		} else if (p == 3) {
			while (freq[0]) {
				v.push_back(0);
				freq[0]--;
			}
			while (freq[1] && freq[2]) {
				v.push_back(1);
				v.push_back(2);
				freq[1]--, freq[2]--;
			}
			while (freq[1] >= 3) {
				v.push_back(1);
				v.push_back(1);
				v.push_back(1);
				freq[1] -= 3;
			}
		} else if (p == 4) {
			while (freq[0]) {
				v.push_back(0);
				freq[0]--;
			}
			while (freq[1] && freq[3]) {
				v.push_back(1);
				v.push_back(3);
				freq[1]--, freq[3]--;
			}
			while (freq[2] >= 2) {
				freq[2] -= 2;
				v.push_back(2);
				v.push_back(2);
			}
			while (freq[1] >= 2 && freq[2]) {
				v.push_back(1);
				v.push_back(1);
				v.push_back(2);
				freq[1] -= 2, freq[2]--;
			}
			while (freq[1] >= 4) {
				v.push_back(1);
				v.push_back(1);
				v.push_back(1);
				v.push_back(1);
				freq[1] -= 4;
			}
		}
		static int tc = 1;
		for (int i = 0; i < 4; i++) {
			while (freq[i]) {
				v.push_back(i);
				freq[i]--;
			}
		}
		int sum = 0;
		for (int i = 0; i < v.size(); i++) {
			if (!sum) ans++;
			sum += v[i];
			sum %= p;
		}
		printf("Case #%d: %d\n", tc++, ans);
	}

	return 0;
}

