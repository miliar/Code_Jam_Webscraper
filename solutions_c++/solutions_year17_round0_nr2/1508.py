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

#define metafor(iter,container) \
	for ((iter) = (container).begin(); (iter) != (container).end(); ++(iter))
#define FOR(i,n) for (size_t i = 0; i < (n); ++i)
#define FORi(i,n) for (int i = 0; i < (n); ++i)
template<class C>
void show(const C & v) { FOR(i,v.size()) cout << v[i] << ' '; cout << endl; }
ostream& operator<<(ostream& os, const vector<int> & v)
{
	FOR(i, v.size()) os << ' ' << v[i] ;
	return os;
}

#define FFOR(i,j,n) FOR(i,2*(n)-1) FOR(j,n)

string solve_case(string s)
{
	const size_t n = s.size();
	assert(n >= 1);

	if (n <= 1) return s;

	assert(s[0] != '0');

	string rr; rr += s[n - 1];
	for (int i = n - 2; i >= 0; --i) {
		if (s[i] <= rr.back()) rr += s[i];
		else { assert(s[i] != 0); rr = string(rr.size(), '9') + static_cast<char>(s[i] - 1); }
	}
	int zeros = 0;
	while (rr.back() == '0') {
		++zeros;
		rr.pop_back();
	}
	reverse(rr.begin(), rr.end());
	assert(is_sorted(rr.begin(), rr.end()));

	return rr;
}

void solve(istream & in, ostream & out)
{
	int TC_NCases;
	in >> TC_NCases;
	out.precision(18);
	out.setf(std::ios_base::fixed, std::ios_base::floatfield);
	for (int t = 1; t <= TC_NCases; ++t)
	{
		string s;
		in >> s;

		string result = solve_case(move(s));
		out << "Case #" << t << ": " << result << endl;
	}
}


int main()
{
	//ifstream in("B-sample.in");
	//ofstream out("B-sample-out.txt");

	//ifstream in("B-small-attempt0.in");
	//ofstream out("B-small-attempt0-out.txt");

	ifstream in("B-large.in");
	ofstream out("B-large-out.txt");

	solve(in,out);

	return 0;
}
