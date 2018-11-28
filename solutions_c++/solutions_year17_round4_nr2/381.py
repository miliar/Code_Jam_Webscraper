#include <set>
#include <map>
#include <queue>
#include <stack>
#include <cmath>
#include <string>
#include <cctype>
#include <cstdio>
#include <vector>
#include <cstdlib>
#include <cstring>
#include <iomanip>
#include <sstream>
#include <iostream>
#include <algorithm>
using namespace std;
#define ls id<<1,l,mid
#define rs id<<1|1,mid+1,r
#define OFF(x) memset(x,-1,sizeof x)
#define CLR(x) memset(x,0,sizeof x)
#define MEM(x) memset(x,0x3f,sizeof x)
typedef long long ll ;
typedef pair<int,int> pii ;
const int maxn = 1e5 + 50 ;
const int maxm = 1e6 + 50;
const double eps = 1e-10;
const int max_index = 62;
const int inf = 0x3f3f3f3f ;
const int MOD = 1e9+7 ;

inline int read(){
    char c = getchar();
    while (!isdigit(c)) c = getchar();
    int x = 0;
    while (isdigit(c)) {
        x = x * 10 + c - '0';
        c = getchar();
    }
    return x;
}

std::vector<int> loc[1005];
int dp[1005];

bool check(int x, int n) {
	int temp = 0;
	for (int i = 1; i <= n; i++) {
		temp += dp[i];
		if (temp > i * x) return 0;
	}	
	return 1;
}

int main() {
#ifdef zzblack
	freopen("C:\\Users\\zzblack\\Desktop\\case.in","r",stdin);
     freopen("C:\\Users\\zzblack\\Desktop\\case.out","w",stdout);
#endif
	int T = read(), cas = 1;
	while (T--) {
		printf("Case #%d: ", cas++);
		memset(dp, 0, sizeof dp);
		int n = read(), c = read(), m = read();
		for (int i = 1; i <= c; i++) loc[i].clear();
		for (int i = 1; i <= m; i++) {
			int p = read(), b = read();
			loc[b].push_back(p);
		}
		int l = 0, r = m;
		for (int i = 1; i <= c; i++) {
			l = max(l, (int)loc[i].size());
			for (int j = 0; j < loc[i].size(); j++) {
				dp[loc[i][j]]++;
			}
		}
		while (l < r) {
			int mid = l + r >> 1;
			if (check(mid, n)) r = mid;
			else l = mid + 1;
		}
		int ansl = l;
		int temp = 0, ansr = 0;
		for (int i = 1; i <= n; i++) {
			if (dp[i] > ansl) ansr += dp[i] - ansl;
		}
		printf("%d %d\n", ansl, ansr);
	}

	return 0;
}
