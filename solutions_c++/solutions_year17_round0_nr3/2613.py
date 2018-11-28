#include <bits/stdc++.h>
using namespace std;

typedef long long lint;



int main()
{
	
	int T; cin >> T;
	for(int t = 1; t <= T; t++)
	{
		lint N, K;
		cin >> N >> K;
		map<lint, lint> m;
		m[N]++;
		while(true)
		{
			auto it = m.end(); it--; // largest
			
			lint x = it->first;
			lint l = (x - 1) / 2;
			lint h = x / 2; 
			
			if(K <= it->second)
			{
				cout << "Case #" << t << ": " << h << " " << l << endl;
				break;
			}
			K -= it->second;
			m[l] += it->second;
			m[h] += it->second;
			m.erase(it);
		}
	}
	
	return 0;
}
