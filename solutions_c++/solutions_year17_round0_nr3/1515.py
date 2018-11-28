#include <bits/stdc++.h>
using namespace std;

typedef long long LL;

LL getlen()
{
	LL n,k;
	scanf("%lld%lld",&n,&k);
	LL a=n,b=n,ca=1,cb=0;
	for (;;)
	{
		a--;b--;
		LL t1=a/2,t2=a-t1,t3=b/2,t4=b-t3,ta,tb,tca=0,tcb=0;
		k-=ca;
		if (k<=0) return a;
		k-=cb;
		if (k<=0) return b;
		ta=max(t1,max(t2,max(t3,t4)));
		tb=min(t1,min(t2,min(t3,t4)));
		if (ta==tb)
		{
			a=b=ta=tb;
			ca=2*(ca+cb);
			cb=0;
		}
		else
		{
			if (t1==ta)
				tca+=ca;
			else
				tcb+=ca;
			if (t2==ta)
				tca+=ca;
			else
				tcb+=ca;
			if (t3==ta)
				tca+=cb;
			else
				tcb+=cb;
			if (t4==ta)
				tca+=cb;
			else
				tcb+=cb;
			a=ta;
			ca=tca;
			b=tb;
			cb=tcb;
		}
	}
}

void solve()
{
	LL l=getlen();
	LL k1=l/2,k2=l-k1;
	printf("%lld %lld\n",k2,k1);
}

int main()
{
	freopen("read.txt","r",stdin);
	freopen("write.txt","w",stdout);
	int T;
	scanf("%d",&T);
	for (int i=1;i<=T;i++)
	{
		printf("Case #%d: ",i);
		solve();
	}
	return 0;
}
