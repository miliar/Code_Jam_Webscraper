#include <bits/stdc++.h>
using namespace std;
typedef unsigned long long ull;

void flip(string& s,int i)
{
	if (s[i] == '+')
	{
		s[i] = '-';
	}
	else
	{
		s[i] = '+';
	}
}
int main()
{
	int t;
	cin>>t;
	int testCaseNum = 0;
	while(t--)
	{
		string s;
		cin>>s;
		int k;
		cin>>k;
		testCaseNum++;
		printf("Case #%d: ", testCaseNum);
		int count = 0;
		for (int i = 0; i <= s.length() - k; ++i)
		{
			if (s[i] == '-')
			{
				for (int j = i; j < i + k; ++j)
				{
					flip(s,j);
				}
				count++;
			}
		}
		bool possible = true;
		for (int i = 0; i < s.length(); ++i)
		{
			if (s[i] == '-')
			{
				possible = false;
			}
		}
		if (possible)
		{
			printf("%d\n", count);
		}
		else
		{
			printf("IMPOSSIBLE\n");
		}
	}



	return 0;
}