#include <map>
#include <set>
#include <list>
#include <cmath>
#include <ctime>
#include <deque>
#include <queue>
#include <stack>
#include <string>
#include <bitset>
#include <cstdio>
#include <limits>
#include <vector>
#include <climits>
#include <cstring>
#include <cstdlib>
#include <fstream>
#include <numeric>
#include <sstream>
#include <iostream>
#include <algorithm>
#include <unordered_map>
#include <unordered_set>
#include <cctype>
#include <utility>
#include <exception>
using namespace std;  // since cin and cout are both in namespace std, this saves some text

class Round1A {
public:
	double speed(vector<pair<double, double>>& horse, double de) {
		double mtm = 0;
		for (auto e:horse) {
			double tm = (de-e.first)/e.second;
			mtm = max(mtm, tm);
		}
		return de/mtm;
	}
};

int main() {
	int t;
	cin >> t;  // read t. cin knows that t is an int, so it reads it as such.
	cin.ignore();
	Round1A round1;
	for (int i = 1; i <= t; ++i) {
		double de = 0;
		int ho = 0;
		cin >> de >> ho;
		cin.ignore();
		vector<pair<double, double>> horse;
		for (int r = 0; r < ho; ++r) {
			double ki=0, si=0;
			cin >> ki >> si;
			cin.ignore();
			horse.push_back(make_pair(ki,si));
		}
		printf("Case #%d: %.6f\n", i, round1.speed(horse, de));
//		cout << "Case #" << i << ": " << round1.speed(horse, de) << endl;
	}
}
