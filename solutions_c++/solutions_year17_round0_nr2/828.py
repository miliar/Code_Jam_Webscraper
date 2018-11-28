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

int main(){
//必须编译过才能交
	int ik, i, j, k, kase;
//	freopen("B-small-attempt0.in", "r", stdin);
	freopen("B-large.in", "r", stdin);
	freopen("output.txt", "w", stdout);
	scanf("%d", &kase);
	for (ik = 1; ik <= kase; ++ik){
		char s[100];
		scanf("%s", s);
		ll result = 0;
		for (i = 0; s[i]; ++i){
			bool ok = false;
			for (j = i+1; s[j]; ++j)
				if (s[j] > s[i]) ok = true;
				else if (s[j] < s[i]) break;
			if (s[j] == 0) ok = true;
			if (ok){
				result = result * 10 + s[i] - '0';
			}else{
				result = result * 10 + s[i] - '0' - 1;
				for (j = i + 1; s[j]; ++j){
					result = result * 10 + 9;
				}
				break;
			}
		} 
		printf("Case #%d: %I64d\n", ik, result);
	}
	return 0;
}

