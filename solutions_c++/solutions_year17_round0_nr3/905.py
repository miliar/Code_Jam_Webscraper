#include<bits/stdc++.h>
using namespace std;

int main()
{
	int t;
	cin >> t;
	for(int tc = 1; tc <= t; ++tc)
	{
		long long n, k;
		cin >> n >> k;
		
		map<long long, long long> mp;
		mp[n] = 1;
		
		long long L, R;
		
		while(!mp.empty())
		{
			pair<long long, long long> p = *mp.rbegin();
			long long x = p.first, y = p.second;
			mp.erase(x);
			if(x&1)
				mp[x/2] += 2*y;
			else
			{
				mp[x/2] += y;
				mp[(x/2)-1] += y;
			}
			
			k -= y;
			if(k<=0)
			{
				if(x&1)
					L = R = x/2;
				else
				{
					L = (x/2);
					R = (x/2)-1;
				}
				break;
			}
		}
		
		cout << "Case #" << tc << ": " << L << " " << R << endl;
	}
	return 0;
}
