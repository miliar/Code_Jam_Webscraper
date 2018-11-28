#include<bits/stdc++.h>
#include<cmath>

#define forn(i, n) for(int i=0;i<(int)(n);i++)
#define forin(i, k, n) for(int i=k;i<(int)(n);i++)

using namespace std;
using pii = pair<int, int>;
using vi = vector<int>;
using vii = vector<pii>;
using mii = map<int, int>;
using ll = long long;

inline int Read()
{
	register int c=getchar();
	int x=0;
	for(;(c<48 || c>57);c=getchar());
	for(;c>47 && c<58;c=getchar())
		x=(x<<1)+(x<<3)+c-48;
	return x;
}

inline void ReadAI(int *a, int n)
{
	for(int i=0;i<n;i++)
		a[i]=Read();
}

// inline ll Read()
// {
// 	register int c=getchar();
// 	ll x=0;
// 	for(;(c<48 || c>57);c=getchar());
// 	for(;c>47 && c<58;c=getchar())
// 		x=(x<<1)+(x<<3)+c-48;
// 	return x;
// }

// void ReadALL(ll *a, ll n)
// {
// 	for(ll i=0;i<n;i++)
// 		a[i]=Read();
// }

int main()
{
	int t=Read();
	auto flip = [](char &c)
	{
		if(c == '+')
			c = '-';
		else
			c = '+';
	};
	forin(test, 1, t+1)
	{
		string s;
		cin >> s;
		int n = Read(), l = s.length();
		int ans = 0;
		forn(i, l)
		{
			if(s[i] == '+')
				continue;
			if(i + n > l)
				break;
			ans++;
			forin(j, i, i + n)
				flip(s[j]);
		}
		if(find(s.begin(), s.end(), '-') == s.end())
			printf("Case #%d: %d\n", test, ans);
		else
			printf("Case #%d: %s\n", test, "IMPOSSIBLE");
	}
} 
