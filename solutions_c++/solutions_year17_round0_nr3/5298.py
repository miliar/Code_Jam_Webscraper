#include <cstdio>
#include <cstdlib>
#include <cstring>
#include <cmath>
#include <algorithm>
#include <queue>
#include <numeric>
#include <array>
#include <map>
#include <set>
#include <stack>
#include <unordered_map>
#include <functional>
#include <iostream>
#include <thread>
#include <sstream>
#include <atomic>

using namespace std;


int main () {
	int T;
	scanf("%d", &T);
	for (int t=1; t<=T; t++) {
		int N, K;
		scanf("%d%d", &N, &K);
                priority_queue<int> Q;
                Q.push(N);
                for (int i=1; i<K; i++) {
                    int v=Q.top();
                    Q.pop();
                    Q.push(v/2);
                    Q.push((v-1)/2);
                }
                printf("Case #%d: %d %d\n", t, Q.top()/2, (Q.top()-1)/2);
	}
	return 0;
}
