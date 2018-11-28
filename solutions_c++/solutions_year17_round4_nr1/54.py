


                #include <string>
#include <vector>
#include <map>
#include <list>
#include <iterator>
#include <cassert>
#include <set>
#include <queue>
#include <iostream>
#include <sstream>
#include <stack>
#include <deque>
#include <cmath>
#include <memory.h>
#include <cstdlib>
#include <cstdio>
#include <cctype>
#include <algorithm>
#include <utility>
#include <time.h>
using namespace std;

#define FOR(i, a, b) for(int i=(a);i<(b);i++)
#define RFOR(i, b, a) for(int i=(b)-1;i>=(a);--i)
#define FILL(A,value) memset(A,value,sizeof(A))

#define ALL(V) V.begin(), V.end()
#define SZ(V) (int)V.size()
#define PB push_back
#define MP make_pair
#define Pi 3.14159265358979
#define x0 ikjnrmthklmnt
#define y0 lkrjhkltr
#define y1 ewrgrg

typedef long long Int;
typedef unsigned long long UInt;
typedef vector<int> VI;
typedef pair<int, int> PII;
typedef pair<Int, Int> PLL;
typedef pair<long double, long double> PDD;

const int INF = 1000000000;
const int BASE = 1000000007;
const int MAX = 107;
const int MAX2 = 10007;
const int MAXE = 100000;
const int ADD = 1000000;
const int MOD = 1000000007;
const int CNT = 0;

int c[7];

int dp3[MAX][MAX];
int dp4[MAX][MAX][MAX];

int main()
{
	freopen("in.txt" , "r" , stdin);
	freopen("out.txt" , "w" , stdout);

	int t;
	cin >> t;
	FOR(tt,0,t)
	{
		printf("Case #%d: " , tt + 1);

		int n , p;
		cin >> n >> p;

		FILL(c,0);

		FOR(i,0,n)
		{
			int x;
			cin >> x;
			x %= p;
			c[x] ++;
		}

		int res = c[0];

		if (p == 2)
		{
			res += (c[1] + 1) / 2;
			cout << res << endl;
			continue;
		}

		if (p == 3)
		{
			FILL(dp3,0);

			FOR(i,0,c[1] + 1)
				FOR(j,0,c[2] + 1)
				{
					int val = dp3[i][j];
					if ((i * 1 + j * 2) % 3 == 0)
						val ++;
					dp3[i + 1][j] = max(dp3[i + 1][j] , val);
					dp3[i][j + 1] = max(dp3[i][j + 1] , val);
				}
			res += dp3[c[1]][c[2]];
			cout << res << endl;
			continue;
		}
		if (p == 4)
		{
			FILL(dp4,0);

			FOR(i,0,c[1] + 1)
				FOR(j,0,c[2] + 1)
					FOR(k,0,c[3] + 1)
					{
						int val = dp4[i][j][k];
						if ((i * 1 + j * 2 + k * 3) % 4 == 0)
							val ++;
						dp4[i + 1][j][k] = max(dp4[i + 1][j][k] , val);
						dp4[i][j + 1][k] = max(dp4[i][j + 1][k] , val);
						dp4[i][j][k + 1] = max(dp4[i][j][k + 1] , val);
					}
			res += dp4[c[1]][c[2]][c[3]];
			cout << res << endl;
			continue;
		}

	}


    return 0;
}






