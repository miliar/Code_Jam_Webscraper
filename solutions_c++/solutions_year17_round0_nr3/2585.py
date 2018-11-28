#include<stdio.h>
#include<math.h>
int main()
{
	int t,i=0;
	long long int a,b,n,k,l,r,pos,s=0,max,min,p;
	scanf("%d",&t);
	while(t--)
	{i++;
		s=1;
		scanf("%lld%lld",&n,&k);
        b=n/2;
        a=(n-1)/2;
		l=r=s=1;
		while(s<k)
		{
			p=s;
			s=1+2*s;
			if(a%2==0&&b%2==0)
			{
				b=a/2;
				a=b-1;
				l=2*l;
				r=2*r;
			}
			else if(a%2==0)
			{
				b=a/2;
				a=b-1;
				r=2*r+l;
			}
			else if(b%2==0)
			{
				l=2*l+r;
				b=b/2;
				a=b-1;
			}
			else
			{
				l=2*l;
				r=2*r;
				a=a/2;
				b=b/2;
			}
//			printf("%d\t%d\t%d\t%d\n",l,r,a,b);
		}
		pos=k-p;
		if(b<=0)
		{
		max=0;
		min=0;}
		else if(pos<=r)
		{
		//	printf("enter %d %d %d %d\n",l,r,a,b);
			if(r>l&&r-l>=2*pos)
		     {
		     	max = b;min=b;
		     }
		     else
		     {
		     	max=b;min=a;
			 }

		}
		else if(a<0)
		{
			max=b;min=0;
		}
		else
		{
			max=min=a;
		}
		printf("case #%d: %lld %lld\n",i,max,min);
	}
	return 0;
}
