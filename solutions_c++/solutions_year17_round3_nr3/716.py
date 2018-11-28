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

	ifstream fin("C-small-1-attempt0.in");
	ofstream fout("out.txt");
	fin >> T;
	REP(t, T) {
		int n, k;
		fin >> n >> k;
		double u;
		fin >> u;
		vector<double> p;
		p.resize(n);
		for (int i = 0; i < n; i++) {
			fin >> p[i];
		}

		sort(p.begin(), p.end());

		double nextgreater = 0.0;
		int ng = 1;
		while ((u > 0) && (ng < n))
		{
			nextgreater = p[ng];
			double diff = nextgreater - p[0];
			diff *= (double)ng;
			if (diff > u) diff = u;
			u -= diff;
			diff /= (double)ng;
			for (int i = 0; i < ng; i++) {
				p[i] += diff;
			}
			ng++;
		}

		double ans = 1.0;
		for (auto& prob : p) {
			prob += u / ((double)p.size());
			if (prob > 1.0) prob = 1.0;
			ans *= prob;
		}

		fout << "Case #" << t + 1 << ": " << setprecision(20) << ans << "\n";
	}

	fout.close();
	fin.close();
	return 0;
}