#include <bits/stdc++.h>
using namespace std;
char s[2000];
int k;
int main(){
	freopen("A.in","r",stdin);
	freopen("A.out","w",stdout);
	int ca = 0;
	int T;
	scanf("%d",&T);
	while(T--){
		scanf("%s",s);
		scanf("%d",&k);
		int n = strlen(s);
		int ans = 0;
		for (int i = 0;i < n - k + 1;i ++)
			if (s[i]=='-'){
				ans ++;
				for (int j = 0;j < k;j ++)
					if (s[i+j]=='-')s[i+j]='+';
					else s[i+j]='-';
			}
		int flag = 0;
		for (int i = 0;i < n;i ++)
			if (s[i]=='-') flag = 1;
		printf("Case #%d: ",++ca );
		if (flag)
			puts("IMPOSSIBLE");
		else printf("%d\n",ans );
	}
	return 0;
}