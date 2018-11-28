/*
 * GCJ2017_QR_A.cpp
 *
 *  Created on: Apr 7, 2017
 *      Author: davidzhu
 */

#include <cstdio>
#include <iostream>
#include <algorithm>

using namespace std;

int T, K, N, counter;
bool arr[1010];
string S;

void flip(int start) {
	for(int i = start; i < start + K; i++) {
		arr[i] = !arr[i];
	}
}

void solve() {
	cin >> S;
	cin >> K;
	N = S.length();
	counter = 0;
	for(int i = 0; i < N; i++) {
		if(S[i] == '+') {
			arr[i] = true;
		} else {
			arr[i] = false;
		}
	}
	for(int i = 0; i < N - K + 1; i++) {
		if(!arr[i]) {
			flip(i);
			counter++;
		}
	}
	bool flag = true;
	for(int i = N - K + 1; i < N; i++) {
		if(!arr[i]) {
			flag = false;
			break;
		}
	}
	if(flag) {
		cout << counter << endl;
	} else {
		cout << "IMPOSSIBLE" << endl;
	}
}

int main() {
	freopen("GCJ2017_QR_A.in", "r", stdin);
	freopen("GCJ2017_QR_A.out", "w", stdout);
	cin >> T;
	for(int i = 0; i < T; i++) {
		cout << "Case #" << (i+1) << ": ";
		solve();
	}
}
