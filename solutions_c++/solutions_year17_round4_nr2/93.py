#include "bits/stdc++.h"
using namespace std;
#define rep(i,n) for(int (i)=0;(i)<(int)(n);++(i))
#define rer(i,l,u) for(int (i)=(int)(l);(i)<=(int)(u);++(i))
#define reu(i,l,u) for(int (i)=(int)(l);(i)<(int)(u);++(i))
static const int INF = 0x3f3f3f3f; static const long long INFL = 0x3f3f3f3f3f3f3f3fLL;
typedef vector<int> vi; typedef pair<int, int> pii; typedef vector<pair<int, int> > vpii; typedef long long ll;
template<typename T, typename U> static void amin(T &x, U y) { if (y < x) x = y; }
template<typename T, typename U> static void amax(T &x, U y) { if (x < y) x = y; }

int main() {
	int T;
	scanf("%d", &T);
	for (int ii = 0; ii < T; ++ ii) {
		int N; int C; int M;
		scanf("%d%d%d", &N, &C, &M);
		vector<int> degA(C, 0), degB(N, 0);
		rep(i, M) {
			int P; int B;
			scanf("%d%d", &P, &B), -- P, -- B;
			++ degA[B];
			++ degB[P];
		}
		int ans1 = *max_element(degA.begin(), degA.end());
		for (;; ++ ans1) {
			vi v = degB;
			for (int i = N - 1; i > 0; -- i)
				v[i - 1] += max(v[i] - ans1, 0);
			if (v[0] <= ans1) break;
		}
		int ans2 = 0;
		rep(i, N)
			ans2 += max(degB[i] - ans1, 0);
		printf("Case #%d: %d %d\n", ii + 1, ans1, ans2);
	}
	return 0;
}
