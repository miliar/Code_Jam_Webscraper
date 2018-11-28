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
		long long n, k;
		cin >> n >> k;
		set <pair<long long, long long>> s;
		s.insert({-n, 0});
		while(k--)
		{
			auto pi = *s.begin();
			s.erase(s.begin());
			long long len = -pi.first;
			long long st = pi.second;
			long long pos = st + (len - 1)/2;
			if(k == 0)
				cout << len - (pos - st + 1) << " " << pos - st << endl;
			s.insert({-(pos - st), st});
			s.insert({-(len - (pos - st + 1)), pos + 1});
		}
	}
}
