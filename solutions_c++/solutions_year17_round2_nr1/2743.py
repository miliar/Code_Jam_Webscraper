
#define _CRT_SECURE_NO_WARNINGS



#include <iostream>
#include <cstdio>
#include <algorithm>
#include <cstring>
#include <string>
#include <cctype>
#include <stack>
#include <queue>
#include <deque>
#include <unordered_map>
#include <list>
#include <vector>
#include <map>
#include <set>
#include <sstream>
#include <cmath>
#include <bitset>
#include <utility>
#include <numeric>
#include <ctime>
#include <functional>
#include <stdio.h>
#include <fstream>
#include <cstdlib>

using namespace std;

typedef long long ll;
typedef pair<int, int> pi;
typedef pair<ll, ll> pll;

#define mp              make_pair
#define pb              push_back
#define INF             1<<30
#define avg(x, y)       (x + y)/2

#define fr(i, a)        for( int i = (0); i < (a); i++ )
#define fi(i, sz)       for( size_t i = 0; i < sz.size (); i++ )
#define fe(i, x)        for(typeof (x.begin()) i = x.begin(); i != x.end (); i++)
#define set(a, s)       memset(a, s, sizeof (a))
#define x				first
#define y				second

inline ll power(int b, int p) { ll ret = 1; for (int i = 1; i <= p; i++) ret *= b; return ret; }

void split(const string &s, char delim, vector<string> &elems) {
	stringstream ss;
	ss.str(s);
	string item;
	while (getline(ss, item, delim)) {
		elems.push_back(item);
	}
}

vector<string> split(const string &s, char delim) {
	vector<string> elems;
	split(s, delim, elems);
	return elems;
}

/* END TEMPLATE */

#define FILE_MODE

int main(int argc, const char ** argv)
{
	string file("A-large (1)");
#ifdef FILE_MODE
	ifstream def_fin(file + ".in");
	ofstream def_fout(file + ".out");
#else
	istream &def_fin = cin;
	ostream &def_fout = cout;
#endif
	istream &i = def_fin;
	ostream &o = def_fout;
	o << fixed;
	int T;
	i >> T;

	for(int t = 0; t < T; t++)
	{
		int D, N;
		i >> D >> N;
		double max_time = -INF;
		for(int n = 0; n < N; n++)
		{
			int ki, si;
			i >> ki >> si;
			double atime = 1.0 * (D - ki) / si;
			max_time = max(atime, max_time);
		}
		double spd = D / max_time;
		o << "Case #" << (t + 1) << ": ";
		o << spd << endl;
	}
	return 0;
}