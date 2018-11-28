#include <algorithm>
#include <cmath>
#include <cstring>
#include <cstdio>
#include <iostream>
#include <map>
#include <set>
#include <vector>
#include <queue>
#include <iomanip>

using namespace std;
typedef unsigned long long ull;

int sched[1444];

int dp[1444][721][2];

int swapP(int person) {
	return person != 1 ? 1 : 2;
}

int magic(int time, int cTime, int person) {
	if (cTime > 720) return 50000;
	if (time == 1440) {
		if (cTime != 720) return 50000;
		if (sched[time] == person) return 0;
		else return 1;
	}
	int &res = dp[time][cTime][person];
	if (res != -1) return res;
	if (sched[time] != 0) {
		if (sched[time] == 1) ++cTime;
		if (sched[time] == person) {
			return magic(time+1, cTime, person);
		} else {
			return 1 + magic(time+1, cTime, swapP(person));
		}
	}
	res = magic(time+1, cTime + (person == 1), person);
	int other = swapP(person);
	res = min(res, 1+magic(time+1, cTime + (other == 1), other));
	return res;
}

void solve() {
	int nc, nj;
	fill(sched, sched+1441, 0);
	cin >> nc >> nj;
	for (int i=0; i<nc; ++i) {
		int start, end;
		cin >> start >> end;
		for (int t=start; t<end; ++t) {
			sched[t] = 1;
		}
	} 
	for (int i=0; i<nj; ++i) {
		int start, end;
		cin >> start >> end;
		for (int t=start; t<end; ++t) {
			sched[t] = 2;
		}
	}
	int best = 20000;
	for (int i=1; i<=2; ++i) {
		sched[1440] = i;
		memset(dp, -1, sizeof(dp));
		best = min(best, magic(0, 0, i));
	}
	cout << best << endl;
}

int main() {
	int cases;
	cin >> cases;
	for (int i=1; i<=cases; ++i) {
		cout << "Case #" << i << ": ";
		solve();
	}
	return 0;
}
