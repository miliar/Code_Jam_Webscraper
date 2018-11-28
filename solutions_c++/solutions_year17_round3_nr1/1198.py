#define _CRT_SECURE_NO_DEPRECATE
#include<iostream>
#include<string>
#include<sstream>
#include<vector>
#include<deque>
#include<queue>
#include<stack>
#include<numeric>
#include<math.h>
#include<set>
#include<map>
#include<fstream>
#define epsilon 0.000000001
#define cosinusa(a, b, c) ((a * a + b * b - c * c) / (2.0 * a * b));
#define infi 1000000000
using namespace std;
const double pi = acos(0.0) * 2.0;
int main()
{
	freopen("google.in", "r", stdin);
	freopen("google.out", "w", stdout);
	int numTests;
	cin >> numTests;
	for(int testCounter = 0; testCounter < numTests; ++testCounter)
	{
		printf("Case #%d: ", testCounter + 1);
		int n, k;
		cin >> n >> k;
		vector<pair<long long, long long> > pancakes(n);
		for (int i = 0; i < n; i++) {
			cin >> pancakes[i].first >> pancakes[i].second;
		}

		sort(pancakes.rbegin(), pancakes.rend());
		long long surface = 0;
		long long maxsurface = 0;

		for (int i = 0; i < n; i++) {
			surface = 0;
			surface += pancakes[i].first * pancakes[i].first;
			surface += 2 * pancakes[i].second * pancakes[i].first;
			vector<pair<long long, long long> > heights;
			for (int j = i + 1; j < n; j++) {
				heights.push_back(make_pair(pancakes[j].second * pancakes[j].first, pancakes[j].first));
			}
			if (heights.size() < k - 1) {
				break;
			}
			sort(heights.rbegin(), heights.rend());
			for (int j = 0; j < k - 1; j++) {
				surface += 2 * heights[j].first;
			}
			maxsurface = max (maxsurface, surface);
		}

		double answer = maxsurface * pi;
		printf("%.9lf\n", answer);

	}
	return 0;
}


