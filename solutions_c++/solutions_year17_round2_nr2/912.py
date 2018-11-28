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

	ifstream fin("B-large (1).in");
	ofstream fout("out.txt");
	fin >> T;

	map<char, int> cbyn;
	char clr[] = "-RYOBVG";
	for (int i = 0; i < 7; i++) {
		cbyn[clr[i]] = i;
	}

	REP(t, T) {
		int n;
		fin >> n;
		//int red, orange, yellow, green, blue, violet;
		vector<int> colors, scolors;
		
		colors.resize(8, -1);
		scolors.resize(5, -1);
		
		fin >> colors[1];
		fin >> colors[1 | 2];
		fin >> colors[2];
		fin >> colors[4 | 2];
		fin >> colors[4];
		fin >> colors[1 | 4];

		scolors[1] = colors[1] + colors[1 | 4] + colors[1 | 2];
		scolors[2] = colors[2] + colors[1 | 2] + colors[4 | 2];
		scolors[4] = colors[4] + colors[1 | 4] + colors[4 | 2];
		
		/*vector<bool> complex(8, false);
		complex[1 | 2] = true;
		complex[4 | 2] = true;
		complex[1 | 4] = true;*/

		std::string ret;
		int last = 0;
		int first = 0;
		for(int s = 0; s < n; s++) {
			int maxclr = -1;
			int maxi = -1;
			for (int i = 0; i < colors.size(); i++) {
				if (colors[i] <= 0) continue;
				if (!(i & last)) {
					int curpwr = 0;
					if (i & 1) curpwr += scolors[1];
					if (i & 2) curpwr += scolors[2];
					if (i & 4) curpwr += scolors[4];

					if (maxclr == curpwr) {
						if (i & first) {
							maxi = i;
							maxclr = curpwr;
						}
					}
					if (maxclr < curpwr) {
						maxi = i;
						maxclr = curpwr;
					}
				}
			}
			if (maxi < 0) {
				ret = "IMPOSSIBLE";
				break;
			}
			ret += clr[maxi];
			colors[maxi]--;
			if (maxi & 1) scolors[1]--;
			if (maxi & 2) scolors[2]--;
			if (maxi & 4) scolors[4]--;

			last = maxi;
			if (s == 0) {
				first = last;
			}
		}

		if (cbyn[ret.back()] & cbyn[ret.front()]) ret = "IMPOSSIBLE";

		fout << "Case #" << t + 1 << ": " << ret << "\n";
	}
	fout.close();
	fin.close();
	return 0;
}