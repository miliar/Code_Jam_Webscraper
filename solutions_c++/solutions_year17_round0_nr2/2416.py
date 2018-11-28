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

string solve(string N) {
	if (N.size() == 1) {
		return N;
	}

	bool isTidy = true;
	while (true) {
		char prev = N[0];
		isTidy = true;
		for (int i = 1; i < N.size(); ++i) {
			char ni = N[i];

			if (ni < prev) {
				for (int j = i; j < N.size(); ++j) {
					N[j] = '9';
				}

				N[i - 1] = prev - 1;

				isTidy = false;

				break;
			}

			prev = ni;
		}

		if (isTidy) {
			if (N[0] == '0') {
				N = N.substr(1, N.size() - 1);
			}

			break;
		}
	}

	return N;
}

int main() {
	freopen("B-large.in", "r", stdin);
	freopen("B-large.out", "w", stdout);

	int T;
	char N[20];
	scanf("%d", &T);

	forN1(i, T) {
		scanf("%s", N);

		string ret = solve(string(N));

		printf("Case #%d: %s\n", i, ret.c_str());
	}


}