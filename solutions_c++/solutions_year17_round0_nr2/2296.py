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

long long dp[55][11][2];

int main(){
	freopen("1.in","r",stdin);	
	freopen("1.out","w",stdout);
	int T;
	cin >> T;
	for (int tt = 1; tt <= T; tt++) {
		string s;
		cin >> s;
		for (int i = 0; i <= s.size(); i++) for (int j = 0; j < 10; j++) for (int o = 0; o< 2; o++) dp[i][j][o] = -1;
		dp[0][0][1] = 0;

		for (int i = 0; i < s.size(); i++) for (int j = 0; j < 10; j++) for (int o = 0; o < 2; o++) if (dp[i][j][o] >= 0) {
			for (int c = j; c < 10; c++) {
				if (o == 1 && c > s[i] - '0') continue;

				int oo = o;
				if (c < s[i] - '0') oo = 0;
				dp[i + 1][c][oo] = max(dp[i + 1][c][oo], dp[i][j][o] * 10 + c);
			}
		}
		long long ans = -1;
		for (int j = 1; j < 10; j++) ans = max(ans, max(dp[s.size()][j][0], dp[s.size()][j][1]));

		cout << "Case #" << tt << ": " << ans << endl;
		

	}
	return 0;
}