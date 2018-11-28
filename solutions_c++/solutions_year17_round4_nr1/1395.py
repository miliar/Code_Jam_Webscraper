#include <cstring>
#include <cstdio>
#include <cmath>
#include <iostream>
#include <iomanip>
#include <string>
#include <vector>
#include <set>
#include <map>
#include <algorithm>

typedef long long int ll;
typedef unsigned long long int ull;

using namespace std;

template<class T1, class T2>
ostream& operator<< (ostream &os, pair<T1, T2> p) { return os << "(" << p.first << ", " << p.second << ")"; }

#define FOR(i, a, b) for (int i = (a); i < (b); ++i)
#define FORI(v) for (auto it = v.begin(); it != v.end(); ++it)

template<typename T> void _debug(const char* s, T x) { cerr << s << "=" << x <<"\n"; }
template<typename T, typename... TA> void _debug(const char* s, T h, TA... t) {
  while(*s != ',') cerr << *s++; cerr << "=" << h <<","; _debug(s+1, t...);
}
template <typename T> void _DEBUGC(string s, T v) {
	cerr << s << "=(";
	FORI(v) { if (it != v.begin()) cerr << ", "; cerr << *it; }
	cerr <<")\n";
}
#define DBG 0
#define DEBUG(...) if (DBG) _debug(#__VA_ARGS__, __VA_ARGS__)
#define DEBUGC(v) if (DBG) _DEBUGC(#v, v)

int main()
{
	int T;
	cin >> T;

	FOR(t, 1, T+1)
	{
		int N, P;
		cin >> N >> P;
		vector<int>	G(4);
		FOR(i, 0, N)
		{
			int g;
			cin >> g;
			G[g % P]++;
		}
		int result;
		DEBUGC(G);
		if (P == 2)
		{
			result = G[0] + (G[1] + 1) / 2;
		}
		else if (P == 3)
		{
			result = G[0] + min(G[1], G[2]) + (G[1] + G[2] - 2 * min(G[1], G[2]) + 2) / 3;
		}
		else if (P == 4)
		{

			result = G[0] + min(G[1], G[3]) + G[2] / 2;
			int r = max(G[1], G[3]) - min(G[1], G[3]);
			if (G[2] % 2)
			{
				result++;
				r -= 2;
			}
			if (r > 0)
				result += (r + 3) / 4;
		}
		cout << "Case #" << t << ": " << result << "\n";
	}
	
	return 0;
}

