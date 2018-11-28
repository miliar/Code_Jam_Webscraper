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
//template<class C>
//void show(const C & v) { FOR(i,v.size()) cout << v[i] << ' '; cout << endl; }


pair<long long, long long> solve_case(long long n, long long k)
{
	if (k == 1) return make_pair( n-1-(n-1)/2, (n-1)/2 );
	
	long long m = 1;
	while (2*m+1 < k) m = 2*m+1;
	assert(1 <= m && m < k && k <= n);
	
	long long r = (n-m) % (m+1);
	long long q = (n-m) / (m+1);
	assert(n == (m+1)*q + m + r);
	if (k - m <= r) return solve_case(q+1,1);
	else return solve_case(q,1);
}

void solve(istream & in, ostream & out)
{
	int TC_NCases;
	in >> TC_NCases;
	out.precision(18);
	out.setf(std::ios_base::fixed, std::ios_base::floatfield);
	for (int t = 1; t <= TC_NCases; ++t)
	{
		long long n, k;
		in >> n >> k; assert(1 <= k && k <= n);

		auto result = solve_case(n, k);
		out << "Case #" << t << ": " << result.first << ' ' << result.second << endl;
	}
}


int main()
{
	// for (int n = 1; n < 100; ++n) {
		// cout << n << ": ";
		// for (int k = 1; k <= n && k < 20; ++k)
			// cout << solve_case(n,k).second << ' ';
		// cout << '\n';
	// }
		// cout << '\n';
	// for (int n = 1; n < 100; ++n) {
		// cout << n << ": ";
		// for (int k = 1; k <= n && k < 20; ++k)
			// cout << solve_case(n,k).first << ' ';
		// cout << '\n';
	// }
	// cout << endl;
	// ifstream in("C-sample.in");
	// ofstream out("C-sample-out.txt");

	// ifstream in("C-small-1-attempt0.in");
	// ofstream out("C-small-1-attempt0-out.txt");

	// ifstream in("C-small-2-attempt0.in");
	// ofstream out("C-small-2-attempt0-out.txt");

	ifstream in("C-large.in");
	ofstream out("C-large-out.txt");

	solve(in,out);

	return 0;
}
