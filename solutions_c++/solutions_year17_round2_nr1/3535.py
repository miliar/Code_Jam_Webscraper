#include <iostream>
#include <tuple>
#include <sstream>
#include <cmath>
#include <ctime>
#include <cassert>
#include <cstdio>
#include <vector>
#include <queue>
#include <stack>
#include <set>
#include <unordered_set>
#include <map>
#include <unordered_map>
#include <fstream>
#include <cstdlib>
#include <string>
#include <cstring>
#include <algorithm>
#include <numeric>
#include <memory>
#include <array>
#include <iomanip>

using namespace std;

double solve(int d, int n, vector<pair<double, double> > &locspeeds)
{
	//sort(locspeeds.begin(), locspeeds.end(),
	//	[](const pair<double, double> &a, const pair<double, double> &b) { return a.first > b.first; });

	double maxtime = 0;
	for (auto it = locspeeds.begin(); it != locspeeds.end(); ++it) {
		double loc = it->first;
		double speed = it->second;
		double mintime = (d - loc) / speed;
		maxtime = max(mintime, maxtime);

		//if (mintime > maxtime) {
		//	maxtime = mintime;
		//} else {
		//	double time = (d - loc) / speed;
		//}
		////maxtime = max(time, maxtime);
	}


    return d / maxtime;
}

int main(int argc, char *argv[])
{
    if (argc > 1) freopen(argv[1], "r", stdin);
    if (argc > 2) freopen(argv[2], "w", stdout);

    int numCases;
    cin >> numCases;

    int casei = 0;
    int d, n;
    while (++casei, cin >> d >> n) {

		vector<pair<double, double> > locspeeds(n);
		for (int i = 0; i < n; ++i) {
			cin >> locspeeds[i].first >> locspeeds[i].second;
		}

        cout << "Case #" << casei << ": ";

		cout << setprecision(17) << fixed << solve(d, n, locspeeds);

        cout << endl;
    }

    return 0;
}