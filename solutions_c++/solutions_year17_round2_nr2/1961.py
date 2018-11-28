#include <stdio.h>
#include <iostream>
using namespace std;
int main()
{
	freopen("B-small-attempt3.in","r",stdin);
	freopen("meSB.out","w",stdout);
	int T;
	cin>>T;
	int a[10];

	for(int s=1;s<=T;s++)
	{
		
		for(int i=0;i<7;i++)
		
		
		cin>>a[i];
	
	
		printf("Case #%d: ",s);
		if(a[1]>a[3]+a[5]||a[3]>a[1]+a[5]||a[5]>a[1]+a[3])
		{
			printf("IMPOSSIBLE\n");
			continue;
		}
		int max=0;
		int now;
		for(int i=1;i<=5;i=i+2)
		{
			if(max<a[i])
			{
				max=a[i];
				now=i;
			}
		} 
		int end=a[1]+a[3]+a[5];
		int count=1;
		while(end)
		{
		
			if(now==1)
			{
				if(a[1]<=a[3]||a[1]<=a[5])count=0;
				if(a[1])
				{
					printf("R");
					a[1]--;
					end--;
				}
				if(a[3])
				{
					printf("Y");
					a[3]--;
					end--;
				}
				if(a[1]&&count)
				{
					printf("R");
					a[1]--;
					end--;
				}
				if(a[5])
				{
					printf("B");
					a[5]--;
					end--;
				}	
				//if(a[1]<=a[3]||a[1]<=a[5])count=0; 
			}
			if(now==3)
			{
				if(a[3]<=a[1]||a[3]<=a[5])count=0; 
				if(a[3])
				{
					printf("Y");
					a[3]--;
					end--;
				}
				if(a[1])
				{
					printf("R");
					a[1]--;
					end--;
				}
				if(a[3]&&count)
				{
					printf("Y");
					a[3]--;
					end--;
				}
				if(a[5])
				{
					printf("B");
					a[5]--;
					end--;
				}	
				//if(a[3]<=a[1]||a[3]<=a[5])count=0; 
			}
			if(now==5)
			{
				
				if(a[5]<=a[1]||a[5]<=a[3])count=0;
				if(a[5])
				{
					printf("B");
					a[5]--;
					end--;
				}	
				if(a[3])
				{
					printf("Y");
					a[3]--;
					end--;
				}
				if(a[5]&&count)
				{
					printf("B");
					a[5]--;
					end--;
				}	
				if(a[1])
				{
					printf("R");
					a[1]--;
					end--;
				}
				//if(a[5]<=a[1]||a[5]<=a[3])count=0; 
			}
		}
		printf("\n");
	}
}
