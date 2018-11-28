#include <iostream>
#include <cstring>
#include <cstdio>
#include <vector>
#include <set>
#include <map>
#include <queue>
#include <algorithm>
#include <stack>
#include <cctype>
#include <cmath>
#include <vector>
#include <sstream>
#include <bitset>
#include <deque>
#include <iomanip>
using namespace std;
#define pr(x) cout << #x << " = " << x << endl;
#define bug cout << "bugbug" << endl;
#define ppr(x, y) printf("(%d, %d)\n", x, y);
#define MST(a,b) memset(a,b,sizeof(a))
#define CLR(a) MST(a,0)
#define SQR(a) ((a)*(a))
#define PCUT puts("\n---------------")

typedef long long ll;
typedef double DBL;
typedef pair<int, int> P;
typedef unsigned int uint;
const int MOD = 1e9 + 7;
const int inf = 0x3f3f3f3f;
const ll INF = 0x3f3f3f3f3f3f3f3f;
const int maxn = 1e3 + 4;
const int maxm = 1e4 + 4;
const double pi = acos(-1.0);
char s[maxn];
int sub[maxn];
int main(){
//必须编译过才能交
	int ik, i, j, k, kase;
	freopen("A-large.in", "r", stdin);
	freopen("output.txt", "w", stdout);
	scanf("%d", &kase);
	for (ik = 1; ik <= kase; ++ik){
		scanf("%s%d", s, &k);
		int len = strlen(s);
		int cnt = 0, ans = 0;
		memset(sub, 0, sizeof sub);
		for (i = 0; i <= len - k; ++i){
			int kind = s[i] == '+' ? 1 : 0;
			cnt -= sub[i];
			kind = (kind + cnt) % 2;
//			cout << i << ' ' << kind << endl;
			if (kind == 0){
				cnt++;
				sub[i+k] = 1;
				ans++;
			}
		}
		bool flag = true;
		for (; i < len; ++i){
			int kind = s[i] == '+' ? 1 : 0;
			cnt -= sub[i];
			kind = (kind + cnt) % 2;
			if (kind == 0) flag = false;
		}
		printf("Case #%d: ", ik);
		if (flag) printf("%d\n", ans);
		else puts("IMPOSSIBLE");
	} 
	return 0;
}

