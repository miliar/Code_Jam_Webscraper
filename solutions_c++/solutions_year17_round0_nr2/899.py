#include <cstdio>
#include <iostream>
#include <ctime>
#include <iomanip>
#include <cstdlib>
#include <algorithm>
#include <vector>
#include <set>
#include <map>
#include <string>
#include <cstring>
using namespace std;

int T, x, C;

bool check(long long N) {
	int prev = N % 10;
	N /= 10;
	while(N) {
		if(prev < N % 10) return false;
		prev = N % 10;
		N /= 10;
	}
	return true;
}

long long next(long long N) {
	int cnt = 1;
	int prev = N % 10;
	N /= 10;
	while(N) {
		if(prev < N % 10) break;
		prev = N % 10;
		N /= 10;
		cnt++;
	}
	for(int i = 0 ; i < cnt ; ++i) N*=10;
	return N-1;
}

long long solve(long long N) {
	for(long long i = N ; i >= 0 ; i = next(i)) {
		if(check(i)) return i;
	}
	return 0;
}

int main() {
	scanf("%d", &T);
	while (T--) {
		long long N;
		scanf("%llu", &N);
		printf("Case #%d: %llu\n", ++C, solve(N));
	}
}
