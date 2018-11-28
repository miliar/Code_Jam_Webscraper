#include <bits/stdc++.h>
using namespace std;
typedef long long LL;
#define IOS ios_base::sync_with_stdio(0);cin.tie(0);
#define MP make_pair
#define PB push_back
#define FF first
#define SS second
int main() {
	IOS;
	int n, kase = 0;
	cin >> n;
	while (n--) {
		string s;
		int k;
		cin >> s >> k;
		int len = s.length();
		int time = 0;
		bool chk = 0;
		for (int i = 0; i < len; i++) {
			if (s[i] == '+') continue;
			else {
				if (i + k > len) {
					chk = 1;
					break;
				}
				time++;
				for (int j = 0; j < k; j++) {
					if (s[i + j] == '+') s[i + j] = '-';
					else s[i + j] = '+';
				}
			}
		}
		cout << "Case #" << ++kase << ": ";
		if (chk) cout << "IMPOSSIBLE\n";
		else cout << time << "\n";
	}
}
