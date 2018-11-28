#include <stdio.h>
#include <queue>

FILE* in=fopen("C-large.in","r");
FILE* out=fopen("C-large.out","w");

struct INTERVAL
{
	long long w,num;
	
	bool operator<(const INTERVAL& I) const
	{
		return w<I.w;
	}
	
	INTERVAL(long long _w=0,long long _num=0)
	{
		w=_w;
		num=_num;
	}
};

void solve()
{
	std::priority_queue<INTERVAL> Q;
	long long n,k,w;
	fscanf(in,"%lld %lld",&n,&k);
	Q.push(INTERVAL(n,1));
	while(1)
	{
		w=Q.top().w;
		n=0;
		
		while(!Q.empty() && (Q.top().w==w))
		{
			n+=Q.top().num;
			Q.pop();
		}
		
		if(n>=k)
		{
			fprintf(out,"%lld %lld\n",w/2,(w-1)/2);
			return;
		}
		k-=n;
		
		Q.push(INTERVAL(w/2,n));
		Q.push(INTERVAL((w-1)/2,n));
	}
}

int main()
{
	int i,T;
	fscanf(in,"%d",&T);
	for(i=1;i<=T;i++)
	{
		fprintf(out,"Case #%d: ",i);
		solve();
	}
}
