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
const char HAPPY = '+';
const char PLAIN = '-';

void solve_case(int r, int c, vector<string> & k)
{
	const string all(c,'?');
	int FIRST = -1;
	int PREV = -1;
	FOR(i,r) {
		char prev = '?';
		int first = -1;
		FOR(j,c) {
			if (k[i][j] != '?') {
				prev = k[i][j];
				if (first == -1) first = j;
			} else {
				if (prev != '?') k[i][j] = prev;
			}
		}
		if (first > 0) FOR(j,first) k[i][j] = k[i][first];
		if (first != -1) {
			PREV = i;
			if (FIRST == -1) FIRST = i;
		} else {
			if (PREV != -1) k[i] = k[PREV];
		}
	}
	if (FIRST != -1)
		FOR(i,FIRST) k[i] = k[FIRST];
	return;
}

void solve(istream & in, ostream & out)
{
	int TC_NCases;
	in >> TC_NCases;
	out.precision(18);
	out.setf(std::ios_base::fixed, std::ios_base::floatfield);
	for (int t = 1; t <= TC_NCases; ++t)
	{
		int r, c;
		in >> r >> c;
		vector<string> k(r);
		FORi(i,r) {
			in >> k[i];
			assert(k[i].size() == c);
		}

		solve_case(r, c, k);
		out << "Case #" << t << ": " << endl;
		output(out, k);
	}
}


int main()
{
	// ifstream in("A-sample.in");
	// ofstream out("A-sample-out.txt");

	// ifstream in("A-small-attempt0.in");
	// ofstream out("A-small-attempt0-out.txt");

	ifstream in("A-large.in");
	ofstream out("A-large-out.txt");

	solve(in,out);

	return 0;
}
