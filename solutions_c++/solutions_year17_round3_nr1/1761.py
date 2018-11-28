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
typedef pair<lli, lli> Plli;
typedef vector<Plli> VPlli;


int visit[1002];

double solve(int N, int K, VPlli pancakes) {
	forN(i, N) {
		visit[i] = 0;
	}

	double total = 0;
	std::sort(pancakes.begin(), pancakes.end());


	int finalMax = -1;

	for (int i = 0; i < K; ++i) {
		double max = 0;
		double maxHA = 0;
		int maxIndex = -1;
		for (int j = 0; j < N; ++j) {
			if (visit[j]) {
				continue;
			}

			lli r = pancakes[j].first;
			lli h = pancakes[j].second;
			double ha = r * h * 2 * PI;

			double ta = ha;
			if (i == K - 1 && j > finalMax) {
				if (finalMax == -1) {
					ta += (r*r) * PI;
				}
				else {
					ta += (r*r - pancakes[finalMax].first * pancakes[finalMax].first) * PI;
				}
				
			}

			if (ta > max) {
				max = ta;
				maxIndex = j;
				maxHA = ha;
			}
		}

		total += maxHA;
		visit[maxIndex] = 1;
		if (maxIndex > finalMax) {
			finalMax = maxIndex;
		}
	}

	lli lr = pancakes[finalMax].first;
	double area = lr * lr * PI;
	total += area;

	return total;
}

int main() {
	//freopen("A-small-practice.in", "r", stdin);
	//freopen("A-small-practice.out", "w", stdout);

	freopen("A-large.in", "r", stdin);
	freopen("A-large.out", "w", stdout);


	int T, N, K;
	lli RI, HI;
	scanf("%d", &T);

	forN1(i, T) {
		scanf("%d %d", &N, &K);

		VPlli pancakes = VPlli();
		forN(i, N) {
			scanf("%lld %lld", &RI, &HI);
			pancakes.PB(Plli(RI, HI));
		}

		double ret = solve(N, K, pancakes);

		printf("Case #%d: %.8lf\n", i, ret);
	}


}