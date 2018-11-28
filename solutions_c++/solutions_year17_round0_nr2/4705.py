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
	forin(test, 1, t+1)
	{
		string s;
		cin >> s;
		int n = s.length();
		forin(i, 1, n)
		{
			if(s[i] < s[i-1])
			{
				forin(j, i, n)
					s[j] = '9';
				i--;
				while(i >= 0)
				{
					s[i]--;
					if(i && (s[i] < s[i-1]))
						s[i] = '9';
					else
						break;
					i--;
				}
				break;
			}
		}
		int i = 0;
		for(;s[i] == '0';i++);
		s = s.substr(i, n - i);
		cout << "Case #" << test << ": " << s << endl;
	}
}
