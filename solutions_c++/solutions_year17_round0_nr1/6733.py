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
#endif
	ios_base::sync_with_stdio(0); cin.tie(0);
	int t;
	cin >> t;
	for (int tc = 1; tc <= t; tc++)
	{
		cout << "Case #" << tc << ": ";
		cin >> s;
		int n = s.size();
		int K;
		cin >> K;
		int cnt = 0;
		for (int i = 0; i <= n - K; i++)
		{
			if (s[i] == '+')
				continue;
			cnt++;
			for (int j = 0; j < K; j++)
			{
				if (s[i + j] == '+')
					s[i + j] = '-';
				else
					s[i + j] = '+';
			}
		}
		bool flag = 0;
		for (int i = 0; i < n; i++)
		{
			if (s[i] == '-')
			{
				flag = 1;
				break;
			}
		}
		if (flag)
		{
			cout << "IMPOSSIBLE\n";
		}
		else
		{
			cout << cnt << endl;
		}
	}
	return 0;
}