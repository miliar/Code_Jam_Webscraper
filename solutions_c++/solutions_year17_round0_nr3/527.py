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
		ll n, k;
		cin >> n >> k;
		map<ll,ll> m;
		m[-n] = 1;
		
		ll ansl=0,ansr=0;
		
		while(k)
		{
			ll x = -m.begin()->first;
			ll y = m.begin()->second;
			ll side1 = (x-1)/2;
			ll side2 = (x)/2;
			if(k <= y) {
				ansl = side1;
				ansr = side2;
				break;
			}
			
			k -= y;
			m.erase(m.begin());
			
			m[-side1] += y;
			m[-side2] += y;
		}
		
		
		cout << "Case #" << tt << ": " << ansr << " " << ansl << "\n";
		cout.flush();
	}

	return 0;
}
