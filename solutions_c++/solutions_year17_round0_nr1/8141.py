#define _CRT_SECURE_NO_WARNINGS
#include<bits/stdc++.h>
#define all(v)              ((v).begin()), ((v).end())
#define allr(v)             ((v).rbegin()), ((v).rend())
#define sz(v)               ((int)((v).size()))
#define clr(v, d)           memset(v, d, sizeof(v))
#define MP                  make_pair
#define lpv(i, v)           for(int i=0;i<sz(v);++i)
#define lpn(i, n)           for(int i=0;i<(int)(n);++i)
#define PI                  3.14159265359
#define pb                  push_back
#define ull                 unsigned long long
#define ll                  long long
#define LD                  long double
#define vi                  vector<int>
#define vl                  vector<ll>
#define vs                  vector<string>
#define vp                  vector<pair<int,int>>
#define OO                  (int)2e9	
using namespace std;
const ll MOD = 1e9 + 7;

int main()
{	
	freopen("A-large.in", "r", stdin);
	freopen("output.txt", "w", stdout);
	int T;
	cin >> T;
	for (int t = 1;t <= T;t++)
	{
		bool ok = true;
		string s;
		cin >> s;
		int k;
		cin >> k;
		int res = 0;
		if (s.find('-') == -1)
			res = 0;
		else if (s.find('+') == -1 && s.size() % k != 0)
			ok = false;
		else if (s.find('+') == -1 && s.size() % k == 0)
			res = s.size() / k;
		else
		{
			for (int i = 0;i < sz(s);i++)
			{
				int temp = k;
				if (s[i] == '-'&&i + k <= sz(s))
				{
					for (int j = i;j < sz(s) && temp;j++)
						s[j] == '-' ? s[j] = '+' : s[j] = '-', temp--;
					res++;
				}
				else if (s[i] == '-'&&i + k > sz(s))
				{
					ok = false;
					break;
				}
			}
		}
		if (!ok)
			printf("Case #%d: IMPOSSIBLE\n", t);
		else
			printf("Case #%d: %d\n", t, res);
	}
	return 0;
}