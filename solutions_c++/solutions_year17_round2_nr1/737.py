#include <iostream>
#include <string>
#include <cstring>
#include <cstdio>
#include <algorithm>
using namespace std;

#define LL long long
#define INF (1LL<<60)
#define MAXN 1001

struct Horse {
	double K, S;
};

int T, nCase;
int D, N;
Horse H[MAXN];

double solv()
{
	double maxt = 0;
	for (int i=0;i<N;++i) {
		double t = (D-H[i].K) / H[i].S;
		if (t > maxt) maxt = t;
	}
	return D/maxt;
}

int main ()
{
	cin >> T;
	for (nCase = 1; nCase <= T; ++nCase) {
		cin >> D >> N;
		for (int i=0;i<N;++i)
			cin >> H[i].K >> H[i].S;
		printf("Case #%d: %.6f\n", nCase, solv());
	}
	return 0;
}