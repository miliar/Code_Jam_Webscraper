/*
 * GCJ 2017 round 1B
 * Task: A. Steed 2: Cruise control
 */
#include <stdio.h>
#include <string.h>
#include <string>
#include <vector>
#include <sstream>
#include <algorithm>
#include <iostream>
#include <string.h>
#include <queue>
using namespace std;

#define FOR(i,n) for (int i = 0; i < n; i++)
#define abs(x) ((x)<0?(-(x)):(x))
#define REP(i,v) for (unsigned i = 0; i < v.size(); i++)
#define RL(i,v) for (unsigned i = 0; i < v.length(); i++)
typedef long long ll;

const int INF = 999666111;
const int MAXN = 1001;

int n;
double D;
double init[MAXN], speed[MAXN];

struct Crossing {
	double time;
	int i, j;
	Crossing(){}
	Crossing(double time, int i, int j): time(time), i(i), j(j) {}
	
	inline bool operator < (const Crossing& rhs) const
	{
		if (time != rhs.time) return time > rhs.time;
		if (i != rhs.i) return i > rhs.i;
		return j > rhs.j;
	}
};

double solve()
{
	scanf("%lf%d", &D, &n);
	FOR(i, n) scanf("%lf%lf", &init[i], &speed[i]);
	
	bool dead[MAXN] = {false};
	priority_queue<Crossing> Q;
	FOR(i, n) {
		Q.push(Crossing((D - init[i]) / speed[i], i, -1));
	}
	FOR(i, n) FOR(j, n) {
		if (i == j || init[i] > init[j] || speed[i] <= speed[j]) continue;
			
		// init[j] > init[i]; speed[j] < speed[i]:
		double spdiff = speed[i] - speed[j];
		double stdiff = init[j] - init[i];
		double timeToCatchUp = stdiff / spdiff;
		if (init[j] + timeToCatchUp * speed[j] <= D) {
			Q.push(Crossing(timeToCatchUp, i, j));
		} else {
			Q.push(Crossing((D - init[i]) / speed[i], i, -1));
		}
	}
	
	double lastHorseTime = -1;
	while (!Q.empty()) {
		Crossing c = Q.top();
		Q.pop();
		if (c.j == -1) {
			if (!dead[c.i])
				lastHorseTime = max(lastHorseTime, c.time);
		} else {
			dead[c.i] = true;
		}
	}
	return D/lastHorseTime;
}

int main(void)
{
	//freopen("/home/vesko/gcj/A-small.in", "rt", stdin);
	int T;
	scanf("%d", &T);
	for (int tc = 1; tc <= T; tc++) {
		printf("Case #%d: %.6lf\n", tc, solve());
	}
	return 0;
}
