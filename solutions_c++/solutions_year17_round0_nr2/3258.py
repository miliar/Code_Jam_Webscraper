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

LL N;

bool perfect(LL curN) {
	int lastD = 10;

	while (curN) {
		int curD = curN % 10;
		curN /= 10;

		if (curD > lastD)
			return false;
		else
			lastD = curD;
	}

	return true;
}

void solve() {
	if(perfect(N)){
		cout << N << endl;
		return;
	}

	LL prefix = N / 10L;
	LL base = 10L;

	while (prefix) {

		LL curTry = (prefix - 1) * base + base - 1L;

		if (perfect(curTry)) {
			cout << curTry << endl;
			return;
		}

		prefix /= 10L;
		base *= 10L;
	}

}
int main() {

	ios_base::sync_with_stdio(false);
	//freopen("/Users/george/A_1.in", "r", stdin);
	freopen("/Users/george/Downloads/B-large.in", "r", stdin);
	freopen("/Users/george/Downloads/B_large.out", "w", stdout);
	int T;
	cin >> T;
	LPE(cn, 1, T)
	{
		cin >> N;
		cout << "Case #" << cn << ": ";
		solve();
	}

	return 0;
}
