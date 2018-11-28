#define _CRT_SECURE_NO_WARNINGS
#include<iostream>
#include<sstream>
#include<cstdio>
#include<cstdlib>
#include<cstring>
#include<climits>
#include<cmath>
#include<string>
#include<vector>
#include<set>
#include<map>
#include<queue>
#include<numeric>
#include<functional>
#include<algorithm>
#include<bitset>
#include<tuple>
#include<unordered_set>
#include<random>
#include<array>
#include<cassert>
using namespace std;
#define INF (1<<29)
#define rep(i,n) for(int i=0;i<(int)(n);i++)
#define all(v) v.begin(),v.end()
#define uniq(v) v.erase(unique(all(v)),v.end())


bool fc[1440], fj[1440];
int dp[1441][721][2];

int main() {
	ios::sync_with_stdio(0);
	cin.tie(0);

	int t;
	cin>>t;
	rep(_t,t){
		int ac,aj;
		cin>>ac>>aj;
		int cc[100], dc[100];
		int cj[100], dj[100];
		rep(i, ac)cin >> cc[i] >> dc[i];
		rep(i, aj)cin >> cj[i] >> dj[i];
		int ans=INF;

		memset(fc,false,sizeof(fc));
		memset(fj,false,sizeof(fj));
		rep(i, ac)for (int j = cc[i]; j<dc[i]; j++)fc[j]=true;
		rep(i, aj)for (int j = cj[i]; j<dj[i]; j++)fj[j] = true;

		if (!fc[0]){
			rep(i, 1441)rep(j,721)rep(k, 2)dp[i][j][k] = INF;
			dp[1][1][0] = 0;
			for (int i=1;i<1440;i++)rep(j,721){
				if (j < 720 && !fc[i]){
					dp[i + 1][j + 1][0] = min(dp[i + 1][j + 1][0], dp[i][j][0]);
					dp[i + 1][j + 1][0] = min(dp[i + 1][j + 1][0], dp[i][j][1] + 1);
				}
				if (i - j < 720 && !fj[i]){
					dp[i + 1][j][1] = min(dp[i + 1][j][1], dp[i][j][0] + 1);
					dp[i + 1][j][1] = min(dp[i + 1][j][1], dp[i][j][1]);
				}
			}
			ans = min(ans, dp[1440][720][0]);
			ans = min(ans, dp[1440][720][1]+1);
		}
		if (!fj[0]){
			rep(i, 1441)rep(j, 721)rep(k, 2)dp[i][j][k] = INF;
			dp[1][0][1] = 0;
			for (int i = 1; i<1440; i++)rep(j, 721){
				if (j < 720 && !fc[i]){
					dp[i + 1][j + 1][0] = min(dp[i + 1][j + 1][0], dp[i][j][0]);
					dp[i + 1][j + 1][0] = min(dp[i + 1][j + 1][0], dp[i][j][1] + 1);
				}
				if (i - j < 720 && !fj[i]){
					dp[i + 1][j][1] = min(dp[i + 1][j][1], dp[i][j][0] + 1);
					dp[i + 1][j][1] = min(dp[i + 1][j][1], dp[i][j][1]);
				}
			}
			ans = min(ans, dp[1440][720][0] + 1);
			ans = min(ans, dp[1440][720][1]);
		}

		cout << "Case #" << _t + 1 << ": "<<ans<<endl;
	}

	return 0;
}