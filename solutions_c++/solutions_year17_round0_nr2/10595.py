#include<cstdio>
#include<algorithm>
#include<iostream>
using namespace std;
main()
{
	int t,c=0;
	cin >> t;
	int n,i;
	i=1;
	while(t--)
	{
		cin >>n;
		
	    //  printf("%d",n);
		while(n>=0)
		{
			int k=n,rem,prev=0;
			//if(k%10!=0)
			{
				//printf("%dcc",c);
				while(k>0)
				{
						c=0;
				
						rem=k%10;
						k=k/10;
						//printf("%dkkk",rem);
						if(rem==0)
						{
							c=1;
							break;
						}
						else if(prev==0)
						prev=rem;
						else if(rem<=prev)
						prev=rem;
						else
						{     c=1;
							break;
						}
						//printf("%d--",rem);
				
				}
				//printf("\n");
				//printf("%dcc",c);
			}
			//else
			//c=1;
			if(c==0)
			{
				printf("Case #%d: %d\n",i++,n);
					break;
			}
			else
			//printf("nope");
			//printf("%d--",n);
			n--;
			c=0;
			
			
		}
	}
}
