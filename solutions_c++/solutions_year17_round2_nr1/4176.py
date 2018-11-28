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
#include <map>

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


double solve(long D, int N, VPLL KS) {
	sort(KS.begin(), KS.end());

	double td = 0;

	while (KS.size()>1) {
		PLL p2 = KS[KS.size() - 1];
		PLL p1 = KS[KS.size() - 2];

		KS.pop_back();

		if (p2.second >= p1.second) {
			continue;
		}

		KS.pop_back();

		double t = ((double)(p2.first) - (p1.first + p1.second*td)) / (p1.second - p2.second);
		double t2 = ((double)D - p2.first) / p2.second;

		if (t < t2) {
			td += t;
			KS.PB(PLL(p1.first + p1.second*td, p2.second));
		}
		else {
			KS.PB(PLL(p1.first + p1.second*td, p1.second));
		}
	}

	PLL p = KS[0];

	return ((double)D) / (((double)D-p.first)/p.second + td);
}

int main() {
	freopen("A-small-attempt2.in", "r", stdin);
	freopen("A-small-attempt2.out", "w", stdout);

	int T,N;
	long D;

	scanf("%d", &T);

	forN1(i, T) {
		scanf("%ld %d", &D, &N);

		VPLL KS = VPLL();

		forN1(j, N) {
			long KI = 0, SI = 0;
			scanf("%ld %ld", &KI, &SI);

			KS.PB(PLL(KI, SI));
		}

		double ret = solve(D, N, KS);

		printf("Case #%d: %.8lf\n", i, ret);
	}


}