#include <iostream>
#include <cstdio>

using namespace std;

typedef long long LL;

LL n,maxans,minans,K;
int T,cnt;

void calc()
{
	for (LL len=n,tot=0,cnt1=0,cnt2=1;;)
	{
		tot+=cnt2;
		if (K<=tot)
		{
			minans=len-1>>1,maxans=len-1-minans;
			break;
		}
		tot+=cnt1;
		if (K<=tot)
		{
			minans=len-2>>1,maxans=len-2-minans;
			break;
		}
		if (len&1) cnt2=cnt2*2+cnt1,len=len-1>>1;
		else cnt1=cnt1*2+cnt2,len=len>>1;
	}
}

int main()
{
	freopen("bathroom.in","r",stdin),freopen("bathroom.out","w",stdout);
	for (scanf("%d",&T);T--;)
	{
		scanf("%lld%lld",&n,&K);
		calc();
		printf("Case #%d: %lld %lld\n",++cnt,maxans,minans);
	}
	fclose(stdin),fclose(stdout);
	return 0;
}