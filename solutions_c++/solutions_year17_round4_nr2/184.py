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
const int MAXN = 1<<10;
const int P = 1e9+7;

int cnt1[MAXN];
int cnt2[MAXN];

int main(){
#ifdef LOCAL
	//freopen("in.txt", "r", stdin);
	//freopen("out.txt", "w", stdout);
#endif
	int T, i0;
	scanf("%d", &T);
	for(i0 = 1; i0 <= T; i0++){
		int n, m, c;
		int i, j, k;
		memset(cnt1, 0, sizeof cnt1);
		memset(cnt2, 0, sizeof cnt2);
		scanf("%d%d%d", &n, &c, &m);
		for(i = 0; i < m; i++){
			scanf("%d%d", &j, &k);
			j--;
			k--;
			cnt2[j]++;
			cnt1[k]++;
		}
		int ans = 0;
		int z = 0;
		for(i = 0; i < c; i++)
			ans = max(ans, cnt1[i]);
		int sum = 0;
		for(i = 0; i < n; i++){
			sum += cnt2[i];
			ans = max(ans, (sum+i)/(i+1));
		}
		for(i = n-1; i >= 0; i--){
			z += max(0, cnt2[i] - ans);
		}
		printf("Case #%d: %d %d\n", i0, ans, z);
	}
	return 0;
}
