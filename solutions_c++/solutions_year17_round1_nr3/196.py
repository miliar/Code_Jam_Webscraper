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
		int hd, ad, hk, ak, B, D;
		cin >> hd >> ad >> hk >> ak >> B >> D;
		int ans = -1;
		
		for(int nd=0; nd<=100; ++nd)
			for(int na=0; na<=100; ++na)
			{
				int a1 = ad;
				int a2 = ak;
				int h1 = hd;
				int h2 = hk;
				int turn = 1;
				int id=0,ia=0;
				for(; turn<na+nd+300; ++turn)
				{
					//print(turn, h1, h2, a1, a2);
					if(h2 <= a1)
					{
						h2 = 0;
						break;
					}
					bool need_debuff = id < nd;
					int ka = need_debuff ? a2-D : a2;
					if(h1 - ka <= 0)
					{
						h1 = hd - a2;
						continue;
					}
					bool need_buff = !need_debuff && ia < na;
					if(need_debuff)
					{
						a2 -= D;
						++id;
					}
					else if(need_buff)
					{
						a1 += B;
						++ia;
					}
					else
						h2 -= a1;
					if(h2 <= 0)
						break;
					
					h1 -= a2;
					if(h1 <= 0)
						break;
				}
				if(h2 <= 0)
				{
					if(ans < 0 || turn < ans)
						ans = turn;
				}
			}

		if(ans < 0)
			cout << "Case #" << tt << ": IMPOSSIBLE\n";
		else
			cout << "Case #" << tt << ": " << ans << "\n";
		cout.flush();
	}

	return 0;
}
