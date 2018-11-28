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

struct  pancake
{
	double rh;
	double r;
};

bool cmp(const pancake& op1, const pancake& op2) {
	return op1.rh > op2.rh;
}

int main(void) {
	int T;

	ifstream fin("A-large.in");
	ofstream fout("out.txt");
	fin >> T;
	REP(t, T) {
		int n, k;
		fin >> n >> k;
		vector<pancake> p;

		for (int i = 0; i < n; i++) {
			pancake pc;
			double r, h;
			fin >> r >> h;
			pc.r = 3.1415926535897932384626433832795 * r * r;
			pc.rh = 2.0 * 3.1415926535897932384626433832795 * r * h;
			p.push_back(pc);
		}

		sort(p.begin(), p.end(), cmp);
		double sure = 0.0;
		double ans1 = 0.0;
		for (int i = 0; i < k - 1; i++) {
			if (p[i].r > ans1) ans1 = p[i].r;
			sure += p[i].rh;
		}
		ans1 = ans1 + sure + p[k - 1].rh;
		double ans2 = 0.0;
		for (int i = k - 1; i < n; i++) {
			if (p[i].r + p[i].rh > ans2) {
				ans2 = p[i].r + p[i].rh;
			}
		}
		ans2 += sure;
		if (ans2 > ans1) ans1 = ans2;
		fout << "Case #" << t + 1 << ": " << std::setprecision(20) << ans1 << "\n";
	}
	fout.close();
	fin.close();
	return 0;
}