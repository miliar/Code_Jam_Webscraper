#include<stdio.h>
int main()
{
	int t,num,i,k,count,test,A[10000];
	scanf("%d",&t);
	for (int o=1;o<=t;o++)
	{
		
		scanf("%d",&num);
		while(num>0)
		{
		i=0;
		count=0;
		test=num;
		while(test>0)
		{
			A[i]=test%10;
			test=test/10;
			i++;
		}
		for(k=i-1;k>=1;k--)
		{
			if(A[k]<=A[k-1])	
			{
				count++;
			}
		}
		if(i-1==count)
		{
			printf("case #%d: %d\n",o,num);
			break;
		}
		else
		{
			num--;
		}
	}
	}
}
