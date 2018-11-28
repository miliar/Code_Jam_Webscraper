/*
 * GCJ2017_2_A.cpp
 *
 *  Created on: May 13, 2017
 *      Author: davidzhu
 */

#include <cstdio>
#include <iostream>
#include <algorithm>

using namespace std;
const int MAXN = 110;

int T, N, P;
int md[6];

void solve2() {
	int opp = 0;
	opp = md[1]/2;
	int ans = N - opp;
	cout << ans << endl;
	return;
}

void solve3() {
	int opp = 0;
	while(md[1] > 0 && md[2] > 0) {
		opp++;
		md[1]--;
		md[2]--;
	}
	if(md[1] > 0) {
		opp += md[1] - (md[1]+2)/3;
	}
	if(md[2] > 0) {
		opp += md[2] - (md[2]+2)/3;
	}
	int ans = N - opp;
	cout << ans << endl;
	return;
}

void solve4() {
	return;
}

void solve() {
	cin >> N >> P;
	for(int i = 0; i < P; i++) {
		md[i] = 0;
	}
	for(int i = 0; i < N; i++) {
		int temp;
		cin >> temp;
		md[temp%P]++;
	}
	if(P == 2) {
		solve2();
	} else if(P == 3) {
		solve3();
	} else {
		solve4();
	}
	return;
}

int main() {
	freopen("GCJ2017_2_A.in", "r", stdin);
	freopen("GCJ2017_2_A.out", "w", stdout);
	cin >> T;
	for(int i = 0; i < T; i++) {
		cout << "Case #" << (i+1) << ": ";
		solve();
	}
}
