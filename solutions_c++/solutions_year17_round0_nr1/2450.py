#include<cstdio>
#include<iostream>
#include<cstring>

using namespace std;

char panc[1200];

int main()
{
	int T;
	cin >> T;
	int K;
	
	for(int tc=1;tc<=T;tc++)
	{
		scanf("%s%d", panc, &K);
		int len = strlen(panc);
		int ans = 0;
		
		for(int i=0;i+K<=len;i++)
		{
			if(panc[i]=='-')
			{
				for(int j=i;j<=i+K-1;j++)
				{
					if(panc[j]=='-') panc[j] = '+';
					else if(panc[j]=='+') panc[j] = '-';
				}
				ans++;
			}
		}
		bool plusSemua = true;
		for(int i=0;i<len;i++)
		{
			if(panc[i]!='+') plusSemua = false;
		}
		if(!plusSemua)
		{
			printf("Case #%d: IMPOSSIBLE\n", tc);
		}
		else{
			printf("Case #%d: %d\n", tc, ans);
		}
	}

	return 0;
}
