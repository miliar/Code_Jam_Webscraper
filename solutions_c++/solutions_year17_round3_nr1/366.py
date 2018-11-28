#include <bits/stdc++.h>

#define rep(i, n) for(int i = 0; i < n; i ++)
typedef long long LL;
const int N = 1e3 + 5;
const double pi = acos(-1.0);

struct Cake {
	int r, h, id;
	bool operator < (const Cake &rhs) const {
		return r*1LL*h > rhs.r*1LL*rhs.h;
	}
} cakes[N];

bool cmpR(Cake a, Cake b) {
	return a.r < b.r;
}

bool cmpH(Cake a, Cake b) {
	return a.h > b.h;
}

LL sq(int x) {
	return x*1LL*x;
}

double RR(int x) {
	return sq(x)*pi;
}

double RH(int x, int h) {
	return 2*pi*x*h;
}

std::multiset<Cake> cs;

int main() {
	int T, n, r, h, K;
	scanf("%d", &T);
	rep(cas, T) {
		scanf("%d%d", &n, &K);
		rep(i, n) {
			scanf("%d%d", &cakes[i].r, &cakes[i].h);
			cakes[i].id = i;
		}
		double answer = 0.0;
		cs.clear();
		std::sort(cakes, cakes + n, cmpR);
		for (int i = 0, j; i < n; i = j) {
			j = i + 1;
			cs.insert(cakes[i]);
			while(j < n && cakes[j].r == cakes[j-1].r) {
				cs.insert(cakes[j]);
				j ++;
			}
			if (cs.size() < K) {
				continue;
			}
			double better = 0.0;
			for (int o = i; o < j; o ++) {
				better = RR(cakes[o].r) + RH(cakes[o].r, cakes[o].h);
				int used = cakes[o].id;
				int cc = 1;
				for (auto &v: cs) {
					if (cc == K) {
						break;
					}
					if (v.id == used) {
						continue;
					}
					cc ++;
					better += RH(v.r, v.h);
				}
				answer = std::max(answer, better);
			}
		}
		printf("Case #%d: %.7f\n", cas + 1, answer);
	}
	return 0;
}
