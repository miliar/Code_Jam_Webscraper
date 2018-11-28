#include<iostream>
#include<cstring>
#include<cmath>
#include<cstdlib>
#include<cstdio>
#include<string>
#include<algorithm>
#include<vector>
using namespace std;
char s[1010];
int d[1010];
int f[1010];
int main() {
	//freopen("a.in","r",stdin);
	//freopen("a.out","w",stdout);
	int n, k;
	scanf("%d", &n);
	for (int cs = 1; cs <= n; cs++) {
		memset(f, 0, sizeof(f));
		scanf("%s%d", s,&k);
		int len = strlen(s);
		for (int i = 0; i < len; i++) {
			if (s[i] == '+') d[i] = 0;
			else d[i] = 1;
		}
		int ans = 0, sum = 0;
		for (int i = 0; i + k <= len; i++) {
			if ((d[i] + sum) & 1) {
				f[i] = 1;
				ans++;
			}
			sum += f[i];
			if (i - k + 1 >= 0) sum -= f[i - k + 1];
			//cout << f[i] << ' '<<sum<<' '<<ans << endl;
		}
		for (int i = len - k + 1; i < len; i++) {
			//cout << i << ' '<< f[i] << ' ' << sum << endl;
			if ((d[i] + sum) & 1) {
				ans = -1;
			}
			if (i - k + 1 >= 0) sum -= f[i - k + 1];

		}
		if (ans == -1)
			printf("Case #%d: IMPOSSIBLE\n", cs);
		else
			printf("Case #%d: %d\n", cs, ans);
	}
}
