#include<bits/stdc++.h>
/*
ID: arun.ga1
LANG: C++
TASK: 
 */

using namespace std;

#define prime 1000000007
#define DEBUG(x) cout << '>' << #x << ':' << x << endl;
#define REP(i,n) for(int i=0;i<(n);i++)
#define FOR(i,a,b) for(int i=(a);i<=(b);i++)
#define FORD(i,a,b) for(int i=(a);i>=(b);i--)
inline bool EQ(double a, double b) { return fabs(a-b) < 1e-9; }
const int INF = 1<<29;
typedef long long ll;
inline int two(int n) { return 1 << n; }
inline int test(int n, int b) { return (n>>b)&1; }
inline void set_bit(int & n, int b) { n |= two(b); }
inline void unset_bit(int & n, int b) { n &= ~two(b); }
inline int last_bit(int n) { return n & (-n); }
inline int ones(int n) { int res = 0; while(n && ++res) n-=n&(-n); return res; }
template<class T> void chmax(T & a, const T & b) { a = max(a, b); }
template<class T> void chmin(T & a, const T & b) { a = min(a, b); }

/////////////////////////////////////////////////////////////////////
ll func(ll x)
{
	string s = static_cast<ostringstream*>( &(ostringstream() << x) )->str();
	ll len = s.size();
	ll flag = 1;
	ll i;
	for(i=0;i<len-1;i++)
	{
		if(s[i]>s[i+1])
			return 2;
	}
	return 3;
}

int main()
{
	ios_base::sync_with_stdio(false); cin.tie(0);
	ll t,k;
	cin >> t;
	REP(k,t)
	{
		cout << "Case #" << k+1 << ": ";
		ll n,flag = 0;
		cin >> n;
		n++;
		while(n--)
		{
			ll ans = func(n);
			if(ans==3)
			{
				cout << n;
				flag = 1;
				break;
			}
			if(flag)
				break;
		}
		cout << "\n";
	}
	return 0;
}

