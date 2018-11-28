#include<stdio.h>

int main()
{
    int T,N,y,i,r,n,temp;
    scanf("%d",&T);
    for(i=1;i<=T;i++)
    {
	scanf("%d",&N);
	n=N;
	temp=10;
	do
	{
	    r=N%10;
	    if(r<=temp)
	    {
		temp=r;
		N=N/10;
	    }
	    else
	    {
		N=n-1;
		n=N;
		temp=10;
	    }
	}while(N>0);
	printf("case #%d: %d\n",i,n);
    }
    return 1;
}