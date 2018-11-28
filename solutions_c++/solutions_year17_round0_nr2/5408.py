#include <stdio.h>
#include<bits/stdc++.h>using namespace std;
int main(void) {
    freopen("input3.txt","r",stdin);
    freopen("output3.txt","w",stdout);
    int test,u,i,t=0,j,temp[18],arr[18];
	unsigned long long int n,d;
	scanf("%d",&test);
	for(u=0;u<=test-1;u++)
	{
	scanf("%llu",&d);
	n=d;

	t=0;
	while(n>=10)
	{
	    temp[t++]=n%10;
	    n=n/10;
	}

	temp[t]=n;
	for(i=t;i>=0;i--)
	{
	    arr[t-i]=temp[i];
	}

label:
for(i=0;i<=t-1;i++)
{
    if(arr[i]>arr[i+1])
    {
    arr[i]=arr[i]-1;
    for(j=i+1;j<=t;j++)
    arr[j]=9;
    goto label;
    }
}

	printf("Case #%d: ",u+1);
	for(i=0;i<=t;i++)
	{
	    if(arr[i]==0)
	    continue;
	    else
	    printf("%d",arr[i]);
	}
	printf("\n");
	}
	return 0;
}

