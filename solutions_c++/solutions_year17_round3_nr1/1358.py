#include<bits/stdc++.h>

using namespace std;

const int MAXN = 1e3+6;

struct NODE{
	long long R, H, S;
	bool operator < (const NODE & A) const {
		return S > A.S;
	}
}A[MAXN];

double work(){
	int N, K;
	scanf("%d%d", &N, &K);
	long long MS = 0;
	long long ans = 0;
	for (int i = 0; i < N; ++i) {
		scanf("%lld%lld", &A[i].R, &A[i].H);
		A[i].S = 2 * A[i].R * A[i].H;
	}
	sort(A, A+N);
	for (int i = 0; i < N; ++i) {
		long long T = 0;
		T = A[i].R * A[i].R + A[i].S;
		int k = 0;
		for (int j = 0; j < N && k < K-1; ++j) {
			if (j == i) continue;
			++k;
			T += A[j].S;
		}
		if (T > ans) ans = T;
	}
	return ans * acos(-1);
}

int main(){
	int T;
	scanf("%d", &T);
	for (int i = 1; i <= T; ++i) {
		printf("Case #%d: %.20lf\n", i, work());
	}
	return 0;
}
