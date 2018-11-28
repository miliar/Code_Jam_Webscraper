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

char flip(char c)
{
	if(c == '+')return '-';
	return '+';
}

int main()
{
	int t;
	cin >> t;
	for(int test=0; test<t; test++)
	{
		cout << "Case #" << test+1 << ": ";
		int k;
		string s;
		cin >> s >> k;
		int res = 0;
		for(int i=0; i+k<=s.size(); i++)
		{
			if(s[i] == '-')
			{
				res++;
				for(int j=i; j<i+k; j++)
				{
					s[j] = flip(s[j]);
				}
			}
		}
		bool imp = 0;
		for(int i=0; i<s.size(); i++)
		{
			if(s[i] == '-')
			{
				imp = 1;
				break;
			}
		}
		if(imp)cout << "IMPOSSIBLE" << endl;
		else cout << res << endl;
	}
	return 0;
}