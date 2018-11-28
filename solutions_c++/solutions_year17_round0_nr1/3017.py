#include <cstdlib>
#include <cstdio>
#include <iostream>
#include <cstring>
#include <string>

using namespace std;

int main() {
	freopen("a.in", "r", stdin);
	freopen("a.out", "w", stdout);
	
	int T;
	char s[1005];
	
	scanf("%d", &T);
	gets(s);
	for (int times = 1; times <= T; ++times) {
		printf("Case #%d: ", times);
		gets(s);
		
		int l = strlen(s);
		int k = 0;
		for (int i = 0; i < l; ++i) {
			if (s[i] == ' ') {
				for (int j = i + 1; j < l && s[j] >= '0' && s[j] <= '9'; ++j) {
					k = k * 10 + (s[j] - '0'); 
				}
				s[i] = '\0';
				break;
			}
		}

		bool f[k + 5];		
		memset(f, false, sizeof(f));
		int p = 0, ans = 0;
		bool t = false;
		l = strlen(s);
		for (int i = 0; i + k <= l; ++i) {
			if (f[p]) t = !t;			
			if ((s[i] == '+' && t == false) || (s[i] == '-' && t == true)) {
				f[p] = false;
			} else {
				t = !t;
				f[p] = true;
				ans += 1;
			}
			p = (p + 1) % k;
		}
		
		bool res = true;
		for (int i = l - k + 1; i < l; ++i) {
			if (f[p]) t = !t;
			if ((s[i] == '+' && t == false) || (s[i] == '-' && t == true)) {
				f[p] = false;
				p = (p + 1) % k;
			} else {
				res = false;
				break;
			}
		}
		if (res) {
			printf("%d\n", ans);
		} else {
			printf("IMPOSSIBLE\n");
		}
	}
	
	return 0;
}
