#include <cstdio>
#include <cstdlib>
#include <cstring>
#include <cmath>
#include <map>
#include <vector>
#include <algorithm>

using namespace std;

#define MIN(x,y) ((x)<(y)?(x):(y))

int tn;
int R[200];
int Q[100][100];
int N, P;

vector<pair<int,int> > A[100];
int p[100];

pair<int, int> get_servings(int quot, int quant) {

	int smax = (int)((double)quant / (0.9 * quot));
	while (0.9*quot*smax > quant) smax --;
	while (0.9*quot*smax <= quant) smax ++;
	smax --;

	int smin = (int)((double)quant / (1.1 * quot));
	while (1.1*quot*smin < quant) smin ++;
	while (1.1*quot*smin >= quant) smin --;
	smin ++;

	return make_pair(smin, smax);

}

int main() {

	scanf("%d", &tn);
	for(int ctn = 0; ctn < tn; ctn ++) {

		scanf("%d %d", &N, &P);
		for(int i = 0; i < N; i++)
			scanf("%d", &R[i]);
		for(int i = 0; i < N; i++)
			for(int j = 0; j < P; j++)
				scanf("%d", &Q[i][j]);

		for(int i = 0; i < N; i++) {
			A[i].clear();
			for(int j = 0; j < P; j++) {
				pair<int, int> s = get_servings(R[i], Q[i][j]);
				if (s.first <= s.second) {
					A[i].push_back(s);
				}
			}
			sort(A[i].begin(), A[i].end());
		}

		for(int i = 0; i < N; i++) p[i] = 0;
		int ans = 0;
		bool terminated = false;
		for(int i = 0; i < N; i++)
			if (p[i] == A[i].size()) terminated = true;
		while (!terminated) {
			// find the smallest i with smin
			int smin = 1000000, imin = -1;
			for(int i = 0; i < N; i++)
				if (A[i][p[i]].first < smin) {
					smin = A[i][p[i]].first;
					imin = i;
				}
			// check whether this serve is valid
			pair<int, int> s = A[imin][p[imin]];
			bool flag = true;
			for(int i = 0; i < N; i++) {
				if (A[i][p[i]].first > s.second) {
					flag = false;
					break;
				}
			}
			if (flag) {
				// valid serving
				ans ++;
				for(int i = 0; i < N; i++) {
					p[i] ++;
					if (p[i] == A[i].size()) terminated = true;
				}
			}
			else {
				// invalid serving
				p[imin] ++;
				if (p[imin] == A[imin].size()) terminated = true;
			}
		}

		printf("Case #%d: %d\n", ctn+1, ans);

	}

	return 0;

}