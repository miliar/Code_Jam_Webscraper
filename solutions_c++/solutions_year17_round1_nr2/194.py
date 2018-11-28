#include <cmath>
#include <cstdio>
#include <cstring>
#include <set>
#include <map>
#include <stack>
#include <queue>
#include <vector>
#include <string>
#include <numeric>
#include <sstream>
#include <iostream>
#include <algorithm>
using namespace std;
typedef long long ll;

int main()
{
	int t;
	
	cin >> t;
	for(int tt=1; tt<=t; ++tt)
	{
		int n, p;
		cin >> n >> p;
		vector<ll> r(n);
		ll q[64][64];
		for(int i=0; i<n; ++i)
			cin >> r[i];
		for(int i=0; i<n; ++i)
		{
			for(int j=0; j<p; ++j)
				cin >> q[i][j];
			sort(&q[i][0], &q[i][p]);
		}
		//print(n,p);
		
		int ans = 0;		
		int idx[64] = {0};
		for(ll cnt=1; cnt<=1000000; ++cnt)
		{
			bool ok = 1;
			for(int i=0; i<n; ++i)
			{
				while(idx[i] < p && q[i][idx[i]]*100 < cnt*r[i]*90)
				{
					++idx[i];
				}
				if(p <= idx[i])
				{
					ok = 0;
					continue;
				}
				ll v = q[i][idx[i]];
				if(!(cnt*r[i]*90 <= v*100 && v*100 <= cnt*r[i]*110))
					ok = 0;
			}
			
			if(ok)
			{
				for(int i=0; i<n; ++i)
				{
					++idx[i];
				}
				++ans;
				--cnt;
			}

			bool f = 1;
			for(int i=0; i<n; ++i)
				if(idx[i] < p)
					f = 0;
			if(f)
				break;
		}
		
		cout << "Case #" << tt << ": " << ans << "\n";
		cout.flush();
	}

	return 0;
}
