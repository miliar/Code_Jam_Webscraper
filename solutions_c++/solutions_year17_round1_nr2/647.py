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

bool stillhas(int n, const vector<vector<pair<int,int>>> & s)
{
	FORi(i,n) if (s[i].size() == 0) return false;
	return true;
}

int solve_case(int n, int p, vector<int> r, vector<vector<int>> q, ostream & out)
{
	vector<vector<pair<int,int>>> s(n); //servings
	FORi(i,n) {
		FORi(j,p) {
			int mins = (q[i][j]*10 + r[i]*11 - 1)/(r[i]*11);
			int maxs = (q[i][j]*10)/(r[i]*9);
			// out << mins << ' ' << maxs << "   ";
			mins = max(1,mins); // si es 0 no sirve
			if (mins <= maxs) s[i].push_back(make_pair(mins,maxs));
		}
		// out << endl;
		sort(s[i].begin(), s[i].end());
	}
	
	int result = 0;
	while (stillhas(n,s)) {
		int maxs = 0, maxsi = -1;
		int maxmins = s[0].back().first;
		int minmaxs = s[0].back().second;
		FORi(i,n) {
			if (maxmins < s[i].back().first) {
				maxmins = s[i].back().first;
			}
			if (minmaxs > s[i].back().second) {
				minmaxs = s[i].back().second;
			}
			if (maxs < s[i].back().second) {
				maxs = s[i].back().second;
				maxsi = i;
			}
		}
		// out << maxmins << ' ' <<  minmaxs << endl;
		if (maxmins <= minmaxs) {
			++result;
			FORi(i,n) {
				s[i].pop_back();
			}
		} else { // minmaxs < maxmins
			FORi(i,n) {
				while (!s[i].empty() && minmaxs < s[i].back().first)
					s[i].pop_back();
			}
		}
	}
	
	return result;
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
		vector<int> r(n);
		FORi(i,n) in >> r[i];
		vector<vector<int>> q(n, vector<int>(p));
		FORi(i,n) FOR(j,p) in >> q[i][j];

		int result = solve_case(n, p, move(r), move(q), out);
		out << "Case #" << t << ": " << result << endl;
	}
}


int main()
{
	// ifstream in("B-sample.in");
	// ofstream out("B-sample-out.txt");

	// ifstream in("B-small-attempt0.in");
	// ofstream out("B-small-attempt0-out.txt");

	ifstream in("B-large.in");
	ofstream out("B-large-out.txt");

	solve(in,out);

	return 0;
}
