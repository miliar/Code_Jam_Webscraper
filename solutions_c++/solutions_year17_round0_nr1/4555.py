	//     . .. ... .... ..... be name khoda ..... .... ... .. .     \\

#include <algorithm>
#include <iostream>
#include <fstream>
#include <iomanip>
#include <cassert>
#include <cstdlib>
#include <cstdio>
#include <string>
#include <vector>
#include <cmath>
#include <set>
#include <map>
using namespace std;

inline int in() { int x; scanf("%d", &x); return x; }
const int N = 2002;

int main()
{
	int _t = in();
	for(int _i = 1; _i <= _t; _i++)
	{
		printf("Case #%d: ", _i);
		string s;
		cin >> s;
		int n = s.size();
		int k = in();
		int ans = 0;
		bool could = true;
		for(int i = 0; i <= n - k; i++)
			if(s[i] == '-')
			{
				for(int j = i; j < i + k; j++)
					s[j] = (s[j] == '-' ? '+' : '-');
				ans++;
			}
		for(int i = n - k + 1; i < n; i++)
			could &= (s[i] == '+');
		if(!could)
			cout << "IMPOSSIBLE\n";
		else
			cout << ans << endl;
	}
}
