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

	ifstream fin("C-small-2-attempt0.in");
	ofstream fout("out.txt");
	fin >> T;
	REP(t, T) {
		uint64_t k, n;
		fin >> n >> k;

		map<uint64_t, int> ranges;
		ranges[n] = 1;
		k--;

		for (uint64_t i = 0; i < k; i++) {
			auto it = ranges.rbegin();
			auto Ls = (it->first - 1) / 2;
			auto Rs = Ls + (it->first - 1) % 2;

			ranges[Ls]++;
			ranges[Rs]++;

			it->second--;
			if (it->second == 0) {
				ranges.erase(it->first);
			}
		}

		auto it = ranges.rbegin();
		auto Ls = (it->first - 1) / 2;
		auto Rs = Ls + (it->first - 1) % 2;

		fout << "Case #" << t + 1 << ": " << max(Ls, Rs) << " " << min(Ls, Rs) << endl;
	}
	fout.close();
	fin.close();
	return 0;
}