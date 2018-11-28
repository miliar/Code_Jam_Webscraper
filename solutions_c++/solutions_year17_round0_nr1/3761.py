#include <cstdio>
#include <cstdlib>
#include <cstring>
#include <string>
#include <cmath>
#include <iostream>
#include <deque>
#include <algorithm>
#include <vector>
#include <ctime>

using namespace std;

int main()
{
	int n;
	int i,j,k,l;
	string str;
	freopen("A.in","r",stdin);
	freopen("A.out","w",stdout);
	cin>>n;
	for (i=0;i<n;i++)
	{
		cin>>str;
		cin>>k;
		int ans=0;
		for (j=0;j<str.length()-k+1;j++)
		{
			if (str[j] == '-')
			{
				for (l=0;l<k;l++)
				{
					str[j+l] = str[j+l]=='-'?'+':'-';
				}
				ans ++;
			}
		}
		for (j=0;j<str.length();j++)
		{
			if (str[j] == '-')
			{
				ans=-1;
				break;
			}
		}
		if (ans == -1)
		{
			printf("Case #%d: IMPOSSIBLE\n",i+1);
		}
		else
		{
			printf("Case #%d: %d\n",i+1,ans);
		}
	}
	fclose(stdin);
	fclose(stdout);
	return 0;
}
