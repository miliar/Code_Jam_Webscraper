#include <iostream>
#include <stdio.h>
#include <stdlib.h>

using namespace std;

int main()
{
	int *arr;
	int t,n,per;
	scanf("%d",&t);
	for(int i=0;i<t;i++)
	{
		scanf("%d%d",&n,&per);
		arr=(int*)malloc((n+2)*sizeof(int));
		for(int j=1;j<=n;j++)
			arr[j]=0;
		int count_max,count,initial_max,initial,final_max,final;

		arr[0]=1;
		arr[n+1]=1;
		for(int j=0;j<per;j++)
		{
			count_max=0;
			count=0;
			initial_max=0;
			initial=0;
			final_max=0;
			final=0;
			for(int k=n;k>=1;k--)
			{
				if(arr[k]==1)
					continue;
				initial=k;
				count=0;
				while(arr[k]!=1)
				{
					count++;
					k--;
				}
				final=k;
				if(count>count_max)
				{
					count_max=count;
					initial_max=initial;
					final_max=final;
				}
			}
			arr[(initial_max+final_max+1)/2]=1;
		}
		int l=((initial_max+final_max+1)/2)-final_max-1;
		int r=initial_max-((initial_max+final_max+1)/2);
		//printf("%d %d %d %d",l,r,initial_max,final_max);
		printf("Case #%d: %d %d\n",i+1,(l>r?l:r),(l<r?l:r));
	}
}