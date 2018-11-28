#include<bits/stdc++.h>
using namespace std;
char st[9999];
int main() {
	int n;
	scanf("%d", &n);
	for(int i(0); i < n; i++) {
		int k;
		scanf("%s%d", st, &k);
		int len(strlen(st));
		int ans(0);
		for(int i(0); i + k - 1 < len; i++) {
			if(st[i] == '-') {
				ans++;
				for(int j(0); j < k; j++)
					st[i + j] = '+' + '-' - st[i + j];
			}
		}
		bool flag(true);
		for(int i(0); i < len; i++) {
			if(st[i] == '-') {
				flag = false;
			}
		}
		printf("Case #%d: ", i + 1);
		if(flag == false)
			printf("IMPOSSIBLE\n");
		else
			printf("%d\n", ans);
	}
}
