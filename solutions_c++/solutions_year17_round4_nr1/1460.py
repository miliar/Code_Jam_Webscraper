#include <cstdio>
#include <cstring>
#include <cmath>
#include <algorithm>
#include <vector>
#include <string>
#include <set>
#include <map>
#include <queue>
#define mp make_pair
#define pb push_back
#define fir first
#define sec second
using namespace std;
typedef long long ll;

template <typename T> inline void R(T &x) {
	char ch = getchar(); x = 0;
	for (; ch<'0' || ch>'9'; ch = getchar());
	for (; ch<='9' && ch>='0'; ch=getchar()) x = x*10 + ch-'0';
}
const int N = 105;
int cnt[4], n, p;
int dp3[N][N], dp4[N][N][N];
vector<int> poss3, poss4;
void run() {
	scanf("%d%d", &n, &p);
	memset(cnt, 0, sizeof(cnt));
	int x;
	for (int i=1; i<=n; ++i) {
		scanf("%d", &x);
		cnt[x % p]++;
	}
	if (p == 2)
		printf("%d\n", cnt[0] + (cnt[1] + 1) / 2); else
	if (p == 3)
		printf("%d\n", cnt[0] + dp3[cnt[1]][cnt[2]]); else
		printf("%d\n", cnt[0] + dp4[cnt[1]][cnt[2]][cnt[3]]);
}
void pre() {
	for (int i=0; i<=3; ++i)
		for (int j=0; j<=3; ++j)
			if ((i || j) && ((i + j * 2) % 3 == 0))
				poss3.pb((i << 7) | j);
	for (int i=0; i<=100; ++i)
		for (int j=0; j<=100; ++j) {
			if (i || j)
				dp3[i][j] = 1; else
				dp3[i][j] = 0;
			for (int S : poss3) {
				int _i = S >> 7, _j = S & 127;
				if (i >= _i && j >= _j)
					dp3[i][j] = max(dp3[i][j], dp3[i - _i][j - _j] + 1);
			}
		}
	for (int i=0; i<=4; ++i)
		for (int j=0; j<=4; ++j)
			for (int k=0; k<=4; ++k)
				if ((i || j || k) && (i + j * 2 + k * 3) % 4 == 0)
					poss4.pb((i << 14) | (j << 7) | k);
	for (int i=0; i<=100; ++i)
		for (int j=0; j<=100; ++j)
			for (int k=0; k<=100; ++k) {
				dp4[i][j][k] = (i || j || k);
				for (int S : poss4) {
					int _i = S >> 14, _j = (S >> 7) & 127, _k = S & 127;
					if (i >= _i && j >= _j && k >= _k)
						dp4[i][j][k] = max(dp4[i][j][k], dp4[i - _i][j - _j][k - _k] + 1);
				}
			}
}
int main( ){
	pre();
	int T; R(T);
	for (int i=1; i<=T; ++i) {
		printf("Case #%d: ", i);
		run();
	}
	return 0;
}