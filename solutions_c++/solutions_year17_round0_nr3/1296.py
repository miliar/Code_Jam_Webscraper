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
    	long long n, k;
    	cin >> n >> k;
    	long long c = n;
    	long long d1 = 1, d2 = 0;
    	long long sum = 0;
    	long long result = 0;
    	while (1)
    	{
    		//cout << c << " " << d1 << " " << d2 << " " << sum << endl;
    		sum += d1;
    		if (sum >= k)
    		{
    			result = c;
    			break;
    		}
    		sum += d2;
    		if (sum >= k)
    		{
    			result = c - 1;
    			break;
    		}
    		long long nd1 = c % 2 ? d1 * 2 + d2 : d1;
    		long long nd2 = 2 * (d1 + d2) - nd1;
    		c = (c - 1) - (c - 1) / 2;
    		d1 = nd1;
    		d2 = nd2;
    	}
    	result--;
    	cout << "Case #" << tc + 1 << ": " << (result - result / 2) << " " << result / 2 << endl;
    }
    return 0;
}