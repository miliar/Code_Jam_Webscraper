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
		char S[1001];
		scanf("%s", S);
		int n = (int)strlen(S);
		int K;
		scanf("%d", &K);
		int ans = 0;
		rer(i, 0, n - K) {
			if (S[i] == '-') {
				++ ans;
				rep(j, K)
					S[i + j] = S[i + j] == '+' ? '-' : '+';
			}
		}
		printf("Case #%d: ", ii + 1);
		if (count(S, S + n, '+') == n)
			printf("%d\n", ans);
		else
			puts("IMPOSSIBLE");
	}
	return 0;
}
