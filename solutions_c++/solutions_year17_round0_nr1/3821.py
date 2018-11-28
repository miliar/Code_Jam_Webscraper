#include <iostream>
#include <cstdio>
#include <algorithm>
#include <cstring>

using namespace std;

int n,T,d,ans,len;
char str[11111];

int main(){
	freopen("1.in","r",stdin);
	freopen("1.out","w",stdout);
	scanf("%d",&n);
	for(int T=1;T<=n;++T){
		scanf(" ");
		scanf("%s%d",&str, &d);
		len = strlen(str);
		ans = 0;
		for (int i=0;i+d<=len;++i)
			if	(str[i] == '-'){
				for(int j=i;j<i+d;++j)
					str[j] = '-'+'+'-str[j];
				ans++;
			}
		for (int i=0;i<len;++i)
			if	(str[i] == '-')	ans = -1;
		printf("Case #%d: ",T);
		if	(ans < 0)	puts("IMPOSSIBLE");
		else	printf("%d\n",ans);
	}
}
