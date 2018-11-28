#include <bits/stdc++.h>
using namespace std;

#define fo(i,s,t) for(int i = s; i <= t; ++ i)

int t, k, ans, n;
char str[1005];

int main()
{
	// freopen("1.in","r",stdin);
	// freopen("1.out","w",stdout);
	scanf("%d",&t);
	fo(qwq,1,t)
	{
		printf("Case #%d: ",qwq);
		scanf("%s",str+1);
		scanf("%d",&k);
		ans = 0; n = strlen(str+1);
		fo(i,1,n) if(str[i]=='-' && i+k-1<=n)
		{
			fo(j,i,i+k-1) if(str[j] == '-') str[j] = '+'; else str[j] = '-';
			++ ans;
		}
		fo(i,1,n) if(str[i]=='-') ans = -1;
		if(ans!=-1) printf("%d\n",ans);
		else printf("IMPOSSIBLE\n");
	}
	return 0;
}