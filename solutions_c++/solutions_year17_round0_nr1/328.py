#include <vector>
#include <string>
#include <iostream>
#include <algorithm>
#include <queue>
#include <set>
#include <map>
#include <sstream>
#include <iomanip>
#include <cstdio>
#include <cstdlib>
#include <cstring>
#include <cmath>
#include <ctime>
#include <cassert>
using namespace std;
typedef long long ll;
typedef double R;
#define pb push_back
#define mp make_pair
#define fi first
#define se second
#define FOR(i, s, t) for(i = (s); i < (t); i++)
#define RFOR(i, s, t) for(i = (s)-1; i >= (t); i--)

const R PI = acos(-1);
const int MAXN = 1<<20;
const int P = 1e9+7;

int a[MAXN];
char s[MAXN];

int main(){
#ifdef LOCAL
	//freopen("in.txt", "r", stdin);
	//freopen("out.txt", "w", stdout);
#endif
	int T, i0;
	scanf("%d", &T);
	for(i0 = 1; i0 <= T; i0++){
		int n, k;
		int i, j;
		int ans = 0;
		scanf("%s%d", s, &k);
		n = strlen(s);
		for(i = 0; i < n; i++)
			a[i] = s[i] == '-';
		for(i = 0; i < n; i++){
			if(a[i]){
				if(i+k > n)
					break;
				ans++;
				for(j = 0; j < k; j++)
					a[i+j] ^= 1;
			}
		}
		printf("Case #%d: ", i0);
		if(i == n)
			printf("%d\n", ans);
		else
			puts("IMPOSSIBLE");
	}
	return 0;
}
