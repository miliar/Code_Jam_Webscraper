#include <algorithm>
#include <cstdio>
#include <cstdlib>
#include <cstring>
#include <iostream>
#include <queue>
using namespace std;

int main() {
	int Test;
	scanf("%d", &Test);
	for (int test = 1; test <= Test; test++) {
		cerr << "test: " << test << "\n";
		int N, K;
		scanf("%d%d", &N, &K);
		priority_queue<int> q;
		q.push(N);
		for (int k = 0; k < K - 1; k++) {
			int x = q.top();
			q.pop();
			if (x / 2 > 0) q.push(x / 2);
			if (x - x / 2 - 1 > 0) q.push(x - x / 2 - 1);
		}
		int x = q.empty() ? 1 : q.top();
		printf("Case #%d: %d %d\n", test, x / 2, x - x / 2 - 1); 
	}
}