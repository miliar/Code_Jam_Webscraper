#include <bits/stdc++.h>
using namespace std;
char str[1010]; 
bool flag[1010];
int k = 0;
int main() {
	freopen("A-large.in","r",stdin);
	freopen("A-large.out","w",stdout);
	int T = 0;
	scanf("%d",&T);
	for(int t = 1;t <= T;++ t) {
		scanf("%s %d",str,&k);
		int len = strlen(str);
		for(int i = 0;i < len;++ i) {
			if(str[i] == '+') flag[i] = 1;
			else flag[i] = 0;
		}
		int ans = 0;
		for(int i = 0;i < len-k+1;++ i) {
			if(!flag[i]) {
				ans ++;
				for(int j = 0;j < k;++ j) {
					flag[i+j] = !flag[i+j]; 
				}
			}
		}
		int cnt = 0;
		for(int i = 0;i < len;++ i) cnt += flag[i];
		if(cnt == len) printf("Case #%d: %d\n",t,ans);
		else printf("Case #%d: IMPOSSIBLE\n",t);
	}
	return 0;
} 
