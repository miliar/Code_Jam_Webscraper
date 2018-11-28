#include <stdio.h>
#include <iostream>
using namespace std;
char str[1005];
int main()
{
	int T,n,r,o,y,b,g,v,i;
	int max,maxi,c1,c2,c3,c;
	cin>>T;

	
	int test=1;
	while(T--)
	{
		for(i=0;i<=1000;i++)
		{
			str[i]='X';
		}

		cin>>n;
		
		cin>>r>>o>>y>>g>>b>>v;
			
		
		max=r;
		maxi=1;
		if(b>r)
		{
			max=b;
			maxi=2;
		}
		if(y>max)
		{
			max=y;
			maxi=3;
		}
		if(maxi==1)
		{
			if(max>y+b)
			{
				printf("Case #%d: IMPOSSIBLE\n",test);
				test++;
				continue;
			}
			c1=0;
			c2=0;
			c3=0;
			for(i=0;i<n;i++)
			{
				if(i%2==0 && c1!=r)
				{
					str[i]='R';
					c1++;
				}
			}
			
			
				c=0;
				for(i=0;i<n;i++)
				{
				
					if(str[i]=='X'&&((b-c2)>=(y-c3))&&str[i-1]!='B')
					{
					str[i]='B';
					c++;
					c2++;
					}
					else if(str[i]=='X') 
					{
					str[i]='Y';
					c++;
					c3++;
					}
				}
				

		}
		if(maxi==2)
		{
			if(max>y+r)
			{
				printf("Case #%d: IMPOSSIBLE\n",test);
				test++;
				continue;
			}
			c1=0;
			c2=0;
			c3=0;
			for(i=0;i<n;i++)
			{
				if(i%2==0 && c2!=b)
				{
					str[i]='B';
					c2++;
				}
			}
			
			
				c=0;
				for(i=0;i<n;i++)
				{
				
					if(str[i]=='X'&&((r-c1)>=(y-c3))&&str[i-1]!='R')
					{
					str[i]='R';
					c++;
					c1++;
					}
					else if(str[i]=='X') 
					{
					str[i]='Y';
					c++;
					c3++;
					}
				}
			
		}
		if(maxi==3)
		{
			if(max>r+b)
			{
				printf("Case #%d: IMPOSSIBLE\n",test);
				test++;
				continue;
			}
			c1=0;
			c2=0;
			c3=0;
			for(i=0;i<n;i++)
			{
				if(i%2==0 && c3!=y)
				{
					str[i]='Y';
					c3++;
				}
			}
			
				c=0;
				for(i=0;i<n;i++)
				{
				
					if(str[i]=='X'&&((r-c1)>=(b-c2))&&str[i-1]!='R')
					{
					str[i]='R';
					c++;
					c1++;
					}
					else if(str[i]=='X') 
					{
					str[i]='B';
					c++;
					c2++;
					}
				}
				

			
		}

		printf("Case #%d: ",test);
		for(i=0;i<n;i++)
		{
			printf("%c",str[i]);
		}
		printf("\n");
		test++;
		
	}
	return 0;
}