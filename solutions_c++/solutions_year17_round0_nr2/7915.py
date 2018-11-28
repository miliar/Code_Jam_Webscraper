#include <bits/stdc++.h>
using namespace std;
long long int fun(int i)
{
	long long int pro = 1;
	for(int j=0;j<i;j++)
	{
		pro = pro*10;
	}
	return pro;
}
int main()
{
	long long int t,n,x=1,sum;
	int digit;
	int arr[20];
	scanf("%lld",&t);
	while(t--)
	{
		digit=0;
		sum=0;
		scanf("%lld",&n);
		int i=0;
		int j=0;
		while(n)
		{
			arr[i] = n%10;
			n/=10;
			digit++;
			i++;
		}
		/*for(i=0;i<digit;i++)
		{
			printf("%d ",arr[i] );
		}*/
		for(i=1;i<digit;i++)
		{
			if(arr[i]>arr[i-1])
			{
				for(j=i-1;j>=0;j--)
				{
					arr[j]=9;
				}
				arr[i] = arr[i] - 1;
			}
		}
	
		for(i=0;i<digit;i++)
		{
			sum = sum + (arr[i])*fun(i);
			//printf("%lld %d %d\n",sum,arr[i]);

		}
		printf("Case #%lld: %lld\n",x,sum);
		x++;


	}
}