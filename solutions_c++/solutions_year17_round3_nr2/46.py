#include <bits/stdc++.h>
using namespace std;

int dp[1450][722][2][2];
bool busy[2][1450];

int solve(int tot, int one, int has, int md){
    if( max(tot - one, one) > 720) return 1000000;
    else if(tot == 1440){
	return (has != md);
    }
    else if(dp[tot][one][has][md] != -1) return dp[tot][one][has][md];
    int ret = 1000000;

    if(busy[0][tot] == 0){
	ret = min(ret, solve(tot + 1, one + 1, 0, md) + has);
    }

    if(busy[1][tot] == 0){
	ret = min(ret, solve(tot + 1, one, 1, md) + 1 - has);
    }

    //cout << tot << " " << one << " " << has << " " << ret << "\n";

    return (dp[tot][one][has][md] = ret);
}

int solve(){
    memset(busy,0,sizeof(busy));
    memset(dp, -1, sizeof(dp));

    int n,m;
    cin >> n >> m;

    for(int i = 1; i <= n; i++){
	int l,r;
	cin >> l >> r;
	for(int j = l; j < r; j++)
	    busy[0][j] = 1;
    }

    for(int i = 1; i <= m; i++){
	int l,r;
	cin >> l >> r;
	for(int j = l; j < r; j++)
	    busy[1][j] = 1;
    }

    return min(solve(0, 0, 0, 0), solve(0, 0, 1, 1));
}

int main(){
    int t;
    cin >> t;
    for(int i = 1; i <= t; i++)
	cout << "Case #" << i << ": " << solve() << "\n";
    return 0;
}
