#include<bits/stdc++.h>
using namespace std;

typedef long long LL;
char sc[50];
int st[50],snum;
void solve(int cas)
{
	LL v,res;
	scanf("%s",sc);
	int len=strlen(sc);
	bool need=false;
	snum=0;
	for(int i=0;i<len;++i)
	{
		if(snum==0||st[snum-1]<=sc[i]-'0')st[snum++]=sc[i]-'0';
		else
		{
			st[snum++]=sc[i]-'0';
			need=true;
			break;
		}
	}
	while(need&&st[0]!=0&&snum>1)
	{
		int a=st[--snum];
		int b=st[--snum];
		--b;
		//cout <<a<<" "<<b<<endl;
		if(snum==0||b>=st[snum-1])
		{
			st[snum++]=b;
			break;
		}
		else
			st[snum++]=b;
	}
	printf("Case #%d: ",cas);
	if(st[0]==0)	
	{
		for(int i=0;i<len-1;++i)printf("9");
		puts("");
	}
	else
	{
		for(int i=0;i<snum;++i)printf("%c",st[i]+'0');
		for(int i=snum;i<len;++i)printf("9");
		puts("");
	}
}
int main()
{
	int T;
	scanf("%d",&T);
	for(int cas=1;cas<=T;++cas)
		solve(cas);
	return 0;
}
