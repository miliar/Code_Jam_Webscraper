#include <iostream>
#include <vector>
#include <algorithm>
#include <fstream>
#include <string>
#include <cmath>
#include <cstdio>

using namespace std;

#define REP(i, a, b)		for(i = int(a); i <= int(b); i++)
#define FOR(i, N)			REP(i, 0, N-1)

#define REPI(it, a, b)		for(it = (a); it != (b); it++)
#define FORI(it, v)			REPI(it, All(v))

#define All(v)				v.begin(), v.end()

#define VI					vector<int>
#define VVI					vector<VI>

#define VD					vector<double>

int main() {
	ifstream cin("input2.txt");
	ofstream cout("output1a.txt");
	int t, T;
	cin >> T;
	REP(t, 1, T) {
		int i;
		double D;
		int N;
		cin >> D >> N;

		VD K(N), S(N);
		FOR(i, N) cin >> K[i] >> S[i];

		double ans = -1;
		FOR(i, N) {
			double time = (D - K[i]) / S[i];
			double speed = D / time;
			if (i == 0 || speed < ans)
				ans = speed;
		}

		char answer[100];
		sprintf(answer, "Case #%d: %.6f", t, ans);
		cout << answer << endl;
	}
}