#include <cstdio>
#include <vector>
#include <algorithm>
struct times{
	int s, e, w;
};
bool operator<(times t1, times t2) {
	return t1.s < t2.s;
}
int main() {
	int T;
	scanf("%d", &T);
	for (int tc = 1; tc <= T; tc++) {
		int C, J; 
		scanf("%d%d", &C, &J);
		std::vector<times> D(C+J);
		int remain_C = 720;
		int remain_J = 720;
		for (int i = 0; i < C+J; i++) {
			scanf("%d%d", &D[i].s, &D[i].e);
			D[i].w = i >= C;
			if (i < C) remain_C -= D[i].e - D[i].s;
			else remain_J -= D[i].e - D[i].s;
		}
		std::sort(D.begin(), D.end());
		std::vector<int> CNU, JNU;
		int tot = 0;
		for (int i = 0; i < D.size(); i++) {
			int next = (i + 1) % D.size();
			if (D[i].w == D[next].w) {
				int v = (D[next].s - D[i].e + 24 * 60) % (24 * 60);
				if (D[i].w == 0) CNU.push_back(v);
				if (D[i].w == 1) JNU.push_back(v);
			}
			else tot++;
		}
		std::sort(CNU.begin(), CNU.end());
		std::sort(JNU.begin(), JNU.end());
		for (int i = 0; i < CNU.size(); i++) {
			if (remain_C - CNU[i] >= 0) remain_C -= CNU[i];
			else tot += 2;
		}
		for (int i = 0; i < JNU.size(); i++) {
			if (remain_J - JNU[i] >= 0) remain_J -= JNU[i];
			else tot += 2;
		}
		printf("Case #%d: %d\n",tc, tot);

	}
}