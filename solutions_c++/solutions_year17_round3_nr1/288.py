/*
 * GCJ2017_1C_A.cpp
 *
 *  Created on: Apr 29, 2017
 *      Author: davidzhu
 */

#include <cstdio>
#include <iostream>
#include <algorithm>

using namespace std;
typedef pair<double, double> pii; // r, h
typedef pair<pii, double> piii; // h, r, i
const double pi = 3.14159265358979;
const int MAXN = 1005;

int T, N, K;
pii pan[MAXN];
piii ph[MAXN];
bool used[MAXN];

void solve() {
	cin >> N >> K;
	for(int i = 0; i < N; i++) {
		cin >> pan[i].first >> pan[i].second;
	}
	sort(pan, pan+N);
	for(int i = 0; i < N; i++) {
		ph[i].first.first = pan[i].second*pan[i].first;
		ph[i].first.second = pan[i].first;
		ph[i].second = i;
	}
	sort(ph, ph+N);
	double ans = 0;
	for(int i = N-1; i >= K-1; i--) {
/*		for(int j = 0; j < N; j++) {
			used[j] = false;
		}
		used[i] = true;*/
		int curr = pan[i].first;
		double h = pan[i].first*pan[i].second;
		int curi = N-1;
		for(int j = 0; j < K-1; j++) {
			while(ph[curi].first.second > curr || ph[curi].second == i) {
				curi--;
			}
			h += ph[curi].first.first;
			curi--;
		}
		ans = max(ans, pi*curr*curr+2*pi*h);
	}
	printf("%.9f\n", ans);
}

int main() {
	freopen("GCJ2017_1C_A.in", "r", stdin);
	freopen("GCJ2017_1C_A.out", "w", stdout);
	cin >> T;
	for(int i = 0; i < T; i++) {
		cout << "Case #" << (i+1) << ": ";
		solve();
	}
}
