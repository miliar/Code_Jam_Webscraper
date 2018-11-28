/*
 * GCJ2017_1C_C.cpp
 *
 *  Created on: Apr 29, 2017
 *      Author: davidzhu
 */

#include <cstdio>
#include <iostream>
#include <algorithm>

using namespace std;
const int MAXN = 55;
const double eps = 0.000000001;

int T;
int N, K;
double P;
double U[MAXN];

int getnuml(int numl) {
	while(numl < N) {
		if(U[numl] <= U[numl-1] + eps && U[numl] >= U[numl-1] - eps) {
			numl++;
		} else {
			break;
		}
	}
	return numl;
}

void solve() {
	cin >> N >> K;
	cin >> P;
	for(int i = 0; i < N; i++) {
		cin >> U[i];
	}
	sort(U, U+N);
	int numl = getnuml(1);

	while(P > 0) {
		double div = P/numl;
		if(numl == N || U[numl] - U[numl-1] > div) {
			for(int i = 0; i < numl; i++) {
				U[i] += div;
			}
			P = 0;
			break;
		} else {
			double newdiv = U[numl] - U[numl-1];
			for(int i = 0; i < numl; i++) {
				U[i] += newdiv;
			}
			P -= numl*newdiv;
			numl = getnuml(numl);
		}
	}

	double ans = 1;;
	for(int i = 0; i < N; i++) {
		ans *= U[i];
	}
	printf("%.9f\n", ans);
}

int main() {
	freopen("GCJ2017_1C_C.in", "r", stdin);
	freopen("GCJ2017_1C_C.out", "w", stdout);
	cin >> T;
	for(int i = 0; i < T; i++) {
		cout << "Case #" << (i+1) << ": ";
		solve();
	}
}
