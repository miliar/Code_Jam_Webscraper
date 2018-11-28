#include<iostream>
#include<stdio.h>
#include<string.h>
#define s scanf
#define p printf
using namespace std;
int ar[20];
int main()
{
	freopen("B-large.in","r",stdin);
	freopen("output.in","w",stdout);
	int t,m=1;
	long long int n;
	s("%d",&t);
	while(t--)
	{
		s("%lld",&n);
		long long int i=0,a,b,j,len,flag=1;
		a=n;
		while(a!=0)
		{
			b=a%10;
			ar[i]=b;
			i++;
			a=a/10;
		}
		len=i;
		while(flag!=0)
		{
			flag=0;
		for(j=len-1;j>0;j--)
		{
			if(ar[j]>ar[j-1])
			{
				ar[j]--;
				flag=1;
				break;
			}
		}
		
	    	for(i=j-1;i>=0;i--)
		    ar[i]=9;
		
		}
		p("Case #%d: ",m);
		for(i=len-1;i>=0;i--)
		{
			if(ar[i]!=0)
			break;
		}
		for(j=i;j>=0;j--)
		p("%d",ar[j]);
		p("\n");
		m++;
	}
	return 0;
}
