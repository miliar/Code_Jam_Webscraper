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

int main()
{
	ios_base::sync_with_stdio(false); cin.tie(0);
	ll t,z;
	cin >> t;
	REP(z,t)
	{
		cout << "Case #" << z+1 << ": ";
		ll i,n,k,ans=0;
		queue<ll>q;
		//queue<ll>num;
		map<ll,ll>num;
		cin >> n >> k;
		q.push(n);
		num[n]=1;
		while(1)
		{
			ll cleg = q.front();
			ll cnum = num[cleg];
			ans+=cnum;
			ll temp;
			ll oth = cleg/2;
			if(cleg%2)
			{
				if(!num[cleg/2])
					q.push(cleg/2);
				num[cleg/2]+=(cnum*2);
				temp=cleg/2;
			}
			else
			{
				if(!num[cleg/2])
					q.push(cleg/2);
				num[cleg/2]+=(cnum);
				if(!num[(cleg-1)/2])
					q.push((cleg-1)/2);
				num[(cleg-1)/2]+=(cnum);
				temp=(cleg-1)/2;
			}
			q.pop();
			if(ans>=k)
			{
				cout << oth << " " << temp << "\n";
				break;
			}
		}
	}
	return 0;
}

