#include <stdio.h>
#include <algorithm>
#define PI 3.141592653589793238462643383279

FILE* in=fopen("A-large.in","r");
FILE* out=fopen("A-large.out","w");

struct CAKE
{
	long long r,h,area;
	bool operator<(const CAKE& C) const
	{
		return area>C.area;
	}
	void get()
	{
		fscanf(in,"%lld %lld",&r,&h);
		area=r*h;
	}
}cake[1000];

void solve()
{
	int n,k,i;
	fscanf(in,"%d %d",&n,&k);
	for(i=0;i<n;i++)
		cake[i].get();
	std::sort(cake,cake+n);
	long long S=0,R=0,t;
	
	for(i=0;i<k-1;i++)
	{
		S+=cake[i].area;
		if(R<cake[i].r) R=cake[i].r;
	}
	long long max=0;
	for(;i<n;i++)
	{
		t=R>cake[i].r?R:cake[i].r;
		t=2*(S+cake[i].area)+t*t;
		if(max<t) max=t;
	}
	fprintf(out,"%lf\n",PI*max);
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
