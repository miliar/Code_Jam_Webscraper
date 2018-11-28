#include <algorithm>
#include <iostream>
#include <sstream>
#include <string>
#include <utility>
#include <vector>
#include <cmath>
#include <map>
using namespace std;
#define VT vector
typedef VT<int> VI;
typedef VT<VI> VVI;
typedef VT<string> VS;
typedef VT<double> VD;
#define REP(i,n) for(int _n=n, i=0;i<_n;++i)
#define FOR(i,a,b) for(int i=(a),_b=(b);i<=_b;++i)
#define ALL(c) c.begin(),c.end()
#define PB push_back
#define MP make_pair
#define FS first
#define SC second
#define SZ size() 


long long solve(long long n, long long k)
{

	map<long long, long long> m;

	m[n] = 1;

	while (k > 0)
	{
		auto last = m.end();
		--last;

		long long cnt = last->second;
		if (cnt < k)
		{
			long long p = last->first;

			m.erase(last);

			if (p % 2 == 1 && p > 1)
			{
				m[p / 2] += (cnt * 2);
			}
			else
			{
				m[p / 2] += cnt;
				m[p / 2 - 1] += cnt;
			}

		}
		else
		{
			return last->first;
		}

		k -= cnt;
	}



}


// BEGIN CUT HERE
int main(int argc, char* argv[])
{

	freopen("in.txt", "r", stdin);
	freopen("out.txt", "w", stdout);


	int T;
	cin >> T;

	REP(t, T)
	{
		long long n, k;
		cin >> n>>k;

		long long mn, mx;
		long long s = solve(n, k);
		if (s % 2 == 1)
			mn = mx = s / 2;
		else
		{
			mn = s / 2 - 1;
			mx = s / 2;
		}



		cout << "Case #" << (t + 1) << ": " << mx << " " << mn << endl;
		cerr << "Case #" << (t + 1) << ": " << mx << " " << mn << endl;

	}


}
// END CUT HERE
