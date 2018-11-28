//Created By Mayur Agarwal :)

#include <iostream>
#include <stdio.h>
#include <cmath>
#include <vector>
#include <string>
#include <cstring>
#include <set>
#include <algorithm>
#include <map>
#include <iterator>
#include <functional>
#include <queue>
#include <stack>

#define ll long long
#define ind(a) scanf("%d",&a)
#define in(a) scanf("%lld",&a)
#define inc(a) scanf("%c",&a)
#define ins(a) scanf("%s",a)
#define pr(a) printf("%lld\n",a)
#define bitcnt(x) __builtin_popcountll(x)
#define debug(x) cout << #x << " = " << x << endl
#define MS0(X) memset((X), 0, sizeof((X)))
#define MS1(X) memset((X), -1, sizeof((X)))
#define pb push_back
#define MP make_pair
#define ff first
#define ss second
#define SIZE 200010
const ll mod = 1000000007L;

using namespace std;
typedef pair<ll, ll>pll;
string s;
int main()
{
#ifndef ONLINE_JUDGE
	freopen("input.txt", "r", stdin);
	//freopen("output1.txt", "w", stdout);
#endif
	ios_base::sync_with_stdio(0); cin.tie(0);
	int t;
	cin >> t;
	for (int tc = 1; tc <= t; tc++)
	{
		cout << "Case #" << tc << ": ";
		cin >> s;
		int n = s.size();
		int idx = -1;
		for (int i = 0; i < n; i++)
		{
			if ((i + 1 < n) && ((s[i] - '0') > s[i + 1] - '0'))
			{
				idx = i;
				break;
			}
		}
		if (idx == -1)
		{
			cout << s << endl;
		}
		else
		{
			//cout << idx << endl;
			if (idx == 0)
			{
				int val = (s[idx] - '0') - 1;
				if (val != 0)
					cout << val;
				for (int i = 1; i < n; i++)
				{
					cout << "9";
				}
			}
			else
			{
				int val = (s[idx] - '0') - 1;
				int v = (s[idx - 1] - '0');
				if (v <= val)
				{
					for (int i = 0; i < idx; i++)
						cout << s[i];
					cout << val;
					for (int i = idx + 1; i < n; i++)
						cout << "9";
				}
				else
				{
					if (val == 0)
					{
						for (int i = 0; i < n - 1; i++)
							cout << "9";
					}
					else
					{
						int temp = val, idx1 = -1;
						//cout << idx << " " << temp << endl;
						for (int i = idx; i >= 0; i--)
						{
							if (temp >= (s[i] - '0'))
							{
								idx1 = i;
								break;
							}
						}
						///cout << "###" << idx1 << endl;
						if (idx1 == -1)
						{
							cout << temp;
							for (int i = 1; i < n; i++)
								cout << "9";
						}
						else
						{
							for (int i = 0; i <= idx1; i++)
								cout << s[i];
							cout << temp;
							for (int i = idx1 + 2; i < n; i++)
								cout << "9";
						}
					}
				}
			}
			cout << endl;
		}
	}
	return 0;
}