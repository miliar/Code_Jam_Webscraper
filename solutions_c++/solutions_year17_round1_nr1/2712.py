#include <algorithm>
#include <iostream>
#include <sstream>
#include <string>
#include <utility>
#include <vector>
#include <cmath>
#include <map>
#include <set>

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

int cnt(VS&f, int r1, int c1, int r2, int c2)
{
	set<int> st;
	FOR(i, r1, r2)
	{
		FOR(j, c1, c2)
		{
			if (f[i][j] != '?')
			{
				st.insert(f[i][j]);
			}
		}
	}
	return st.size();

}

void fill(VS&f, int r1, int c1, int r2, int c2)
{
	if (r1 > r2)
		return;
	if (c1 > c2)
		return;

	FOR(i, r1, r2)
	{
		FOR(j, c1, c2)
		{
			if (f[i][j] != '?')
			{
				int ch = f[i][j];

				if (cnt(f, r1, c1, r2, c2) == 1)
				{
					FOR(i, r1, r2)
					{
						FOR(j, c1, c2)
						{
							f[i][j] = ch;
						}
					}

					return;
				}
				else if (cnt(f, r1, j+1, i, c2) == 0)
				{
					FOR(p, r1, i)
					{
						FOR(k, c1, c2)
						{
							f[p][k] = ch;
						}
					}

					fill(f, i + 1, c1, r2, c2);
					
					return;
				}
				else if (cnt(f, i+1, c1, r2, j) == 0)
				{
					FOR(p, r1, r2)
					{
						FOR(k, c1, j)
						{
							f[p][k] = ch;
						}
					}

					fill(f, r1, j+1, r2, c2);

					return;
				}
				else
				{
					FOR(p, r1, i)
					{
						FOR(k, c1, j)
						{
							f[p][k] = ch;
						}
					}

					fill(f, r1, j+1, i, c2);
					fill(f, i + 1, c1, r2, c2);

					return;
				}

			}
		}
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
		int R, C;
		cin >> R >> C;

		VS f(R);

		REP(r, R)
			cin >> f[r];

		fill(f, 0, 0, R - 1, C - 1);

		cout << "Case #" << (t + 1) << ":" << endl;
		cerr << "Case #" << (t + 1) << ":" << endl;
		REP(r, R)
		{
			cout << f[r] << endl;
			cerr << f[r] << endl;
		}
	}


}
// END CUT HERE
