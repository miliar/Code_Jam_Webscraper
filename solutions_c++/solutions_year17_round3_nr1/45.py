#include <bits/stdc++.h>
using namespace std;

long long dp[1111][1111];
int r[1111], h[1111];
double PI = acos(-1);

long long circle(long long r){
    return r * r;
}

long long side(long long r, long long h){
    return 2 * r * h;
}

vector< pair<int,int> > arr;

double solve(){
    for(int i = 0; i < 1111; i++)
	for(int j = 0; j < 1111; j++)
	    dp[i][j] = 0;
    arr.clear();

    int n,k;
    cin >> n >> k;
    for(int i = 1; i <= n; i++){
	cin >> r[i] >> h[i];
	arr.push_back({r[i], h[i]});
    }

    sort(arr.begin(), arr.end());
    reverse(arr.begin(), arr.end());

    for(int i = 0; i < n; i++){
	r[i + 1] = arr[i].first;
	h[i + 1] = arr[i].second;
    }

    for(int i = 1; i <= n; i++){
	for(int j = 1; j <= i; j++){
	    dp[i][j] = dp[i - 1][j];
	    if(j == 1)
		dp[i][j] = max(dp[i][j], circle(r[i]) + side(r[i], h[i]));
	    else
		dp[i][j] = max(dp[i][j], dp[i - 1][j - 1] + side(r[i], h[i]));
	}
    }

    return dp[n][k] * PI;
}

int main(){
    int t;
    cin >> t;
    for(int i = 1; i <= t; i++){
	printf("Case #%d: %.7f\n", i, solve());
    }
    return 0;
}
