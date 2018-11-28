#include <cstdio>
#include <algorithm>
#include <vector>
#include <cstring>
#include <numeric>
#include <cassert>
#include <cmath>
#include <map>
#include <set>
#include <iostream>
#include <ctime>

using namespace std;

#define FOR(k,a,b) for(int k(a); k < int(b); ++k)
#define REP(k,a) for(int k=0; k < int(a); ++k)
#define ABS(a) ((a)>0?(a):-(a))
#define EPS 1e-9
typedef long long LL;
const LL MOD = 1e9 + 7;
const int INF = 1e9 + 1;

int main(int argc, char** argv) {
#ifdef HOME
	freopen("A-large.in", "rb", stdin);
	freopen("A-large.out", "wb", stdout);
#endif
	int T,N,ans;
	string s;
	cin >> T;
	FOR(tc, 1, T + 1)
	{
		cin >> s >> N;
		ans = 0;
		REP(i, s.size())
		{
			if (s[i] == '-')
			{
				++ans;
				REP(j, N)
				{
					if (i + j < s.size())
					{
						s[i + j] = (s[i + j] == '-') ? '+' : '-';
					}
					else
					{
						ans = -1;
						break;
					}
				}
			}
			if(ans == -1)
				break;
		}
		cout << "Case #" << tc << ": ";
		if (ans == -1)
		{
			cout << "IMPOSSIBLE" << endl;
		}
		else
		{
			cout << ans << endl;
		}
	}
	return 0;
}
