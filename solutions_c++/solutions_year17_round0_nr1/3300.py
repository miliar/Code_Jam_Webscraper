#include <iostream>
#include <sstream>
#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <math.h>
#include <algorithm>
#include <vector>
#include <iomanip>
#include <set>
#include <map>
#include <stack>
#include <queue>
#include <bitset>
#include <assert.h>
#include <deque>
using namespace std;

typedef unsigned long long UL;
typedef long long LL;
#define LP(i, a, b) for (int i = int(a); i < int(b); i++)
#define LPE(i, a, b) for (int i = int(a); i <= int(b); i++)
typedef pair<int, int> PII;
typedef vector<vector<PII> > WAL;
typedef vector<vector<int> > SAL;
#define Ep 1e-7

#define INF 1e16

/*

 */

int const MaxSize = 1e5 + 10;

int main() {

	ios_base::sync_with_stdio(false);
	//freopen("/Users/george/A_1.in", "r", stdin);
	freopen("/Users/george/Downloads/A-large.in", "r", stdin);
	freopen("/Users/george/Downloads/A_large_out", "w", stdout);
	int T;
	cin >> T;
	LPE(cn, 1, T)
	{
		cout << "Case #" << cn << ": ";
		string S;
		int K;
		cin >> S >> K;
		int ans = 0;
		LPE(i, 0, S.length() - K)
		{
			if (S[i] == '+')
				continue;

			ans++;
			LP(j, 0, K)
			{
				if (S[i + j] == '+')
					S[i + j] = '-';
				else
					S[i + j] = '+';
			}
		}

		bool good = true;
		LP(i, 0, S.length())
		{
			if (S[i] == '-') {
				good = false;
				break;
			}
		}

		if (good)
			cout << ans << endl;
		else
			cout << "IMPOSSIBLE" << endl;
	}

	return 0;
}
