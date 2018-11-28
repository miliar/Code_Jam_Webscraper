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

#define FILE_NAME "A-large"

using namespace std;

int main()
{
	freopen(FILE_NAME ".in", "r", stdin);
	freopen(FILE_NAME ".out", "w", stdout);
	
	int numTestCaces = 0;
	cin >> numTestCaces;
	for(int Case = 1; Case <= numTestCaces; ++Case)
	{
		double d;
		int n;
		cin >> d >> n;
		double k, s;
		double maxt = 0;
		for(int i = 0; i < n; ++i)
		{
			cin >> k >> s;
			maxt = max(maxt, (d - k) / s);
		}
		double res = d / maxt;
		cout << "Case #" << Case << ": ";
		printf("%.6f\n", res);
	}

	return 0;
}
