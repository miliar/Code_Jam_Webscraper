#include <iostream>
#include <fstream>
#include <cstdio>
#include <cmath>
#include <vector>
#include <cstring>
#include <string>
#include <set>
#include <map>
#include <stack>
#include <queue>
#include <algorithm>
using namespace std;

#define REP(i,n) for(int i=0; i<n; ++i)
#define FOR(i,a,b) for(int i=a; i<=b; ++i)
#define FORR(i,a,b) for (int i=a; i>=b; --i)
#define ALL(c) (c).begin(), (c).end()

typedef long long ll;
typedef vector<int> VI;
typedef vector<ll> VL;
typedef vector<VI> VVI;
typedef pair<int,int> P;
typedef pair<ll,ll> PL;

int main(void) {
	ifstream ifs("input.txt");
	ofstream ofs("out.txt");
	FILE *fp;
	fp = fopen("out.txt","w");
	int num_of_cases;
	ifs >> num_of_cases;
	REP(cas,num_of_cases){
		fprintf(fp,"Case #%d: ",cas+1);
		printf("Case #%d: ",cas+1);

		string s;
		ifs >> s;
		int n = s.length();

		vector<vector<vector<ll> > > dp(n+1, vector<vector<ll> > (10, vector<ll> (2,-1)));
		dp[0][0][0] = 0;
		REP(i,n) REP(j,10) REP(k,2){
			if (dp[i][j][k] == -1) continue;
			int lim = (k == 1 ? 9 : s[i] - '0');
			FOR(l,j,lim){
				int p = (k | (l < s[i] - '0'));
				dp[i+1][l][p] = max(dp[i+1][l][p], 10 * dp[i][j][k] + l);
			}
		}

		ll ans = 0;
		FOR(j,1,9) REP(k,2) ans = max(ans, dp[n][j][k]);

		cout << ans << endl;
		fprintf(fp, "%lld\n", ans);
	}

	return 0;
}