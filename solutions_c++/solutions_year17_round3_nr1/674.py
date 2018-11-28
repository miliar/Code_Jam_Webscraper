#include <iostream>
#include <algorithm>
#include <vector>
#include <set>
#include <string>
#include <map>
#include <stack>
#include <queue>
#include <cmath>
#include <fstream>
#include <iomanip>
#include <cstring>

using namespace std;

const long double PI = 3.14159265358979323846;

int main()
{
	freopen("input.txt", "r", stdin);
	freopen("output.txt", "w", stdout);
	int t;
	cin >> t;
	for (int c = 0; c < t; c++) {
		int n, k, r, h;
		cin >> n >> k;
		vector<pair<long long, long long> > v(n);
		for (int i = 0; i < n; i++) {
			cin >> v[i].first >> v[i].second;
		}
		sort(v.begin(), v.end());
		multiset<pair<long long, int> > mins;
		long double hgs = 0, res = 0;
		for (int i = 0; i < k - 1; i++)
			mins.insert({ 2 * v[i].second * v[i].first, i });
		for (int i = k - 1; i < n; i++) {
			long double tmp = 0;
			for (auto j = mins.begin(); j != mins.end(); j++) {
				tmp += (*j).first;
			}
			mins.insert({ 2 * v[i].second * v[i].first, i });
			mins.erase(mins.begin());
			tmp += v[i].second * 2 * v[i].first;
			tmp += v[i].first * v[i].first;
			tmp *= PI;
			if (tmp > res)
				res = tmp;
		}
		cout << "Case #" << c + 1 << ": " << fixed << setprecision(9) << res << endl;
	}
	return 0;
}
