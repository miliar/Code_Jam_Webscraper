#include <bits/stdc++.h>

#define rep(i, n) for(int i = 0; i < n; i ++)
typedef long long LL;
const int N = 1000 + 5;

struct Pos {
	int K, speed;
} horses[N];

int main() {
	int T, D, n;
	scanf("%d", &T);
	rep(cas, T) {
		scanf("%d%d", &D, &n);
		rep(i, n) {
			scanf("%d%d", &horses[i].K, &horses[i].speed);
		}
		double min_time = -1.0;
		rep(i, n) {
			min_time = std::max(min_time, (D-horses[i].K*1.0)/horses[i].speed);
			rep(j, n) if (i != j) {
				if (horses[i].speed >= horses[j].speed && horses[i].K > horses[j].K) {
					continue;
				}
				if (horses[j].speed >= horses[i].speed && horses[j].K > horses[i].K) {
					continue;
				}
				int min_speed = std::min(horses[i].speed, horses[j].speed);
				int max_speed = std::max(horses[i].speed, horses[j].speed);
				int min_k = D - std::max(horses[i].K, horses[j].K);
				int max_k = D - std::min(horses[i].K, horses[j].K);
				int dist = abs(horses[i].K - horses[j].K);
				int d_speed = abs(horses[i].speed - horses[j].speed);
				if (d_speed == 0) {
					min_time = std::max(min_time, max_k*1.0/min_speed);
					continue;
				}
				double catch_time = 1.0 * dist / d_speed;
				if (max_speed * catch_time <= max_k) {
					min_time = std::max(min_time, min_k*1.0/min_speed);
				} else {
					min_time = std::max(min_time, max_k*1.0/max_speed);
				}
			}
		}
		printf("Case #%d: %.7f\n", cas + 1, D*1.0 / min_time);
	}
	return 0;
}
