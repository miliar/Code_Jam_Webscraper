#include<stdio.h>
#include<iostream>
#include<vector>
#include<cmath>
#include<algorithm>
#include<memory.h>
#include<map>
#include<set>
#include<queue>
#include<list>
#include<sstream>
#define mp make_pair
#define pb push_back      
#define F first
#define S second
#define SS stringstream
#define sqr(x) ((x)*(x))
#define m0(x) memset(x,0,sizeof(x))
#define m1(x) memset(x,63,sizeof(x))
#define CC(x) cout << (x) << endl
#define pw(x) (1ll<<(x))
#define M 1000000007
#define N 111111
using namespace std;
typedef pair<int,int> pt;

int dp[1555][722][2];

int can[2][1555];

int main(){
	freopen("1.in","r",stdin);	
	freopen("1.out","w",stdout);
	int T;
	cin >> T;
	for (int tt = 1; tt <= T; tt++) {
		int n1, n2;
		cin >> n1 >> n2;

		for (int i = 0; i <= 24 * 60; i++) can[0][i] = can[1][i] = 1;

		while (n1--) {
			int x, y;
			cin >> x >> y;
			for (int i = x; i < y; i++) can[0][i] = 0;
		}
		while (n2--) {
			int x, y;
			cin >> x >> y;
			for (int i = x; i < y; i++) can[1][i] = 0;
		}

		int ans = 1e9 + 1;

		for (int s = 0; s < 2; s++) {


		for (int i = 0; i <= 24 * 60; i++) for (int j = 0; j <= 720; j++) for (int o = 0; o < 2; o++) dp[i][j][o] = 1e9 + 1;

		dp[0][0][s] = 0;

		for (int i = 0; i < 24 * 60; i++) for (int j = 0; j <= 720; j++) for (int o = 0; o < 2; o++) if (dp[i][j][o] < 1e9) {
			if (can[o][i]) dp[i + 1][j + (o == 0)][o] = min(dp[i + 1][j + (o == 0)][o], dp[i][j][o]);

			if (can[o ^ 1][i]) dp[i + 1][j + (o == 1)][o ^ 1] = min(dp[i + 1][j + (o == 1)][o ^ 1], dp[i][j][o] + 1);
		}

		ans = min(ans, min(dp[24 * 60][720][s], dp[24 * 60][720][s ^ 1] + 1));
		}



		cout << "Case #" << tt << ": " << ans << endl;

	}
	return 0;
}