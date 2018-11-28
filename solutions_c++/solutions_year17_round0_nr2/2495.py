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

#define MAXN 20
char n[MAXN];

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
	int s = strlen(n);
	char last;
rerun:
// printf("r = %s\n", n);
	last = '0';
	for (int i = 0; i < s; ++i) {
		if (n[i] >= last) {
			last = n[i];
			continue;
		}
		for (int j = i; j < s; ++j) {
			n[j] = '9';
		}
		for (int j = i - 1; j >= 0; --j) {
			if (n[j] == '0') {
				n[j] = '9';
			} else {
				n[j] = (char)(n[j] - 1);
				break;
			}
		}
		goto rerun;
		break;
	}
	// output answer
	bool is_lead = true;
	for (int i = 0; i < s; ++i) {
		if (n[i] == '0' && is_lead)
			continue;
		else
			is_lead = false;
		printf("%c", n[i]);
	}
	printf("\n");
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
		scanf("%s", n);
		solve();
	}
	return 0;
}


