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

	ifstream fin("A-large (1).in");
	ofstream fout("out.txt");
	fin >> T;
	REP(t, T) {
		int n;
		double dest;
		fin >> dest;
		fin >> n;
		double maxtime = 0.0;
		for (int i = 0; i < n; i++) {
			double pos, speed;
			fin >> pos >> speed;
			maxtime = max((dest - pos) / speed, maxtime);
		}
		fout.precision(15);
		fout << "Case #" << t + 1 << ": " << dest / maxtime << "\n";
	}
	fout.close();
	fin.close();
	return 0;
}