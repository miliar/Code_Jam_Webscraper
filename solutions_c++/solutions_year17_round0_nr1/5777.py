#include<bits/stdc++.h>
using namespace std;


int main()
{
	int t, k, ca=1;
	char str[10000];
	
	scanf("%d", &t);
	
	while(t--)
	{
		scanf("%s %d", str, &k);
			
		int i=0, j=0, res=0, n=strlen(str);
		
		printf("Case #%d: ", ca);
		ca += 1;
		
		while(i!=n)
		{
			if(str[i]=='-')
			{
				if(i+k-1>=n)break;
				
				res += 1;
				for(j=i;j<i+k;++j)
				{
					if(str[j]=='-')str[j]='+';
					else str[j] = '-';
				}
			}
			
			else
			{
				++i;
			}
		}
		
		int flag = 0;
		for(i=0;i<n;++i)
		{
			if(str[i]=='-')
			{
				printf("IMPOSSIBLE\n");
				flag = 1;
				break;
			}
		}
		
		if(!flag)
		{
			printf("%d\n", res);
		}
	}
	
	return 0;
}
