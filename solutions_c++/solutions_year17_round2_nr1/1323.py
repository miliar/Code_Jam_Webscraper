#include <stdio.h>
#include <string.h>

FILE* in=fopen("A-large.in","r");
FILE* out=fopen("A-large.out","w");

char A[1001];

void solve()
{
	int d,n,k,s;
	double M=0,t;
	fscanf(in,"%d %d",&d,&n);
	while(n--)
	{
		fscanf(in,"%d %d",&k,&s);
		t=(double)(d-k)/s;
		if(t>M) M=t;
	}
	fprintf(out,"%lf\n",d/M);
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
