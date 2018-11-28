/*
 * GCJ2017_1B_C.cpp
 *
 *  Created on: Apr 22, 2017
 *      Author: davidzhu
 */

#include <cstdio>
#include <iostream>
#include <algorithm>

using namespace std;
const int MAXN = 105;
const long long BIG = 1L << 59;

int T;
int N, Q;
int E[MAXN], S[MAXN];
int D[MAXN][MAXN];
int U, V;
double dp[MAXN]; // how much time has passed when you reach that city

void solvesmall() {
	cin >> N >> Q;
	for(int i = 0; i < N; i++) {
		cin >> E[i] >> S[i];
	}
	for(int i = 0; i < N; i++) {
		for(int j = 0; j < N; j++) {
			cin >> D[i][j];
		}
	}
	cin >> U >> V;
	U--; V--;

	for(int i = 0; i < N; i++) {
		dp[i] = BIG;
	}
	dp[0] = 0;

	for(int i = 0; i < N-1; i++) {
		double cumd = 0;
		for(int j = i+1; j < N; j++) {
			cumd += D[j-1][j];
			if(E[i] >= cumd) {
				double ti = 1.0*cumd/S[i];
				dp[j] = min(dp[i] + ti, dp[j]);
			} else {
				break;
			}
		}
	}
	printf("%.9f\n", dp[N-1]);
}

int main() {
	freopen("GCJ2017_1B_C.in", "r", stdin);
	freopen("GCJ2017_1B_C.out", "w", stdout);
	cin >> T;
	for(int i = 0; i < T; i++) {
		cout << "Case #" << (i+1) << ": ";
		solvesmall();
	}
}
