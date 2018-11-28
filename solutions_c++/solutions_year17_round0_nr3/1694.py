
/* 
Take yourself as work in progress.
-Bhai
*/

#include<bits/stdc++.h>
using namespace std;

#define M 1000000007
#define LL long long
#define PB push_back
#define MP make_pair
#define F first
#define S second
#define VI vector<int>
#define SZ(a) int(a.size())
#define TR(c, it) for(typeof((c).begin()) it=(c).begin(); it!=(c).end(); it++ )
#define SET(a, b) memset(a, b, sizeof(a))

LL n, k;
map<LL, LL> m;
set<LL> is;
pair<LL, LL> z;
LL ans;


int main()
{
	ios_base::sync_with_stdio(0);
	int t;
	cin >> t;
	int nahoy = 1;
	while(t--)
	{
		cin >> n >> k;
		
		m.clear();
		is.clear();
		m[n] = 1LL;
		is.insert(n);
		ans = 0;

		while(1)
		{
			z = *(m.rbegin());
			if(z.S >= k)
			{
				ans = z.F;
				break;
			}
			
			m.erase((m.rbegin())->F);
			is.erase(z.F);

			LL seg1 = z.F/2;
			LL seg2 = (z.F-1)/2;

			m[seg1] += z.S;
			m[seg2] += z.S;
			
			k -= z.S;
		}

		cout << "Case #" << nahoy << ": " << ans/2 << " " << (ans-1)/2 << endl;

		nahoy += 1;
	}
	return 0;
}
