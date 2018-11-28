#include <iostream>
#include <vector>
#include <string>
#include <bitset>
#include <map>
#include <algorithm>
#define ll long long int
using namespace std;

template <typename T>
struct comp {
	bool operator() ( T a, T b) const
	{
		return a > b;
	};

};


int main()
{
	iostream::sync_with_stdio(0);
	cin.tie(0);
	int t;
	cin >> t;
	for (int q = 0; q < t; q++)
	{
		ll a, b;
		cin >> a >> b;
		map<ll, ll,comp<ll> > toi;
		toi[a] = 1;
		while (b>0)
		{			
			int num = min(b,toi.begin()->second);
			
			ll cr = toi.begin()->first;
			
			b -= num;
			if ((cr-1) % 2)
			{
				
				toi[(cr-1)/2] += num;
				toi[(cr-1)/2 + 1] += num;
				toi.erase(toi.begin());
			}
			else
			{
				toi[(cr-1) / 2] += num*2;
				toi.erase(toi.begin());
			}
			if (b <= 0) {
				ll  o1, o2;	
				if ((cr - 1) % 2)
				{
					o1 = (cr - 1) / 2;
					o2 = (cr - 1) / 2 + 1;
				}
				else
				{
					o1 = (cr - 1) / 2;
					o2 = (cr - 1) / 2;
				}

			
			cout << "Case #" << q + 1 << ": " << max(o1, o2) << " " << min(o1, o2) << "\n";
			}
						
		}

	}
	
	return 0;
}

