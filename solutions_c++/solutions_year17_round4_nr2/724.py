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
    	int n, c, m;
    	cin >> n >> c >> m;
    	vector<int> pos(m), id(m);
    	vector<int> ord(c), freq(n);
    	for (int i = 0; i < m; i++)
    	{
    		cin >> pos[i] >> id[i];
    		pos[i]--, id[i]--;
    		ord[id[i]]++, freq[pos[i]]++;
    	}
    	int l = 1;
    	for (int i = 0; i < c; i++)
    		l = max(l, ord[i]);
    	int r = m;
    	int prom = 0;
    	while (l < r)
    	{
    		int mid = (l + r) / 2;
    		prom = 0;
    		int free = 0;
    		int fail = 0;
    		for (int i = 0; i < n; i++)
    			if (freq[i] <= mid + free)
    			{
    				int nprom = max(0, freq[i] - mid);
    				free -= nprom;
    				prom += nprom;
    				if (nprom == 0)
    					free += mid - freq[i];
    			}
    			else
    			{
    				fail = 1;
    				break;
    			}
    		if (fail)
    			l = mid + 1;
    		else
    			r = mid;
    	}
    	cout << "Case #" << tc + 1 << ": " << l << " " << prom << endl;
    }
    return 0;
}