#include<stdio.h>

int main()
{
//	freopen("2_large.in","r",stdin);
//	freopen("2_largeout.txt","w",stdout);
	int t;
	scanf("%d",&t);
	for(int l=1;l<=t;l++)
	{
		long long int n,i,k,h;
		scanf("%lld",&n);
		
		while(n>0)
		{
			i=n;
			bool f=true;
			int p=i%10,d=1;
			i=i/10;
			k=p;
			while(i>0)
			{
				if(i%10<=p)
				{
					p=i%10;
					i=i/10;
					h=p;
					for(int o=1;o<=d;o++)
						{
							h=h*10;
						}
					k=k+h;
					d++;
				}
				else
				{
					if(k==0)
					{
						n--;
					}
					else
					{
						n=n-k;
					}
					f=false;
					break;
				}
			}
			if(f)
			{
				break;
			}
		}
		printf("Case #%d: ",l);
		printf("%lld\n",n);
	}
}
