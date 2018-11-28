/*
 * main.cpp
 *
 *  Created on: 9 Apr 2016
 *      Author: ljchang
 */

#include <cstdio>
#include <cstring>
#include <vector>
#include <set>
#include <map>
#include <algorithm>

using namespace std;

long long N, K;

void input() {
	scanf("%lld%lld", &N, &K);
}

void solve() {
	/*char *str = new char[N+2];
	memset(str, 0, sizeof(char)*(N+2));
	str[0] = str[N+1] = 1;

	for(int i = 0;i < K;i ++) {
		int idx = -1, min, max;
		for(int j = 1;j <= N;j ++) if(!str[j]) {
			int left = 0, right = 0;
			for(int k = j - 1;!str[k];k --) ++ left;
			for(int k = j + 1;!str[k];k ++) ++ right;
			if(left > right) swap(left, right);
			if(idx == -1||left > min||(left == min&&right > max)) {
				idx = j;
				min = left;
				max = right;
			}
		}
		str[idx] = 1;
		if(i == K-1) printf(" %d %d\n", max, min);
	}*/

	while(K > 1) {
		-- K;
		if(N%2 == 1) {
			N = (N-1)/2;
			K -= K/2;
		}
		else {
			long long left = (N-1)/2;
			long long right = left+1;
			if(K%2 == 0) {
				N = left;
				K /= 2;
			}
			else {
				N = right;
				K -= K/2;
			}
		}
	}

	long long min = (N-1)/2;
	long long max = min;
	if((N-1)%2 == 1) ++ max;
	printf(" %lld %lld\n", max, min);
}

int main() {
	int t;
	scanf("%d", &t);
	for(int cas = 0; cas < t;cas ++) {
		input();
		printf("Case #%d:", cas+1);
		solve();
	}
	return 0;
}
