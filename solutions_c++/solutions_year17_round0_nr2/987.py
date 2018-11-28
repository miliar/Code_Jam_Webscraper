#include <bits/stdc++.h>
using namespace std;

int A[20];
int ans[20];

int solve(int idx, int equal) {
	if(idx == 0) {
		return 1;
	}
	if(equal) {
		for(int i = A[idx]; i >= ans[idx + 1]; --i) {
			ans[idx] = i;
			if(solve(idx - 1, i == A[idx])) {
				return 1;
			}
		}
	}
	else {
		for(int i = 9; i >= ans[idx + 1]; --i) {
			ans[idx] = i;
			if(solve(idx - 1, 0)) {
				return 1;
			}
		}
	}
	return 0;
}

int main() {
	int t;
	scanf("%d", &t);
	for(int tc = 1; tc <= t; ++tc) {
		long long n;
		scanf("%lld", &n);
		long long temp = n;
		int done = 0;
		while(temp) {
			A[++done] = temp % 10;
			temp /= 10;
		}
		ans[done + 1] = 0;
		int final = solve(done, 1);
		assert(final == 1);
		while(ans[done] == 0) {
			done--;
		}
		if(done == 0) {
			++done;
		}
		printf("Case #%d: ", tc);
		for(int i = done; i > 0; --i) {
			printf("%d", ans[i]);
		}
		printf("\n");
	}
}