#include<cstdio>
#include<cstring>
#include<algorithm>
const int MAXN=10+5;
char cake[MAXN];int ans,k,t,n;
void search(int now,int flip)
{
//	printf("SEC: %d %d\n",now,flip);
	for(int i=1;i<=n;i++)
	{
		if(cake[i]=='-') goto skip;
//		printf("%c",cake[i]);
	}	
	ans=std::min(flip,ans);
//	printf("FOUND=%d\n",ans);
skip:
	if(now==n+1) return;
	search(now+1,flip);
	if(now+k-1<=n)
	{
		for(int i=now;i<=now+k-1;i++)
			cake[i]=(cake[i]=='-'?'+':'-');
		search(now+1,flip+1);
		for(int i=now;i<=now+k-1;i++)
			cake[i]=(cake[i]=='-'?'+':'-');
	}
}
int main()
{
	freopen("o.txt","w",stdout);
	scanf("%d",&t);
	for(int CASE=1;CASE<=t;CASE++)
	{
		scanf("%s",cake+1);
		scanf("%d",&k);
		n=strlen(cake+1);
		ans=2147483647;
		search(1,0);
		if(ans!=2147483647) printf("Case #%d: %d\n",CASE,ans); else printf("Case #%d: IMPOSSIBLE\n",CASE);
	}
}
