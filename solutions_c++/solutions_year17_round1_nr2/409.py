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

int main()
{
    freopen("input.txt", "r", stdin);
    freopen("output.txt", "w", stdout);
    int tn;
    cin >> tn;
    for (int tc = 0; tc < tn; tc++)
    {
    	int n, p;
    	cin >> n >> p;
    	vector<int> r(n);
    	for (int &z : r)
    		cin >> z;
    	vector<vector<int> > q(n, vector<int>(p));
    	vector<int> c(n);
    	for (int i = 0; i < n; i++)
    	{
    		for (int j = 0; j < p; j++)
    			cin >> q[i][j];
    		sort(q[i].begin(), q[i].end());
    	}
    	int result = 0;
    	for (long long k = 1; k <= 1000000; k++)
    	{
    		while (1)
    		{
	    		int fail = 0;
	    		for (int i = 0; i < n; i++)
	    		{
	    			while (c[i] < p && q[i][c[i]] * 100LL < r[i] * k * 90)
	    				c[i]++;
	    			fail |= c[i] == p || q[i][c[i]] * 100LL > r[i] * k * 110;
	    		}
	    		if (!fail)
	    		{
	    			result++;
	    			for (int i = 0; i < n; i++)
	    				c[i]++;
	    		}
	    		else
	    			break;
    		}
    	}
    	cout << "Case #" << tc + 1 << ": " << result << endl;
    }
    return 0;
}