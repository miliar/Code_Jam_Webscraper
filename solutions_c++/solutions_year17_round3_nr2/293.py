/*
 * GCJ2017_1C_B.cpp
 *
 *  Created on: Apr 29, 2017
 *      Author: davidzhu
 */

#include <cstdio>
#include <iostream>
#include <algorithm>

using namespace std;
const int MAXN = 105;
typedef pair<int, int> pii;
typedef pair<pii, int> piii;

int T, C, J;
pii ct[MAXN];
pii jt[MAXN];
piii both[MAXN*2];
int ce[MAXN];
int je[MAXN];

void solve() {
	cin >> C >> J;
	int conly = 0, jonly = 0;
	int flips = 0;
	int free = 0;
	int nc = 0; // # of consecutive c's
	int totc = 0; // total time between consecutive c's
	int nj = 0;
	int totj = 0;

	for(int i = 0; i < C; i++) {
		cin >> ct[i].first >> ct[i].second;
		both[i].first = ct[i];
		both[i].second = 0;
		conly += ct[i].second - ct[i].first;
	}
	sort(ct, ct+C);
	for(int i = 0; i < J; i++) {
		cin >> jt[i].first >> jt[i].second;
		both[i+C].first = jt[i];
		both[i+C].second = 1;
		jonly += jt[i].second - jt[i].first;
	}
	sort(jt, jt+J);
	sort(both, both+C+J);
	both[C+J] = piii(pii(both[0].first.first+1440, both[0].first.second+1440), both[0].second);
	for(int i = 0; i < C+J; i++) {
		if(both[i].second != both[i+1].second) {
			flips++;
			free += both[i+1].first.first - both[i].first.second;
		} else if(both[i].second == 0) {
			ce[nc] = both[i+1].first.first - both[i].first.second;
			totc += ce[nc];
			nc++;
		} else {
			je[nj] = both[i+1].first.first - both[i].first.second;
			totj += je[nj];
			nj++;
		}
	}
	sort(ce, ce+nc);
	sort(je, je+nj);
//	cout << "free " << free << " conly " << conly << " jonly " << jonly << " totc " << totc << " totj " << totj << endl;

	if(conly + totc + free < 720) {
		while(conly + totc + free < 720) {
			nj--;
			free += je[nj];
			totj -= je[nj];
			flips += 2;
		}
	} else {
		while(jonly + totj + free < 720) {
			nc--;
			free += ce[nc];
			totc -= ce[nc];
			flips += 2;
		}
	}
	cout << flips << endl;
}

int main() {
	freopen("GCJ2017_1C_B.in", "r", stdin);
	freopen("GCJ2017_1C_B.out", "w", stdout);
	cin >> T;
	for(int i = 0; i < T; i++) {
		cout << "Case #" << (i+1) << ": ";
		solve();
	}
}
