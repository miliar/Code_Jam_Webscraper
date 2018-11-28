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
		int n, c, m;
		cin >> n >> c >> m;
		
		int x[1024] = {0};
		int y[1024] = {0};
		for(int i=0; i<m; ++i)
		{
			int p, b;
			cin >> p >> b;
			--p, --b;
			++x[b];
			++y[p];
		}

		int ans = 0, z = 0;
		for(int i=0; i<c; ++i)
			ans = max(ans, x[i]);

		for(int limit=ans; limit<=1000; ++limit)
		{
			int newr = 0;

			bool ok = 1;
			int nf = 0;
			for(int i=0; ok && i<n; ++i)
			{
				nf += max(0,limit - y[i]);
				int d = max(0, y[i]-limit);
				nf -= d;
				newr += d;
				if(nf < 0)
					ok = 0;

			}
			if(ok)
			{
				z += newr;
				ans = max(ans, limit);
				break;
			}
		}

		cout << "Case #" << tt << ": " << ans << " " << z << "\n";
		cout.flush();
	}

	return 0;
}
