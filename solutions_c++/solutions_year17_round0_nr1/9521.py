#include <bits/stdc++.h>
using namespace std;

#define ll long long
#define sd(x) scanf("%d",&x)
#define sll(x) scanf("%lld",&x)
#define sc(x) scanf(" %c", &x)
#define MAX 1000007
#define MOD 1000000007

int main()
{
	int t,i,y,test;
	sd(t);
	for(test=1; test<=t; ++test)
	{
		string s; int l,plus=0,minus=0,count=0;
		cin >> s;
		cin >> l;

		for(i=0; i<s.length(); ++i)
		{
			if(s[i] == '-')
			{
				if(s.length()-i >= l)
				{
					for(y=i; ( (y<i+l) and (y<s.length()) ); ++y)
					{
						if(s[y] == '+')
							s[y] = '-';
						else
							s[y] = '+';
					}
					++count;
				}
				else
					count = -1;
			}
		}

		for(i=0; i<s.length(); ++i)
		{
			//cout << "tttttt: " << s[i] << "\n";
			if(s[i] == '-')
				count = -1;
		}

		printf("Case #%d: ", test);	
		if(count == -1)
			printf("IMPOSSIBLE\n");
		else
			printf("%d\n", count);
	}
	return 0;
}