#include <bits/stdc++.h>
using namespace std;
int main() {
	freopen("A-large.in","r",stdin);
	freopen("ou.txt","w",stdout);

	int t;
	cin >> t;
	for (int T = 1; T <= t; T++) {
		string s;
		int k;
		cin >> s >> k;
		int ans = 0;
		for (int i = 0; i < s.size(); i++)
			if (s[i] == '-') {
				ans++;
				for (int j = i, cnt = 0; i + k - 1 < s.size() && cnt < k;
						j++, cnt++)
					s[j] = (s[j] == '-') ? '+' : '-';
			}
		bool flag = false;
		printf("Case #%d: ", T);

		for (int i = 0; i < s.size(); i++)
			if (s[i] == '-')
				flag = true;
		if (flag)
			printf("IMPOSSIBLE\n");
		else
			printf("%d\n", ans);
	}
}
