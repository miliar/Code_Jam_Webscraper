#include <stdio.h>
#include <string.h>
#include <cstring>
#include <string.h>
#include <string>
#include <iostream>
using namespace std;


int main()
{
	int T, K;
	scanf("%d", &T);
	int ans=0;
	string S;
	char* s=new char[1001];
	for(int i=1;i<=T;i++)
	{
		ans=0;
		bool possible=true;
		cin>>S>>K;
		
		int L=S.length();
		for(int index=0;index<S.length();index++)
		{
			s[index]=S[index];
		}
		
		int j=0;
		for(j=0;j<=L-K;j++)
		{
			if(s[j]=='-')
			{
				for(int k=j;k<j+K;k++)
				{
					if(s[k]=='+')
						s[k]='-';
					else
						s[k]='+';
				}
				ans++;
			}
		}
		
		for(int k=j;k<L;k++)
		{
			if(s[k]=='-')
			{
				possible=false;
				break;
			}
		}
		
		if(possible)
			printf("Case #%d: %d\n", i, ans);
		else
			printf("Case #%d: IMPOSSIBLE\n", i);
	}
	return 0;
}
