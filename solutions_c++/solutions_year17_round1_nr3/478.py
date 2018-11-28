#include <iostream>
#include <cstdio>
#include <cstring>
#include <queue>

using namespace std;

struct State {
	int dH, dA, kH, kA;
};
int b, d;
queue<State> que;
int dis[101][101][101][101];

int main() {
	int testCases;
	cin >> testCases;
	for (int _ = 1; _ <= testCases; ++_) {
		State s0;
		cin >> s0.dH >> s0.dA >> s0.kH >> s0.kA >> b >> d;
		int dH0 = s0.dH;
		memset(dis, -1, sizeof dis);
		dis[s0.dH][s0.dA][s0.kH][s0.kA] = 0;
		
		for (; !que.empty(); que.pop());
		que.push(s0);
		int ret = -1;
		for (; !que.empty(); que.pop()) {
			State s1 = que.front();
			State s2;

			s2 = s1;
			s2.kH -= s2.dA;
			if (s2.kH <= 0) {
				ret = dis[s1.dH][s1.dA][s1.kH][s1.kA] + 1;
				break;
			}
			s2.dH -= s2.kA;
			if (s2.dH > 0 && dis[s2.dH][s2.dA][s2.kH][s2.kA] == -1) {
				que.push(s2);
				dis[s2.dH][s2.dA][s2.kH][s2.kA] = dis[s1.dH][s1.dA][s1.kH][s1.kA] + 1;
			}

			s2 = s1;
			s2.dA = min(s2.dA + b, 100);
			s2.dH -= s2.kA;
			if (s2.dH > 0 && dis[s2.dH][s2.dA][s2.kH][s2.kA] == -1) {
				que.push(s2);
				dis[s2.dH][s2.dA][s2.kH][s2.kA] = dis[s1.dH][s1.dA][s1.kH][s1.kA] + 1;
			}

			s2 = s1;
			s2.kA = max(0, s2.kA - d);
			s2.dH -= s2.kA;
			if (s2.dH > 0 && dis[s2.dH][s2.dA][s2.kH][s2.kA] == -1) {
				que.push(s2);
				dis[s2.dH][s2.dA][s2.kH][s2.kA] = dis[s1.dH][s1.dA][s1.kH][s1.kA] + 1;
			}

			s2 = s1;
			s2.dH = dH0;
			s2.dH -= s2.kA;
			if (s2.dH > 0 && dis[s2.dH][s2.dA][s2.kH][s2.kA] == -1) {
				que.push(s2);
				dis[s2.dH][s2.dA][s2.kH][s2.kA] = dis[s1.dH][s1.dA][s1.kH][s1.kA] + 1;
			}
		}

		if (ret == -1) {
			printf("Case #%d: IMPOSSIBLE\n", _);
		} else {
			printf("Case #%d: %d\n", _, ret);
		}
	}
	return 0;
}
