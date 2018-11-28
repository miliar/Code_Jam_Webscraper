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


int main() {
#ifdef zzblack
	freopen("C:\\Users\\zzblack\\Desktop\\case.in","r",stdin);
     freopen("C:\\Users\\zzblack\\Desktop\\case.out","w",stdout);
#endif
	int T = read(), cas = 1;
	while (T--) {
		int a[4] = {0, 0, 0, 0};
		int n = read(), p = read();
		for (int i = 0; i < n; i++) {
			int x = read();
			a[x%p] ++;
		}
		int ans = a[0];
		if (p == 2) {
			ans += a[1] / 2;
			if (a[1] % 2) ans++;
		} else if (p == 3) {
			ans += min(a[1], a[2]);
			int x = abs(a[1] - a[2]);
			ans += x / 3;
			if (x % 3) ans++;
		} else {
			ans += a[2] >> 1;
			a[2] %= 2;
			ans += min(a[1], a[3]);
			int x = abs(a[1] - a[3]);
			x += a[2] * 2;
			ans += x / 4;
			if (x % 4) ans++;
		}
		// if (ans != a[0]) ans++;
		printf("Case #%d: %d\n", cas++, ans);
	}

	return 0;
}
