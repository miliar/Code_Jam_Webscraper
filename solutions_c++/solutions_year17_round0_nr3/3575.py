/*
 * GCJ2017_QR_C.cpp
 *
 *  Created on: Apr 8, 2017
 *      Author: davidzhu
 */

#include <cstdio>
#include <iostream>
#include <algorithm>
#include <queue>

using namespace std;

int T, N, K;

void solve() {
	cin >> N >> K;
	priority_queue<int> pq;
	pq.push(N);
	int counter = 1;
	while(!pq.empty() && counter < K) {
		int cur = pq.top(); pq.pop();
		pq.push(cur/2);
		pq.push((cur-1)/2);
		counter++;
	}
	int cur = pq.top();
	cout << (cur/2) << " " << ((cur-1)/2) << endl;
}

int main() {
	freopen("GCJ2017_QR_C.in", "r", stdin);
	freopen("GCJ2017_QR_C.out", "w", stdout);
	cin >> T;
	for(int i = 0; i < T; i++) {
		cout << "Case #" << (i+1) << ": ";
		solve();
	}
}
