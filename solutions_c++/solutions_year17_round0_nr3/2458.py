#include <map>
#include <set>
#include <list>
#include <cmath>
#include <ctime>
#include <deque>
#include <assert.h>
#include <queue>
#include <stack>
#include <string>
#include <bitset>
#include <cstdio>
#include <functional> 
#include <limits>
#include <vector>
#include <climits>
#include <cstring>
#include <tuple>
#include <cstdlib>
#include <fstream>
#include <numeric>
#include <sstream>
#include <iostream>
#include <algorithm>
#include <iomanip>
#include <unordered_map>
#include <unordered_set>

using namespace std;




class Compare
{
public:
	bool operator() (long long a, long long b)
	{
		return a > b;
	}
};

bool mycmp(pair <int, int> a, pair <int, int> b)
{
	if (a.first == b.first)
	{
		return a.second > b.second;
	}
	return a.first > b.first;
}


int main()
{
	ifstream cin("input.txt");
	ofstream cout("output.txt");
	int qqq;
	cin >> qqq;
	for (int qq = 1; qq <= qqq; qq++)
	{
		cout << "Case #" << qq << ": ";
		vector < tuple <long long, long long, long long > > ans;
		map <long long, long long > num;
		long long n, k;
		cin >> n >> k;
		num[(-1)*n] = 1;

		//set <long long, vector<long long>, greater<long long> > q;

		while (!num.empty())
		{
			pair <long long,long long> x = *num.begin();
			x.first = x.first * (-1);

			num.erase(num.begin());
			long long mid = (x.first + 1) / 2;

			long long u = mid - 1, uu = x.first - mid;
			if (u > uu)
				swap(u, uu);
			ans.push_back(make_tuple(uu, u, x.second));
			if (u > 0)
			{
				num[(-1)*u] += x.second;
			}
			if (uu > 0)
			{
				num[(-1)*uu] += x.second;
			}
		}
		int i = 0;
		while (k - get<2>(ans[i]) > 0)
		{
			k -= get<2>(ans[i]);
			i++;
		}
		cout << get<0>(ans[i]) << " " << get<1>(ans[i]) << endl;
		//cout << ans[k - 1].second << " " << ans[k-1].first << endl;


		

	}
	return 0;
}