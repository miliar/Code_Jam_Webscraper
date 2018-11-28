#include<stdlib.h>
#include<stdio.h>
#include<cstring>
#include<string>
#include<vector>
#include<algorithm>
using namespace std;

int n;
typedef long long ll;
string nu;

ll dp[20][10][2];
ll p10[20];

ll rec(int idx, int lastDigit, bool smaller){
	if (idx == n) return 0;
	ll &ret = dp[idx][lastDigit][smaller];
	if (ret != -1) return ret;
	int up = smaller ? 9 : (nu[idx] - '0');
	for (int i = lastDigit; i <= up; i++){
		bool nsmaller = smaller | (i < (nu[idx] - '0'));
		ll tret = rec(idx + 1, i, nsmaller);
		if (tret != -1) ret = i * p10[n-idx] + tret;
	}
	return ret;
}

int main(){
    freopen("B-small-attempt0.in","rt",stdin);
	freopen("B-small-attempt0.out", "w", stdout);
	p10[1] = 10;
	for (int i = 2; i < 19; i++) p10[i] = p10[i - 1] * 10LL;
	int T; scanf("%d", &T);
	for (int tc = 1; tc <= T; tc++){
		ll N; scanf("%lld", &N);
		nu = to_string(N);
		n = nu.size();
		memset(dp, -1, sizeof(dp));
		printf("Case #%d: %lld\n", tc, rec(0, 0, 0)/10LL);
	}
}
