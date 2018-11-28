#include <iostream>
#include <cstring>
#include <cstdio>
#include <algorithm>

using namespace std;

char s[111];
int p[111];
int len;
int ans[111];
int cnt[111];

void solve()
{
	bool flag=true;
	int i,j,the,tmp;
	len=strlen(s);
	for(i=0;i<len;i++)
		p[i]=s[i]-'0';
	memset(cnt,0,sizeof(cnt));
	for(i=1;i<len;i++)
		if(p[i]<p[i-1])
		{
			the=i;
			flag=false;
			break;
		}
	if(flag)
	{
		printf("%s\n",s);
		return ;
	}
	else
	{
		tmp=the;
		tmp--;
		while(tmp>0 && p[tmp]==p[tmp-1])
			tmp--;
		p[tmp]--;
		for(i=tmp+1;i<len;i++)
			p[i]=9;
	}
	tmp=0;
	while(p[tmp]==0)
		tmp++;
	for(i=tmp;i<len;i++)
		printf("%d",p[i]);
	printf("\n");
}

int main()
{
	int T,cas=0;
	freopen("B-large.in","r",stdin); 
	freopen("B-large.out","w",stdout);
	cin>>T;
	while(T--)
	{
		scanf("%s",&s);
		printf("Case #%d: ",++cas);
		solve();
	}
	fclose(stdin);
	fclose(stdout);
	return 0;
}
