#include<bits/stdc++.h>
using namespace std;
int main() {
	freopen("input.txt", "r", stdin);
	freopen("output.txt", "w", stdout);
	int T;
	scanf("%d", &T);
	for (int t = 1; t <= T; t++) {
		string s;
		cin >> s;
		int size = s.size();
		string ans = s;
		for (int i = 1; i < size; i++) {
			if (s[i] < s[i - 1]) {
				int j = i - 1;
				while(j - 1 >= 0 && s[j] == s[j - 1]) {
					--j;
				}
				--ans[j];
				for (int k = j + 1; k < size; k++) {
					ans[k] = '9';
				}
				break;
			}
		}
		if (ans[0] == '0') {
			ans.erase(ans.begin() + 0);
			ans[0] = '9';
		}

		printf("Case #%d: %s\n", t, ans.c_str());
	}
	return 0;
}
// 11111111000000000000
