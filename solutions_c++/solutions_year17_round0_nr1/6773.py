#include<bits/stdc++.h>
using namespace std;
char s[1005];
int mark[1005];
int main(){
	freopen("1.in","r",stdin);
	freopen("1.out","w",stdout);
	int T;
	scanf("%d\n",&T);
	for (int test = 0;test < T;test++) {
		printf("Case #%d: ",test + 1);
		int k;
		scanf("%s %d\n",s,&k);
		memset(mark,0,sizeof mark);
		int now = 0,n = strlen(s);
		int ans = 0;
		bool flag = true;
		for (int i=0;i<n;i++) {
			now += mark[i];
			int x = s[i] == '-' ? 0 : 1;
			if (now % 2 == 1) x ^= 1;
			if (i > n - k) {
				if (x != 1) {
					flag = false;
					break;
				}
			}
			if (x != 1) {
				ans++;
				mark[i+1]++;
				mark[i+k]--;
			}
		}
		if (flag == false) printf("IMPOSSIBLE\n");
		else {
			printf("%d\n",ans);
		}
	}
}
