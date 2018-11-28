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
    	long long n;
    	cin >> n;
    	stringstream ss;
    	ss << n;
    	string s = ss.str();
    	int len = s.length();
    	while (1)
    	{
    		int fail = 0;
    		for (int i = 0; i < len - 1; i++)
    			if (s[i] > s[i + 1])
    			{
    				s[i]--;
    				for (int j = i + 1; j < len; j++)
    					s[j] = '9';
    				fail = 1;
    			}
    		if (!fail)
    			break;
    	}
    	if (s[0] == '0')
    		s = s.substr(1);
    	cout << "Case #" << tc + 1 << ": " << s << endl;
    }
    return 0;
}