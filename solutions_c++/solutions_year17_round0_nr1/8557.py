#include <cstdio>
#include <iostream>
#include <cstring>
using namespace std;

int main()
{
	int n;
	scanf("%d",&n);
	for (int i = 0; i < n; ++i)
	{
		char s[1010]={};
		int limit;
		scanf("%s %d",s,&limit);
		int cnt = 0;
		for (int j = 0; j < strlen(s) - limit+1 ; ++j)
		{	
			//printf("%s\n",s );
			if (s[j]=='-')
			{	
				
				for (int l = j; l < j+limit; ++l)
				{	
					if (s[l]=='-')
					{
						s[l]='+';
					}
					else
						s[l]='-';
				}
				cnt+=1;
			}
		}
		int flag=0;
		for (int j = 0; j < strlen(s); ++j)
		{
			if (s[j]=='-')
			{
				flag=1;
				break;
			}
		}
		if (flag)
		{
			printf("Case #%d: IMPOSSIBLE\n", i+1 );
		}
		else
			printf("Case #%d: %d\n", i+1,cnt );
	}
	return 0;
}