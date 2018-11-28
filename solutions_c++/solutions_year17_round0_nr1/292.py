#include <stdio.h>
#include <string.h>

FILE* in=fopen("A-large.in","r");
FILE* out=fopen("A-large.out","w");

char A[1001];

void solve()
{
	int l,n,i,j,cnt=0;
	fscanf(in,"%s %d",A,&n);
	l=strlen(A);
	for(i=0;i<=l-n;i++) if(A[i]=='-')
	{
		cnt++;
		for(j=0;j<n;j++)
			A[i+j]=88-A[i+j];
	}
	for(;i<l;i++) if(A[i]=='-')
	{
		fprintf(out,"IMPOSSIBLE\n");
		return;
	}
	fprintf(out,"%d\n",cnt);
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
