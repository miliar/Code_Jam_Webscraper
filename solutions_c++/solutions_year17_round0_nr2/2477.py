#include <vector>
#include <list>
#include <map>
#include <set>
#include <deque>
#include <stack>
#include <bitset>
#include <algorithm>
#include <functional>
#include <numeric>
#include <utility>
#include <sstream>
#include <iostream>
#include <iomanip>
#include <cstdio>
#include <cmath>
#include <cstdlib>
#include <ctime>

#define FILE_NAME "B-large"

using namespace std;

int main()
{
	freopen(FILE_NAME ".in", "r", stdin);
	freopen(FILE_NAME ".out", "w", stdout);
	
	int numTestCaces = 0;
	cin >> numTestCaces;
	for(int Case = 1; Case <= numTestCaces; ++Case)
	{
		long long n;
		cin >> n;
		long long d = 0;
		long long nn = n;
		while(nn > 0)
		{
			++d;
			nn /= 10;
		}
		long long res = n;
		if(d > 1)
		{
			res = 9;
			for(int i = 1; i < d - 1; ++i)
				res = res * 10 + 9;
		}
		long long cand = 1;
		for(int i = 1; i < d; ++i)
			cand = cand * 10 + 1;
		if(cand <= n)
		{
			if(res < cand)
				res = cand;
			for(int i = 0; i < d; ++i)
			{
				long long pt = 1;
				for(int j = 0; j < d - i - 1; ++j)
					pt *= 10;
				long long dig = (cand / pt) % 10;
				while(dig < 9)
				{
					++dig;
					long long tail = dig;
					for(int j = 0; j < d - i - 1; ++j)
						tail = tail * 10 + dig;
					if((cand / pt / 10) * pt * 10 + tail <= n)
						cand = (cand / pt / 10) * pt * 10 + tail;
					else
						break;
					//cerr << cand << endl;
				}
				if(cand <= n && res < cand)
					res = cand;
			}
		}

		cout << "Case #" << Case << ": ";
		cout << res << endl;
	}

	return 0;
}
