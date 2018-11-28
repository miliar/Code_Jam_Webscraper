#include <vector>
#include <list>
#include <map>
#include <set>
#include <deque>
#include <queue>
#include <stack>
#include <bitset>
#include <algorithm>
#include <functional>
#include <numeric>
#include <utility>
#include <sstream>
#include <iostream>
#include <fstream>
#include <iomanip>
#include <cstdio>
#include <cmath>
#include <cstdlib>
#include <cctype>
#include <string>
#include <cstring>
#include <cstdio>
#include <cmath>
#include <cstdlib>
#include <ctime>

using namespace std;

#define FOR(i, a, b) for (int i(a), _b(b); i <= _b; ++i)
#define REP(i, n) for (int i(0), _n(n); i < _n; ++i)

int main(void) {
	int T;

	ifstream fin("B-small-attempt1.in");
	ofstream fout("out.txt");
	fin >> T;
	REP(t, T) {
		int ac, aj;
		fin >> ac >> aj;
		vector<pair<int, int> > acs, ajs;
		acs.resize(ac);

		for (int i = 0; i < ac; i++) {
			fin >> acs[i].first >> acs[i].second;
		}

		ajs.resize(aj);

		for (int i = 0; i < aj; i++) {
			fin >> ajs[i].first >> ajs[i].second;
		}

		sort(acs.begin(), acs.end());
		sort(ajs.begin(), ajs.end());

		int ans = 0;

		if ((ac == 1) || (aj == 1)){
			ans = 2;
		}
		else {
			if (ac == 2) {
				if (acs[1].second - acs[0].first > 720) {
					if (acs[0].second + 24 * 60 - acs[1].first > 720) {
						ans = 4;
					}
					else {
						ans = 2;
					}
				}
				else {
					ans = 2;
				}
			}
			else {
				if (ajs[1].second - ajs[0].first > 720) {
					if (ajs[0].second + 24 * 60 - ajs[1].first > 720) {
						ans = 4;
					}
					else {
						ans = 2;
					}
				}
				else {
					ans = 2;
				}
			}
		}

		fout << "Case #" << t + 1 << ": " << ans << "\n";
	}
	fout.close();
	fin.close();
	return 0;
}