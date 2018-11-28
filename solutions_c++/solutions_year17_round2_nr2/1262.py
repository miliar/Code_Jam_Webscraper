#include<iostream>
#include<cstring>
#include<cstdio>
#include<algorithm> 
using namespace std;

double k,nowspeed,lasttime;
long long n,cas;

struct nmb
{
	long long pos;
	double sp;
}a[10010];

bool cmp(nmb a,nmb b)
{
	return a.pos>b.pos;
}

int main()
{
	//freopen("in.txt","r",)
	freopen("asd.txt","w",stdout);
	int T;
	cin>>T;
	while(T--)
	{
		memset(a,0.0,sizeof(a));
		nowspeed=lasttime=0;
		cin>>k>>n;
		for(int i=1;i<=n;i++)
			scanf("%lld%lf",&a[i].pos,&a[i].sp);
		n++;
		a[n].pos=0;
		a[n].sp=1e17;
		sort(a+1,a+n+1,cmp);
		nowspeed=a[1].sp;
		lasttime=(k-a[1].pos)/nowspeed;
		for(int i=2;i<=n;i++)
		{
			nowspeed=min(a[i].sp,(double)(k-a[i].pos)/lasttime);
			lasttime=(double)(k-a[i].pos)/nowspeed;
		} 
		printf("Case #%d: %.6lf\n",++cas,nowspeed);
	}
	return 0;
} 
