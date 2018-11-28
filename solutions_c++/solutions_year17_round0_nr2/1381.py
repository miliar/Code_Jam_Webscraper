#include <bits/stdc++.h>
using namespace std;

int dp[20][10][2];
vector<int> digs;
long long ans = 0;

int solve(int idx, int last, int tight){
    if(idx == digs.size()) return 1;
    else if(dp[idx][last][tight] >= 0) return dp[idx][last][tight];
    int ret = 0;
    int st = 9;
    if(tight) st = digs[idx];
    for(int i = st; i >= last; i--)
	ret |= solve(idx + 1, i, tight & (i == digs[idx]));
    return (dp[idx][last][tight] = ret);
}

void trace(int idx, int last, int tight){
    if(idx == digs.size()) return;
    int st = 9;
    if(tight) st = digs[idx];
    for(int i = st; i >= last; i--)
	if(solve(idx + 1, i, tight & (i == digs[idx])) == 1){
	    ans = ans * 10 + i;
	    trace(idx + 1, i, tight & (i == digs[idx]));
	    return;
	}
}

void pre(long long n){
    memset(dp, -1, sizeof(dp));
    ans = 0;
    digs.clear();
    while(n){
	digs.push_back(n%10);
	n /= 10;
    }
    reverse(digs.begin(), digs.end());
}

long long solve(){
    long long n;
    cin >> n;
    pre(n);
    solve(0, 0, 1);
    trace(0, 0, 1);
    return ans;
}

int main(){
    int cases;
    cin >> cases;
    for(int t = 1; t <= cases; t++){
	cout << "Case #" << t << ": ";
	cout << solve();
	cout << "\n";
    }
    return 0;
}
