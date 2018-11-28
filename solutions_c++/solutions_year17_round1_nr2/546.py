#include <algorithm>
#include <cstdio>
#include <cstdlib>
#include <cstring>
#include <iostream>
using namespace std;

const double EPS = 1e-7;

struct Package {
	int x, i, sig;
};

Package a[5005];
int b[55], c[55], d[55];


bool cmp(Package &p, Package &q) {
	if (p.x != q.x) return p.x < q.x;
	return p.sig < q.sig;
}

int main() {
	int Test;
	scanf("%d", &Test);
	for (int test = 1; test <= Test; test++) {
		int N, P, A = 0;
		scanf("%d%d", &N, &P);
		for (int i = 0; i < N; i++) scanf("%d", &b[i]);
		for (int i = 0; i < N; i++) {
			for (int j = 0; j < P; j++) {
				int x;
				scanf("%d", &x);
				int l = int(1.0 * x / b[i] / 1.1 - EPS) + 1;
				int r = int(1.0 * x / b[i] / 0.9 + EPS);
				if (l > r) {
					//cerr << "Error\n";
					continue;
				}
				a[A].x = l;
				a[A].i = i;
				a[A++].sig = -1;
				a[A].x = r;
				a[A].i = i;
				a[A++].sig = 1;
			}
		}
		sort(a, a + A, cmp);
		int ans = 0;
		for (int i = A - 1; i >= 0; i--) {
			if (a[i].sig == 1) {
				++c[a[i].i];
				bool flag = true;
				for (int j = 0; j < N; j++) flag &= c[j] > 0;
				if (flag) {
					ans += 1;
					for (int j = 0; j < N; j++) c[j]--, d[j]++;
				}
			} else {
				if (d[a[i].i] > 0) d[a[i].i]--; else c[a[i].i]--;
			}
		}
		printf("Case #%d: %d\n", test, ans);
	}
}