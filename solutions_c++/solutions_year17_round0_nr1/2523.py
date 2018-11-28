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

#define MAXN 1010
char n[MAXN];
int k;

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

void solve() {
	bool is_pos = true;
	int ans = 0;
	int s = strlen(n);
	for (int i = 0; i < s - k + 1; ++i) {
		if (n[i] == '-') {
			++ans;
			for (int j = i; j < i + k; ++j) {
				if (n[j] == '-') n[j] = '+';
				else			 n[j] = '-';
			}
		}
//		printf("%d %s\n", ans, n);
	}

	for (int i = 0; i < s; ++i) {
		if (n[i] == '-') is_pos = false;
	}

// printf("r = %s\n", n);
	// output answer
//	for (int i = 0; i < s; ++i) {
//		printf("%c", n[i]);
//	}
	if (is_pos) printf("%d\n", ans);
	else printf("IMPOSSIBLE\n");
//	printf("%s\n", n);
	fflush(stdout);
}

int main() {
	int cases;
	int caseid = 1;

	freopen("input.txt", "r", stdin);
	freopen("output", "w", stdout);
	scanf("%d", &cases);
	while (cases--) {
		printf("Case #%d: ", caseid++);
		scanf("%s %d", n, &k);
		solve();
	}
	return 0;
}


