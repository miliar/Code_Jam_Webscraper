#include <iostream>
#include <string>
#include <cstdio>
#include <cstdlib>
#include <cmath>
using namespace std;
typedef long long int ll;
int main()
{
	int t;
	scanf("%d",&t);
	int l;
	for(l=1;l<=t;l++)
	{
		string s;
		int k;
		cin>>s>>k;
		int size = s.length();
		int i,j;
		ll count = 0;
		for(i=0;i<=size-k;i++)
		{
			if(s[i]=='-')
			{
				count++;
				for(j=i;j<i+k;j++)
				{
					if(s[j]=='-')
					{
						s[j] = '+';
					}
					else
					{
						s[j] = '-';
					}
				}
			}
		}
		int flag = 0;
		for(i=0;i<size;i++)
		{
			if(s[i]=='-')
			{
				flag=1;
				break;
			}
		}
		if(flag==0)
		{
			printf("Case #%d: %lld\n",l,count);
		}
		else
		{
			printf("Case #%d: IMPOSSIBLE\n",l);
		}
	}
	return 0;
}
		