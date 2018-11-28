#include <iostream>
#include <queue>
#include <stdio.h>

using namespace std;

int main() {
	int T, N, K;
	cin >> T;
	for(int t=1 ; t <= T ; t++) {
		cin >> N >> K;
		priority_queue<int> ranges;
		ranges.push(N);

		for(int i=0 ; i < K-1 ; i++) {
			int L = ranges.top();
			ranges.pop();
			ranges.push(L/2);
			ranges.push((L-1)/2);
		}

		int L = ranges.top();
		printf("Case #%d: %d %d\n", t, L/2, (L-1)/2);
	}
}

// https://code.google.com/codejam/contest/3264486/dashboard#s=p2
