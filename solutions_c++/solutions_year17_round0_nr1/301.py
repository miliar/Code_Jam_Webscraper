#include <bits/stdc++.h>


#define puba push_back
#define ff first
#define ss second
#define pii pair <int, int>


using namespace std;


typedef long long LL;

char rev(char c) {
	if (c == '-') return '+';
	return '-';
}

const int MAXN = 1010;

char str[MAXN];

int main() {
	int t;
	cin >> t;
	for (int q = 1; q <= t; ++q) {
		cout << "Case #" << q << ": ";
		
		int k;
		string s;
		cin >> s >> k;
		int n = s.size();
		memset(str, 0, sizeof(str));
		for (int i = 0; i < n; ++i) {
			str[i] = s[i];
		}

		int ans = 0;
		for (int i = 0; i + k <= n; ++i) {
			if (str[i] == '-') {
				++ans;
				for (int j = 0; j < k; ++j) {
					str[i + j] = rev(str[i + j]);
				}
			}
		}

		bool flag = false;
		for (int i = 0; i < n; ++i) {
			if (str[i] == '-') {
				flag = true;
				break;
			}
		}

		if (flag) {
			cout << "IMPOSSIBLE";
		}
		else {
			cout << ans;
		}
		cout << endl;
	}
	return 0;
}