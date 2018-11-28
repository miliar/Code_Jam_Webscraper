#include<bits/stdc++.h>
using namespace std;
int a[6];
char col[6] = {'R', 'O', 'Y', 'G', 'B', 'V'};
void check(string ans) {
	int n(ans.size());
	map<char, int> mp;
	for(int i(0); i < 6; i++)
		mp[col[i]] = i;
	for(int i(0); i < n; i++) {
		int a(mp[ans[i]]), b(mp[ans[(i + 1) % n]]);
		if(a % 2 == 1 || b % 2 == 1) {
			assert(abs(b - a) == 3);
		}else {
			assert(a != b);
		}
	}
}
void solve() {
	string ans;
	int n(a[0] + a[1] + a[2] + a[3] + a[4] + a[5]);
	for(int d(0); d < 6; d += 2) {
		if(a[d] == a[(3 + d) % 6] && n == a[d] + a[(3 + d) % 6]) {
			ans.resize(n);
			for(int i(0); i < n; i++)
				ans[i] = i % 2 ? col[d] : col[(d + 3) % 6];
			puts(ans.c_str());
			check(ans);
			return;
		}
	}
	if(a[3] && a[0] <= a[3] || a[5] && a[2] <= a[5] || a[1] && a[4] <= a[1]) {
		puts("IMPOSSIBLE");
		return;
	}
	a[0] -= a[3];
	a[2] -= a[5];
	a[4] -= a[1];
	n -= 2 * a[1] + 2 * a[3] + 2 * a[5];
	if(a[0] * 2 > n || a[2] * 2 > n || a[4] * 2 > n) {
		puts("IMPOSSIBLE");
		return;
	}
	ans.resize(n);
	bool flag(false);
	for(int d(0); d < 6; d += 2) {
		if(a[d] * 2 == n) {
			for(int i(0); i < n; i++) {
				if(i % 2 == 0)
					ans[i] = col[d];
				else {
					if(a[(d + 2) % 6]) {
						a[(d + 2) % 6]--;
						ans[i] = col[(d + 2) % 6];
					}else {
						a[(d + 4) % 6]--;
						ans[i] = col[(d + 4) % 6];
					}
				}
			}
			flag = true;
			break;
		}
	}
	if(!flag) {
		for(int i(0); i < n; i++) {
			int posi(n % 2 == 1 ? i * 2 % n : i < n / 2 ? i * 2 : (i - n / 2) * 2 + 1);
			for(int d(0); d < 6; d += 2) 
				if(a[d]) {
					ans[posi] = col[d];
					a[d]--;
					break;
				}
		}
	}
	for(int d(0); d < 6; d += 2) {
		if(a[(d + 3) % 6]) {
			string tmp;
			for(int i(0); i < a[(d + 3) % 6]; i++) {
				tmp.push_back(col[(d + 3) % 6]);
				tmp.push_back(col[d]);
			}
			for(int i(0); i < (int)ans.size(); i++) {
				if(ans[i] == col[d]) {
					ans = ans.substr(0, i + 1) + tmp + ans.substr(i + 1);
					break;
				}
			}
		}
	}
	for(int i(0); i < (int)ans.size(); i++) {
		assert(ans[i] != ans[(i + 1) % (int)ans.size()]);
	}
	check(ans);
	puts(ans.c_str());
}

int main() {
	int tests;
	scanf("%d", &tests);
	for(int qq(1); qq <= tests; qq++) {
		printf("Case #%d: ", qq);
		int n;
		scanf("%d", &n);
		for(int i(0); i < 6; i++)
			scanf("%d", &a[i]);
		solve();
	}
}

