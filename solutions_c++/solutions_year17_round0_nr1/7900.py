#include <bits/stdc++.h>
using namespace std;

int main()
{
	int i,j,t,k,cnt;
	int x=1;
	char arr[1000005];
	scanf("%d",&t);
	while(t--)
	{
		cnt=0;
		scanf("%s",&arr);
		scanf("%d",&k);
		int len = strlen(arr);
		int flag=1;

		for(i=0;i<=len-k;i++)
		{
			if(arr[i]=='-')
			{
				for (j = i; j < i+k; j++)
				{
					if(arr[j]=='-')
					{	
						arr[j]='+';
					}
					else
					{
						arr[j]='-';
					}
					
				}
				cnt++;
			}
		}
		for(i=len-k+1;i<len;i++)
		{
			if(arr[i]=='-')
			{
				flag=0;
				break;
			}
		}
		if(!flag)
			printf("Case #%d: IMPOSSIBLE\n",x);
		else
			printf("Case #%d: %d\n",x,cnt );
		x++;
	}
}