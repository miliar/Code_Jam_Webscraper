#include <stdio.h>
#include <string.h>

FILE* in=fopen("B-large.in","r");
FILE* out=fopen("B-large.out","w");

char A[20];

void solve()
{
	int l,n,i,j,k;
	fscanf(in,"%s",A);
	l=strlen(A);
	for(i=0;i<l-1;i++)
		if(A[i]>A[i+1]) break;
	if(i==l-1)
	{
		fputs(A,out);
		return;
	}
	for(j=i+1;j<l;j++) A[j]='9';
	for(j=i;j && A[j-1]==A[i];j--);
	A[j]--;
	k=j;
	while(++j<=i) A[j]='9';
	fputs(A[k]=='0'?A+1:A,out);
}

int main()
{
	int i,T;
	fscanf(in,"%d",&T);
	for(i=1;i<=T;i++)
	{
		fprintf(out,"Case #%d: ",i);
		solve();
		fputs("\n",out);
	}
}
