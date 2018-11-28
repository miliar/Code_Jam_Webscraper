#include <cstdio>
#include <iostream>
#include <ctime>
#include <iomanip>
#include <cstdlib>
#include <algorithm>
#include <vector>
#include <set>
#include <map>
#include <string>
#include <cstring>
using namespace std;

int T, x, C;
int D, N;

int K[1001], S[1001];
double tt[1001];

double solve() {
	for(int i = 0 ; i < N ; i++) {
		tt[i] = (double)(D - K[i])/S[i];
	}

	double m_t=0;
	for(int i = 0 ; i < N ; i++)
		m_t = max(tt[i], m_t);

	return (double)D/m_t;
}

int main() {
	scanf("%d", &T);
	while (T--) {
		scanf("%d %d", &D, &N);
		for(int i = 0 ; i < N ; i++) {
			scanf("%d %d", &K[i], &S[i]);
		}
		printf("Case #%d: %lf\n", ++C, solve());
	}
}
