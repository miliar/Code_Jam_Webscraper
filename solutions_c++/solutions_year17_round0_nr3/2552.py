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

#define FILE_NAME "C-large"

using namespace std;

int main()
{
	freopen(FILE_NAME ".in", "r", stdin);
	freopen(FILE_NAME ".out", "w", stdout);
	
	int numTestCaces = 0;
	cin >> numTestCaces;
	for(int Case = 1; Case <= numTestCaces; ++Case)
	{
		long long n, k;
		cin >> n >> k;
		int cnt = 0;
		long long kk = k;
		while(kk > 0)
		{
			kk >>= 1;
			++cnt;
		}
		--cnt;
		long long seg = 1 << cnt;
		n -= seg - 1;
		long long len = n / seg - 1;
		if(n % seg >= (k - seg + 1))
			++len;

		cout << "Case #" << Case << ": ";
		if(len % 2 == 0)
			cout << len / 2 << ' ' << len / 2 << endl;
		else
			cout << len / 2 + 1 << ' ' << len / 2 << endl;
	}

	return 0;
}
