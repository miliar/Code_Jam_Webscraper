#include <iostream>
#include <fstream>
#include <cassert>
#include <vector>
#include <string>
#include <map>
#include <set>
#include <algorithm>
#include <numeric>
#include <queue>
#include <cmath>
//download TTMath from http://www.ttmath.org/
//#include <ttmath/ttmath.h>
#undef max
#undef min

using namespace std;
//using namespace ttmath;
//typedef Int<100> num;

#define metafor(iter,container) \
	for ((iter) = (container).begin(); (iter) != (container).end(); ++(iter))
#define FOR(i,n) for (size_t i = 0; i < (n); ++i)
#define FORi(i,n) for (int i = 0; i < (n); ++i)
template<class C>
void show(const C & v) { FOR(i,v.size()) cout << v[i] << ' '; cout << endl; }
template<class C>
void output(ostream & out, const C & v) { FOR(i,v.size()) out << v[i] << endl; }

const long long IMPOSSIBLE = -1;

int solve_case(int n, int p, vector<int> g)
{
	assert(p >= 2);
	FORi(i,n) g[i] = g[i] % p;
	if (p == 2) {
		int k[2] = {};
		FORi(i,n) ++k[g[i]];
		// cout << k[0] << endl;
		// cout << k[1] << endl;
		// cout << endl;
		return k[0] + k[1]/2 + (k[1]%2);
	} else if (p == 3) {
		int k[3] = {};
		FORi(i,n) ++k[g[i]];
		// cout << k[0] << endl;
		// cout << k[1] << endl;
		// cout << k[2] << endl;
		// cout << endl;
		int a = min(k[1],k[2]);
		int b = max(k[1],k[2]) - a;
		int c = (b%3 == 0)?0:1;
		return k[0] + a + b/3 + c;
	} else if (p == 4) {
		int k[4] = {};
		FORi(i,n) ++k[g[i]];
		// cout << k[0] << endl;
		// cout << k[1] << endl;
		// cout << k[2] << endl;
		// cout << k[3] << endl;
		// cout << endl;
		int a = min(k[1],k[3]);
		int b = max(k[1],k[3]) - a; // sobrante
		int c;
		if (k[2] % 2 == 0) 
			c = ((b % 4 == 0) ? 0 : 1);
		else
			if (b%4 < 2) c = 1;
			else if (b%4 == 2) c = 1;
			else c = 2;
		return k[0] + a + k[2]/2 + b/4 + c;
	} else assert(false);
	return -1;
}

void solve(istream & in, ostream & out)
{
	int TC_NCases;
	in >> TC_NCases;
	out.precision(18);
	out.setf(std::ios_base::fixed, std::ios_base::floatfield);
	for (int t = 1; t <= TC_NCases; ++t)
	{
		int n, p;
		in >> n >> p;
		vector<int> g(n);
		FORi(i,n) {
			in >> g[i];
		}

		auto result = solve_case(n, p, move(g));
		out << "Case #" << t << ": " << result << endl;
	}
}


int main()
{
	// ifstream in("A-sample.in");
	// ofstream out("A-sample-out.txt");
	// ifstream in("A-mysample.in");
	// ofstream out("A-mysample-out.txt");

	// ifstream in("A-small-attempt0.in");
	// ofstream out("A-small-attempt0-out.txt");

	ifstream in("A-large.in");
	ofstream out("A-large-out.txt");

	solve(in,out);

	return 0;
}
