#include <iostream>
#include <algorithm>
#include <vector>
#include <string>
#include <fstream>
#include <map>
using namespace std;

int main()
{
	ifstream cin("in.txt");
	ofstream cout("out.txt");

	int t;
	cin >> t;
	for (int f = 0; f < t; ++f)
	{
		long long n, k;
		cin >> n >> k;

		long long cur = 1;

		map<long long, long long> now, temp;
		temp[n / 2] += 1;
		temp[(n - 1) / 2] += 1;
		now[n] = 1;

		while (k - cur > 0)
		{
			k -= cur;
			now = temp;

			cur = 0;
			temp.clear();
			for (auto v : now)
			{
				cur += v.second;
				temp[v.first / 2] += v.second;
				temp[(v.first - 1) / 2] += v.second;
			}
		}

		auto ss = *now.rbegin();
		auto ff = *now.begin();

		cout << "Case #" << f + 1 << ": ";
		if (ss.second >= k)
			cout << ss.first / 2 << ' ' << (ss.first-1) / 2;
		else
			cout << ff.first / 2 << ' ' << (ff.first-1) / 2;
		cout << endl;
		
	}
	return 0;
}