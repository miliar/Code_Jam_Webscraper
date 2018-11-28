#include <iostream>
#include <cstring>
#include <cstdio>
#include <algorithm>

using namespace std;

char s[11111];
int p[11111];
int len,k;

void solve()
{
	int i,j,ans=0;
	len=strlen(s);
	for(i=0;i<len;i++)
		if(s[i]=='+')
			p[i]=0;
		else
			p[i]=1;
	for(i=0;i+(k-1)<len;i++)
		if(p[i]==1)
		{
			for(j=0;j<k;j++)
				p[i+j]=1-p[i+j];
			ans++;
		}
	for(;i<len;i++)
		if(p[i]==1)
		{
			printf("IMPOSSIBLE\n");
			return ;
		}
	printf("%d\n",ans);
}

int main()
{
	freopen("A-large.in","r",stdin); 
	freopen("A-large.out","w",stdout);
	int T,i,j,cas=0;
	cin>>T;
	while(T--)
	{
		scanf("%s%d",s,&k);
		printf("Case #%d: ",++cas);
		solve();
	}
	fclose(stdin);
	fclose(stdout);
	return 0;
}
