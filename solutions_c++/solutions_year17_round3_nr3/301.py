#include <stdio.h>

FILE* in = fopen("C-small-1-attempt2.in","r");
FILE* out = fopen("C-small-1-attempt2.out","w");

double p[50],u;
int n;

int ok(double k)
{
	double use=0;
	int i;
	for(i=0;i<n;i++) if(p[i]<k)
	{
		use+=k-p[i];
		if(use>u) return 0;
	}
	return 1;
}

void solve()
{
	int i,k;
	fscanf(in,"%d %d %lf",&n,&k,&u);
	for(i=0;i<n;i++) fscanf(in,"%lf",p+i);
	double m=0,M=1,h;
	while(M-m>0.000000001)
	{
		h=(m+M)/2;
		if(ok(h)) m=h;
		else M=h;
	}
	double ans=1;
	for(i=0;i<n;i++)
	{
		ans*=(p[i]>h?p[i]:h);
	}
	fprintf(out,"%.9lf\n",ans);
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
