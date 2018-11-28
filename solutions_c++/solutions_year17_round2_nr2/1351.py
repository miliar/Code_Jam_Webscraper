// #pragma comment(linker,"/STACK:102400000,102400000")
#include <set>
#include <map>
#include <list>
#include <queue>
#include <stack>
#include <cmath>
#include <string>
#include <cstdio>
#include <vector>
#include <sstream>
#include <cstdlib>
#include <cstring>
#include <iostream>
#include <algorithm>

#include <string>
#include <sstream>
#include <iomanip>
#include <iostream>
#include <fstream>
// #include <unordered_set>

using namespace std;

#define FF first
#define SS second
#define MP make_pair
#define PB push_back
#define lson rt << 1, l, mid
#define rson rt << 1 | 1, mid + 1, r
#define FOR(i, n, m) for(int i = n; i <= m; i++)
#define REP(i, n, m) for(int i = n; i >= m; i--)
#define ll long long

typedef long long LL;
typedef pair<int,int> PII;
typedef pair<LL, LL> PLL;
typedef unsigned long long ULL;

const int maxn = 1100;

int n;
char ch[maxn] = {'R', 'O', 'Y', 'G', 'B', 'V'};
int cnt[maxn];
int r, o, y, g, b, v;
char ans[maxn];

void solve() {
    memset(ans, 0, sizeof(ans));
	FOR(i, 0, 5){
		if (cnt[i] > n/2) {
			cout << "IMPOSSIBLE" << endl;
			return;
		}
	}
	int index = 0;
	int mi, ma = -1;
    FOR(i, 0, 5){
		if (cnt[i] > ma) ma = cnt[i], mi = i;
	}
	for (int i = 0; i < cnt[mi]; i ++ ) {
		ans[index] = ch[mi];
		index += 2;
		if (index >= n) {
			index = 1;
		}
	}
	FOR(i, 0, 5){
		if (i != mi) {
			for (int j = 0; j < cnt[i]; j ++ ) {
				ans[index] = ch[i];
				index += 2;
				if (index >= n) {
					index = 1;
				}
			}
		}
	}
	ans[n] = '\0';
	printf("%s\n", ans);
}
int main(){
        freopen("B-small-attempt0.in", "r", stdin);
        freopen("B-small.out", "w", stdout);
        int T;
        cin >> T;
        int cas = 0;
        while(T--){
            cas++;
            cin >> n;
            FOR(i, 0, 5) cin >> cnt[i];
            printf("Case #%d: ", cas);
            solve();
            }
        return 0;
        }
