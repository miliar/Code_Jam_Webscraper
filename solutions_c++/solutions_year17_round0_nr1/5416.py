#include<cstdio>
#include<cstring>
#include<cmath>
#include<algorithm>
#define repp(a,b,c,d) for(int a=b; a<=c; a+=d)
#define rep(a,b,c) repp(a,b,c,1)
#define revv(a,b,c,d) for(int a=b; a>=c; a-=d)
#define rev(a,b,c) revv(a,b,c,1)
typedef long long ll;

bool flag;
char dat[1005];
int main()
{
	int t,k;
	scanf("%d",&t);
	rep(tc,1,t)
	{
		scanf("%s %d",dat,&k);
		int lg=strlen(dat)-1,cnt=0;
		flag=true;
		rep(i,0,lg-k+1)
		{
			if(dat[i]=='+')continue;
			cnt++;
			dat[i]='+';
			rep(j,i+1,i+k-1)
			{
				if(dat[j]=='+') dat[j]='-';
				else dat[j]='+';
			}
		}
		rep(i,lg-k+2,lg)
		{
			if(dat[i]=='+')continue;
			flag=false;
			break;
		}
		if(flag==true) printf("Case #%d: %d\n",tc,cnt);
		else printf("Case #%d: IMPOSSIBLE\n",tc);
	}
	return 0;
}
