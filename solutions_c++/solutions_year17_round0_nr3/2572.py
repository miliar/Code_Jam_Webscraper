#include <cstdio>
#include <iostream>
#include <vector>
#include <cmath>
#include <algorithm>
#include <string>
#include <set>
#include <map>
#include <list>
#include <ctime>
#include <cstring>
#include <deque>
#include <queue>
#include <sstream>
#include <iomanip>
using namespace std;
//-----------------------------------------------------------
#define forn(i, n) for(int i = 0; i < (int)(n); i++)
#define ford(i, n) for(int i = (int)(n) - 1; i >= 0; i--)
#define pb push_back
#define mp make_pair
#define fs first
#define sc second
#define last(a) int(a.size() - 1)
#define all(a) a.begin(), a.end()
#define seta(a,x) memset (a, x, sizeof (a))
#define I (int)
typedef long long ll;
typedef unsigned long long ull;
typedef pair<int, int> pii;
typedef long double ldb;

const long double eps = 1e-9;
const int inf = (1 << 30) - 1;
const ull inf64 = ((ull) 1 << 62) - 1;
const long double pi = 3.1415926535897932384626433832795;

#define bit(i) ((ull)1 << i)
//-----------------------------------------------------------

//#define MAXN 1010
ull n;
ull k;

//void printb(int b) {
//	for(int j = 0; j < MAXN; ++j) {
//		if (j%4 == 0) {
//			cout << endl;
//		}
//		if ((1 << j) & b) {
//			cout << 1;
//		} else {
//			cout << 0;
//		}
//
//	}
//	cout << endl;
//}

/*
 * ------ -----
 * --O--- --O--
 * --O-O- O-O--
 * O-O-O- O-OO-
 */

void solve2() {
	priority_queue<ull> pq;
	pq.push(n);
	ull maxn = 0;
	ull minn = 0;
	for (ull i = 0; i < k; ++i) {
		ull f = pq.top();
		pq.pop();
		maxn = (f - 0) / 2;
		minn = (f - 1) / 2;
		pq.push(maxn);
		pq.push(minn);
//		printf("%llu %llu\n", maxn, minn);
	}
	printf("%llu %llu\n", maxn, minn);
	fflush(stdout);
	return;
}

void solve() {
	ull left = k;
	ull man = 0;
	for (ull level = 0; ; ++level) {
		if (left - 1 >= bit(level)) {
			left -= bit(level);
			man += bit(level);
		} else {
			left -= 1;

			ull leftn = n - man;
			ull mod = leftn % bit(level);
			ull seg = (leftn - mod) / bit(level);
			if (left < mod) {
				seg++;
			}

			if (seg <= 1) {
				printf("0 0\n");
			} else {
				printf("%llu %llu\n", (seg) / 2, (seg - 1) / 2);
			}
//			printf("%llu %llu leftn %llu mode %llu %llu\n", level, left, leftn, mod, seg);
// idx
			break;
		}
	}

//	if (r.y == r.x + 1) {
//		printf("0 0\n");
//	} else {
//		printf("%llu %llu\n", r_dif - 1, l_dif - 1);
//	}
//	printf("%llu\n", n);
	fflush(stdout);
}

int main() {
	int cases;
	int caseid = 1;

	freopen("input.txt", "r", stdin);
//	freopen("output", "w", stdout);
	scanf("%d", &cases);
	while (cases--) {
		printf("Case #%d: ", caseid++);
		scanf("%llu%llu", &n, &k);
		solve();
//		solve2();
	}
	return 0;
}


