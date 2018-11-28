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

int solve(string S, int K) {
	int cnt = 0;

	for (int i = 0; i < S.size(); ++i) {
		char f = S[i];
		if (f == '+') {
			continue;
		}
		else if (i > S.size() - K) {
			return -1;
		}
		else {
			cnt++;
			forN(j, K) {
				char fTmp = S[i + j];
				if (fTmp == '-') {
					S[i + j] = '+';
				}
				else {
					S[i + j] = '-';
				}
			}
		}
	}

	return cnt;
}

int main() {
	freopen("A-large.in", "r", stdin);
	freopen("A-large.out", "w", stdout);

	int T,K;
	char S[1001];
	scanf("%d", &T);

	forN1(i, T) {
		scanf("%s %d", S, &K);

		int ret = solve(string(S), K);

		if (ret == -1) {
			printf("Case #%d: IMPOSSIBLE\n", i);
		}
		else {
			printf("Case #%d: %d\n", i, ret);
		}
	}


}