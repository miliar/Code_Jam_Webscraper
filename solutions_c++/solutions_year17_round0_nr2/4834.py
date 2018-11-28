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
	int t, caso, aux, i, j, k, ini;
	string s;
	scanf("%d", &t);
	caso = 1;
	while(t--)
	{
		cin >> s;
		for(i=s.size()-1; i>=0; i--)
		{
			if(s[i] < s[i-1])
			{
				for(j=s.size()-1; j>=i; j--)
					s[j] = '9';
				k = i-1;
				while(1)
				{
					if(k == -1)
						break;
					if(s[k] != '0')
					{
						s[k]--;
						break;
					}
					s[k] = '9';
					k--;
				}
			}
		}
		ini = 0;
		if(s[0] == '0')
			ini = 1;
		printf("Case #%d: ", caso++);
		for(i=ini; i<s.size(); i++)
			printf("%c", s[i]);
		printf("\n");
	}
}
						
					
			
