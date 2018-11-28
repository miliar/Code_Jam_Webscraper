#include<iostream>
#include<cstdio>
#include<fstream>
using namespace std;
int main(void)
{
		freopen("B-small-attempt2.in","r",stdin);
		freopen("myfile.out","a",stdout);
	int t,s;
	scanf("%d",&t);
	s=t;
	while(t--)
	{
		long long int n,x,sum,prod;
		scanf("%lld",&n);
		int dig=0,flag=0,prev=n%10,dig1=-1;
		x=n/10;
		dig++;
		while(x>0)
		{
			if(x%10>prev)
			dig1=dig;
			else if(dig1!=-1)
			{
				if(x%10==prev)
				dig1=dig;
			}
			prev=x%10;
			dig++;
			x/=10;
		}
				if(dig1==-1)
				sum=n;
				else
				{
					prod=1;
					for(int i=0;i<dig1;i++)
					prod*=10;
					sum=n/prod;
					sum*=prod;
					sum--;
				}
		
	    printf("Case #%d: %lld\n",s-t,sum);
	}
	return 0;
}
