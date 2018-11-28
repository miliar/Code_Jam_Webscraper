#define ALL(C) (C).begin(), (C).end()
#define forN(I, C) for(int I=0; I<int(C); ++I)
#define forEach(I, C) for(int I=0; I<int((C).size()); ++I)
#define forN1(I, C) for(int I=1; I<=int(C); ++I)
#define forEach1(I, C) for(int I=1; I<=int((C).size()); ++I)
#define PI 3.14159265358979323846
#define STR(s) to_string(s)
#define INT(S) stoi(S)
#define PB(V) push_back(V)

#include <iostream>
#include <fstream>
#include <vector>
#include <algorithm>
#include <cmath>
#include <set>
#include <string>
#include <queue>
#include <utility>
#include <list>
#include <functional>
#include <ios>

using namespace std;

typedef vector<string> VS;
typedef vector<int> VI;
typedef vector<long> VL;
typedef queue<int> QI;
typedef queue<long> QL;
typedef pair<int, int> PII;
typedef pair<long, long> PLL;
typedef pair<pair<int, int>, int> PPIII;
typedef vector<PII> VPII;
typedef vector<PLL> VPLL;
typedef priority_queue<PII, VPII, greater<PII>> PQPII;
typedef priority_queue<PLL, VPLL, greater<PLL>> PQPLL;
typedef set<PII> SPII;
typedef set<PLL> SPLL;
typedef set<PPIII> SPPIII;
typedef list<PII> LPII;
typedef list<PLL> LPLL;
typedef list<int> LI;
typedef vector<LI> VLI;
typedef vector<LPII> VLPII;
typedef vector<LPLL> VLPLL;
typedef priority_queue<PPIII> PQPPIII;
typedef long long int lli;

void solve(lli N, lli K) {
	/*int b = 0;
	int i = 64;
	lli tmp = K;
	while (!b) {
		i--;
		b = (tmp >> i) & 1;
	}
	lli div = 1 << i + 1;

	lli q = N / div;
	lli r = N % div;

	if (r > 0) {
		printf("%ll %ll\n", q, q);
	}
	else {
		printf("%ll %ll\n", q, q - 1);
	}*/
	lli oldHiLo[2];
	lli oldTimes[2];
	lli hiLo[2];
	lli times[2];

	forN(i, 2) {
		oldHiLo[i] = 0;
		oldTimes[i] = 0;
		hiLo[i] = 0;
		times[i] = 0;
	}

	hiLo[0] = N;
	times[0] = 1;


	while (K > (times[0] + times[1])) {
		forN(i, 2) {
			oldHiLo[i] = hiLo[i];
			oldTimes[i] = times[i];
			hiLo[i] = 0;
			times[i] = 0;
		}

		forN(i, 2) {
			if (oldHiLo[i] == 0) {
				continue;
			}
			lli qi = oldHiLo[i] / 2;
			lli ri = oldHiLo[i] % 2;
			lli hii = qi;
			lli loi = qi;
			if (ri == 0) {
				loi = hii - 1;
			}

			lli tmpHiLo[2] = { 0, 0 };
			tmpHiLo[0] = hii;
			tmpHiLo[1] = loi;
			forN(j, 2) {
				forN(k, 2) {
					if (hiLo[k] == 0) {
						hiLo[k] = tmpHiLo[j];
						times[k] = oldTimes[i];
						break;
					}
					else if (hiLo[k] == tmpHiLo[j]) {
						times[k] += oldTimes[i];
						break;
					}
				}
			}
		}

		K -= (oldTimes[0] + oldTimes[1]);
	}

	int i = -1;
	if (K <= times[0]) {
		i = 0;
	}
	else if (K <= times[0] + times[1]) {
		i = 1;
	}

	lli qi = hiLo[i] / 2;
	lli ri = hiLo[i] % 2;
	lli hii = qi;
	lli loi = qi;
	if (ri == 0) {
		loi = hii - 1;
	}

	printf("%lld %lld\n", hii, loi);
	return;
}


int main() {
	freopen("C-large.in", "r", stdin);
	freopen("C-large.out", "w", stdout);

	int T;
	lli N, K;

	scanf("%d", &T);

	forN1(i, T) {
		scanf("%lld %lld", &N, &K);

		printf("Case #%d: ", i);
		solve(N, K);
	}


}