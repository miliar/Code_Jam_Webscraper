#include <iostream>
#include <string>
#include <vector>
#include <set>
#include <map>
#include <queue>
#include <stack>
#include <utility>
#include <algorithm>
#include <cmath>
#include <cstdio>
#include <cstdlib>
#include <cstring>
using namespace std;

#define fi first
#define se second
typedef long long ll;
typedef pair<int,int> pii;
typedef pair<ll,ll> pll;

short dp[101][101][101];

int solve(int i, int j, int k, int P, int rest) {
	if(dp[i][j][k]+1) {
		return dp[i][j][k];
	}
	int res = 0;
	int add = 0;
	if(rest % P == 0) add = 1;
	if(2 <= P && i) {
		res = max(res, solve(i-1,j,k,P,(rest+P-1)%P) + add);
	}
	if(3 <= P && j) {
		res = max(res, solve(i,j-1,k,P,(rest+P-2)%P) + add);
	}
	if(4 <= P && k) {
		res = max(res, solve(i,j,k-1,P,(rest+P-3)%P) + add);
	}
	return dp[i][j][k] = res;
}

int main() {
	int T;
	cin >> T;
	for(int t = 0; t < T; t++) {
		int N, P;
		cin >> N >> P;
		vector<int> G(N);
		for(int i = 0; i < G.size(); i++) cin >> G[i];
		int cnt[4] = {};
		for(int i = 0; i < G.size(); i++) {
			cnt[G[i] % P]++;
		}
		memset(dp,-1,101*101*101*sizeof(short));
		int res = 0;
		res = cnt[0];

		cout << "Case #" << t+1 << ": " << res+solve(cnt[1],cnt[2],cnt[3],P,0) << endl;
	}
	return 0;
}
