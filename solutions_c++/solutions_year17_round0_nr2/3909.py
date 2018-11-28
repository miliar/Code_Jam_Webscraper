#include <cstdio>
#include <cstring>
#include <utility>
#include <algorithm>

int displacement = 0;

int find_bad(char *N, int sz) {
	int i;
	for(i = 1; i < sz; ++i) {
		if(N[i-1] > N[i]) {
			return i;
		}
	}
	return -1;
}

void decrease(char *N, int pos, int sz) {
	if(N[pos] == '1') {
		if(pos == 0) {
			N[pos] = '-';
			displacement = pos + 1;
		} else {
			N[pos] = '0';
		}
	} else {
		N[pos] = N[pos] - 1;
	}
	int i;
	for(i = pos+1; i < sz; ++i) {
		N[i] = '9';
	}
}

void solve(char *N, int sz) {
	int pos;
	while((pos = find_bad(N,sz)) > 0) {
		decrease(N, pos-1, sz);
	}
}

int main() {
	int T, t;
	char N[20];
	scanf("%d", &T);
	for(t = 0; t < T; ++t) {
		scanf("%s", N);
		displacement = 0;
		solve(N, strlen(N));
		printf("Case #%d: %s\n", t+1, N+displacement);
	}
	return 0;
}