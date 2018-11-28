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
		vector<int> a(n);
		int nn[4] = {0};
		for(int i=0; i<n; ++i)
		{
			cin >> a[i];
			++nn[a[i]%p];
		}
		
		int ans = nn[0];
		n -= nn[0]; nn[0] = 0;
		int s = 0;
		for(int i=0; i<n; ++i)
		{
			if(!s)
				++ans;

			bool ok = 0;
			for(int j=1; !ok && j<p; ++j) if(nn[j])
				for(int l=j; !ok && l<p; ++l) if(nn[l])
				{
					if((j+l) % p == 0)
					{
						ok = 1;
						nn[j]--;
						nn[l]--;
						--n;
					}
				}

			if(!ok)
			{
				for(int j=1; j<p; ++j) if(nn[j])
				{
					s = (s + j) % p;
					nn[j]--;
				}
			}
		}

		cout << "Case #" << tt << ": " << ans << "\n";
		cout.flush();
	}

	return 0;
}
