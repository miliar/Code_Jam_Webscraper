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
#include <numeric>

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
    	vector<int> g(n);
    	vector<int> cnt(p);
    	for (int i = 0; i < n; i++)
    		cin >> g[i], cnt[g[i] % p]++;
    	int result = cnt[0];
    	for (int i = 1; i * 2 < p; i++)
    	{
    		int z = min(cnt[i], cnt[p - i]);
    		cnt[i] -= z;
    		cnt[p - i] -= z;
    		result += z;
    	}
    	if (p % 2 == 0)
    	{
    		result += cnt[p / 2] / 2;
    		cnt[p / 2] %= 2;
    	}
    	if (p == 2)
    	{
    		if (cnt[1])
    			result++;
    	}
    	else if (p == 3)
    	{
    		int z = max(cnt[1], cnt[2]);
    		result += z / 3;
    		z %= 3;
    		if (z)
    			result++;
    	}
    	else
    	{
    		int z = max(cnt[1], cnt[3]);
    		int best = result + z / 4 + (z % 4 != 0 || cnt[2]);
    		if (cnt[2] && z >= 2)
    			best = max(best, result + 1 + (z - 2) / 4 + ((z - 2) % 4 != 0));
    		result = best;
    	}
    	cout << "Case #" << tc + 1 << ": " << result << endl;
    }
    return 0;
}
