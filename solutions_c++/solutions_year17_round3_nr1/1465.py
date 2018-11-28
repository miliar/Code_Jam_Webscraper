#include <iostream>
#include <string>
#include <cmath>
#include <queue>
#include <stack>
#include <set>
#include <map>
#include <iterator>
#include <functional>
#include <vector>
#include <algorithm>

#define M_PI       3.14159265358979323846

//#pragma comment(linker, "/STACK:160777216")

using namespace std;

struct {
	bool operator()(pair<int, int> a, pair<int, int> b)
	{
		return (long long)a.first * a.second > (long long)b.first * b.second;
	}
} customLess;

void solve()
{
	int n, k; cin >> n >> k;
	vector<pair<int, int> > rh(n);
	for (int i = 0; i < n; ++i)
		cin >> rh[i].first >> rh[i].second;

	std::sort(rh.begin(), rh.end(), customLess);

	double bestR = 0;
	double s = 0;

	for (int i = 0; i < k - 1; ++i)
	{
		s += (double)rh[i].first * rh[i].second;
		bestR = max(bestR, (double)rh[i].first);
	}

	double sP = s * 2 * M_PI;

	double s1 = sP + M_PI * bestR * bestR;

	double bestS = 0;

	for (int i = k - 1; i < n; ++i)
	{
		double curS1 = s1 + 2 * M_PI * rh[i].first * rh[i].second;
		double curS2 = sP + 2 * M_PI * rh[i].first * rh[i].second + M_PI * rh[i].first * rh[i].first;

		bestS = max(bestS, max(curS1, curS2));
	}

	printf("%.9f\n", bestS);
}

int main()
{
	//freopen("i:/input.txt", "rt", stdin);
	//freopen("i:/input.out", "wt", stdout);

	int T; cin >> T;
	for (int t = 1; t <= T; ++t)
	{
		cout << "Case #" << t << ": ";
		solve();
	}
	return 0;
}