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
bool check(string s)
{
	for (int i = 1;i < sz(s);i++)
		if (s[i] < s[i - 1])
			return false;
	return true;
}
int main()
{	
	freopen("B-large.in", "r", stdin);
	freopen("output.txt", "w", stdout);
	int T;
	cin >> T;
	for (int t = 1;t <= T;t++)
	{
		string s;
		cin >> s;
		if (sz(s) == 1)
			cout << "Case #" << t << ": " << s << "\n";
		else
		{
			while (1)
			{
				if (check(s))
					break;
				for (int i = 1;i < sz(s);i++)
					if (s[i] < s[i - 1])
					{
						s[i - 1]--;
						for (int j = i;j < sz(s);j++)
							s[j] = '9';
					}
			}
			while (*s.begin() == '0')
				s.erase(s.begin());
			cout << "Case #" << t << ": " << s << "\n";
		}
	}
	return 0;
}