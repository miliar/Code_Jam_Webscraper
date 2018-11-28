#include <bits/stdc++.h>

using namespace std;
typedef long long ll;
const int MAXN = 53;

#define debug(...) fprintf(stderr, __VA_ARGS__)

bool approx (ll x, ll y) {
	//x is the original value
	//y is the new value
	return 9 * x <= 10 * y && 10 * y <= 11 * x;
}

int N, P;
int R[MAXN], Q[MAXN][MAXN];
int ptr[MAXN];

int go() {
	scanf("%d %d", &N, &P);
	for (int i = 0; i < N; i++) {
		scanf("%d", &R[i]);
	}
	for (int i = 0; i < N; i++) {
		ptr[i] = 0;
		int *arr = Q[i];
		for (int j = 0; j < P; j++) {
			scanf("%d", &arr[j]);
		}
		sort(arr, arr + P);
	}
	fprintf(stderr, "ere\n");

	int ans = 0;
	bool isend = false;
	for (int t = 1; !isend && t <= 1200000; t++) {
		//take t amount. so t * R[i] * .9 or t * R[i] * 1.1
		bool cando;
		do {
			isend = true;
			cando = true;
			for (int i = 0; i < N; i++) {
				ll val = ll(t) * R[i];
				for (; ptr[i] < P; ptr[i]++) {
					if (9 * val <= 10 * Q[i][ptr[i]]) {
						break;
					}
				}

				if (ptr[i] < P) {
					isend = false;
				}

				if (ptr[i] == P || !approx(val, Q[i][ptr[i]])) {
					cando = false;
				}
			}

			if (cando) {
				ans++;
				for (int i = 0; i < N; i++) {
					ptr[i]++;
				}
			}
		} while (cando);
	}
	debug("eren\n");
	return ans;
}

int main() {
	int nq;
	scanf("%d", &nq);
	for (int i = 1; i <= nq; i++) {
		printf("Case #%d: %d\n", i, go());
	}
}
