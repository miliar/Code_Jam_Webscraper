#include <bits/stdc++.h>
using namespace std;

int main(int argc, char const *argv[])
{
	int test,case_no = 1;
	scanf("%d", &test);
	while(test--) {
		int ans = 0;
		string s;
		cin >> s;
		int k;
		cin >> k;
		bool flag = 1;
		int ls = s.size();
		for(int i = 0;i < ls; i++) {
			if (s[i] == '-') {
				if (i+k <= ls) {
					for(int j=i;j<i+k;j++) {
						s[j] == '+' ? s[j] = '-' : s[j] = '+';
					}
					ans++;
				}
				else {
					flag = 0;
					break;
				}
			}
		}
		if (flag)
			printf("Case #%d: %d\n", case_no++, ans);
		else
			printf("Case #%d: IMPOSSIBLE\n", case_no++);
	}
	return 0;
}