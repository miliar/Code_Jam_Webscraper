/*
 * GCJ2017_1B_A.cpp
 *
 *  Created on: Apr 22, 2017
 *      Author: davidzhu
 */

#include <cstdio>
#include <iostream>
#include <algorithm>

using namespace std;
const int MAXN = 1010;

int T, D, N;
int s[MAXN];
int k[MAXN];
double t[MAXN];
double curm;
double curt;

void solve() {
	cin >> D >> N;

	curm = D;
	curt = 0;

	for(int i = 0; i < N; i++) {
		cin >> k[i] >> s[i];
		t[i] = 1.0*(D-k[i])/s[i];
	}
	for(int i = 0; i < N; i++) {
		if(curt < t[i]) {
			curt = t[i];
			curm = 1.0*D/curt;
		}
	}
	printf("%.9f\n", curm);
}

int main() {
	freopen("GCJ2017_1B_A.in", "r", stdin);
	freopen("GCJ2017_1B_A.out", "w", stdout);
	cin >> T;
	for(int i = 0; i < T; i++) {
		cout << "Case #" << (i+1) << ": ";
		solve();
	}
}
