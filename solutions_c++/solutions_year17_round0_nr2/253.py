#include <bits/stdc++.h>
using namespace std;

#define inf 1023456789
#define linf 1023456789123456789ll
#define pii pair<int,int>
#define pipii pair<int, pii >
#define pll pair<long long,long long>
#define vint vector<int>
#define vvint vector<vint >
#define ll long long
#define pdd pair<double, double>

#define DEBUG
#ifdef DEBUG
#define db(x) cerr << #x << " = " << x << endl
#else
#define db(x)
#endif

ll solve(ll n)
{
	vector<int> dec;
	while(n)
	{
		dec.push_back(n%10);
		n /= 10;
	}
	
	ll res = 0;
	bool tesne = 1;
	for(int i=dec.size()-1; i>=0; i--)
	{
		res *= 10;
		if(tesne)
		{
			bool ok = 1;
			for(int j=i-1; j >= 0; j--)
			{
				if(dec[j] > dec[i])break;
				if(dec[j] < dec[i])
				{
					ok = 0;
					break;
				}
			}
			if(ok)
			{
				res += dec[i];
			}
			else
			{
				res += dec[i]-1;
				tesne = 0;
			}
		}
		else
		{
			res += 9;
		}
	}
	return res;
}

int main()
{
	int t;
	scanf("%d", &t);
	for(int test=0; test<t; test++)
	{
		ll n;
		scanf("%lld", &n);
		printf("Case #%d: %lld\n", test+1, solve(n));
	}
	return 0;
}