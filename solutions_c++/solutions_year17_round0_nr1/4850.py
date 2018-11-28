#include <bits/stdc++.h>
#define mp make_pair
#define ft first
#define sd second
#define ue printf("what?\n");
#define pb push_back
#define pf push_front
#define oo 0x3F3F3F3F
#define OO 0x3F3F3F3F3F3F3F3F
#define EPS 1e-2
#define inf 1000000000000000LL
#define N 100005
#define pi acos(-1)
#define mod 1000000007

typedef long long ll;

using namespace std;

main()
{
	int t, caso, k, rsp, i, j;
	string s;
	scanf("%d", &t);
	caso = 1;
	while(t--)
	{
		cin >> s >> k;
		rsp = 0;
		for(i=0; i <= s.size()-k;  i++)
		{
			if(s[i] == '+')
				continue;
			rsp++;
			for(j=i; j<i+k; j++)
			{
				if(s[j] == '+')
					s[j] = '-';
				else
					s[j] = '+';
			}
		}
		bool y = 1;
		for(i=s.size()-k+1; i<s.size(); i++)
			if(s[i] == '-')
				y = 0;
		printf("Case #%d: ", caso++);
		if(y)
			printf("%d\n", rsp);
		else
			printf("IMPOSSIBLE\n");
	}
}
