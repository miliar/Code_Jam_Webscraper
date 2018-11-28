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
    	int r, c;
    	cin >> r >> c;
    	vector<string> s(r);
    	for (auto &p : s)
    		cin >> p;
    	vector<int> fr(26, r), lr(26, -1), fc(26, c), lc(26, -1);
    	for (int i = 0; i < r; i++)
    		for (int j = 0; j < c; j++)
    			if (s[i][j] != '?')
	    		{
	    			fr[s[i][j] - 'A'] = lr[s[i][j] - 'A'] = i;
	    			fc[s[i][j] - 'A'] = lc[s[i][j] - 'A'] = j;
	    		}

		for (int i = 0; i < r; i++)
			for (int j = 0; j < c; j++)
				if (s[i][j] == '?')
					for (int k = 0; k < 26; k++)
						if (lr[k] + 1)
						{
							int fail = 0;
							for (int ii = min(fr[k], i); ii <= max(lr[k], i); ii++)
								for (int jj = min(fc[k], j); jj <= max(lc[k], j); jj++)
									fail |= s[ii][jj] != '?' && s[ii][jj] != k + 'A';
							if (!fail)
							{
								fr[k] = min(fr[k], i);
								lr[k] = max(lr[k], i);
								fc[k] = min(fc[k], j);
								lc[k] = max(lc[k], j);
								for (int ii = fr[k]; ii <= lr[k]; ii++)
									for (int jj = fc[k]; jj <= lc[k]; jj++)
										s[ii][jj] = k + 'A';
								break;
							}
						}

    	/*for (int i = 0; i < r; i++)
    		for (int j = 0; j < c; j++)
    			if (s[i][j] == '?')
    			{
    				char f = '?';
    				for (int ii = i; ii >= 0 && f == '?'; ii--)
    				{
    					for (int jj = j; jj >= 0 && f == '?'; jj--)
    						if (s[ii][jj] != '?')
    							f = s[ii][jj];
    					for (int jj = j + 1; jj < c && f == '?'; jj++)
    						if (s[ii][jj] != '?')
    							f = s[ii][jj];
    				}
    				for (int ii = i + 1; ii < r && f == '?'; ii++)
    				{
    					for (int jj = j; jj >= 0 && f == '?'; jj--)
    						if (s[ii][jj] != '?')
    							f = s[ii][jj];
    					for (int jj = j + 1; jj < c && f == '?'; jj++)
    						if (s[ii][jj] != '?')
    							f = s[ii][jj];
    				}
    				s[i][j] = f;
    			}*/
    	cout << "Case #" << tc + 1 << ": " << endl;
    	for (int i = 0; i < r; i++)
    		cout << s[i] << endl;
    }
    return 0;
}