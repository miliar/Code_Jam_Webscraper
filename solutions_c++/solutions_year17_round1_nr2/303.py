#include <stdio.h>
#include <algorithm>
#include <map>
#include <vector>
#include <deque>

using namespace std;

const int MAX_N = 5e1 + 10, MAX_P = 5e1 + 10;
typedef pair<int, int> pi;

int N, P;
int Nr[MAX_N];
pi isGood(int ix, int x) {
	return  make_pair((x*10-1)/11/Nr[ix] + 1, x*10/9/Nr[ix]);
}

int main() {
	freopen("input.txt", "r", stdin);
	freopen("output.txt", "w", stdout);
	int TC; scanf("%d", &TC);
	for(int tc=1; tc<=TC; tc++) {
		scanf("%d%d", &N, &P);
		deque<int> D[MAX_N];
		for(int i=0; i<N; i++) scanf("%d", &Nr[i]);
		for(int i=0; i<N; i++) {
			for(int j=0, x; j<P; j++) {
				scanf("%d", &x);
				D[i].push_back(x);
			}
			sort(D[i].begin(), D[i].end());
		}
		int ans = 0;
		while(1) {
			bool isOK = true;
			for(int i=0; i<N; i++) if(D[i].size() == 0) {isOK = false; break;}
			if(isOK == false) break;

			int rMin = 0x7fffffff, lMax = -1;
			for(int i=0; i<N; i++) {
				pi inter = isGood(i, D[i].front());
				rMin = min(rMin, inter.second);
				lMax = max(lMax, inter.first);
			}
			if(lMax <= rMin) {
				ans++;
				for(int i=0; i<N; i++) D[i].pop_front();
			} else {
				for(int i=0; i<N; i++) {
					pi inter = isGood(i, D[i].front());
					if(inter.second < lMax) D[i].pop_front();
				}
			}
		}

		printf("Case #%d: %d\n", tc, ans);
	}
	return 0;
}