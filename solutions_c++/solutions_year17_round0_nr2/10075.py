#include <iostream>
#include <stdio.h>
using namespace std;

int main()
{
	int t,n;
	scanf("%d",&t);
	for(int j=1;j<=t;j++)
	{
		scanf("%d",&n);
		if(n<10)
		{
			printf("Case #%d: %d\n",j,n);
			continue;
		}
		for (int i=n;i>=0;i--)
		{
			int flag=0;
			int rem1=0,rem2=0,div=i;
			while(div>9)
			{
				flag=0;
				rem1=div%10;
				rem2=(div%100)/10;
				if(rem1<rem2)
				{
					flag=1;
					break;
				}
				div=div/10;
			}
			if(flag==0)
			{
				printf("Case #%d: %d\n",j,i);
				break;
			}
		}
	}
	return 0;
}