#include <iostream>
#include <cstdio>
#include <cmath>
#include <vector>
#include <cstring>
#include <string>
#include <map>
#include <set>
#include <list>
#include <algorithm>
#include <cctype>
#include <queue>
#include <complex>
#include <functional>
#include <sstream>
#include <tuple>

using namespace std;

short dp[102][102][102][102];
short inf = 10000;

int HD, AD, HK, AK, B, D;

short attk(int d)
{
	return max(0, AK - D * d);
}

int main()
{
    freopen("input.txt", "r", stdin);
    freopen("output.txt", "w", stdout);
    int tn;
    cin >> tn;
    for (int tc = 0; tc < tn; tc++)
    {
    	cin >> HD >> AD >> HK >> AK >> B >> D;
    	for (int hk = 1; hk <= HK; hk++)
    		for (int b = 100; b >= 0; b--)
    			for (int d = 100; d >= 0; d--)
    				for (int hd = HD; hd >= 1; hd--)
    				{
    					int cur = inf;
    					if (hd < HD - attk(d))
    						cur = min(cur, 1 + dp[hk][b][d][HD - attk(d)]);
    					if (hk <= AD + B * b)
    						cur = 1;
    					else if (hd > attk(d))
    						cur = min(cur, 1 + dp[hk - (AD + B * b)][b][d][hd - attk(d)]);
    					if (hd > attk(d) && b < 100)
    						cur = min(cur, 1 + dp[hk][b + 1][d][hd - attk(d)]);
    					if (hd > attk(d + 1) && d < 100)
    						cur = min(cur, 1 + dp[hk][b][d + 1][hd - attk(d + 1)]);
    					dp[hk][b][d][hd] = cur;
    				}
    	if (dp[HK][0][0][HD] == inf)
    		cout << "Case #" << tc + 1 << ": IMPOSSIBLE" << endl;
    	else
    		cout << "Case #" << tc + 1 << ": " << dp[HK][0][0][HD] << endl;
    }
    return 0;
}