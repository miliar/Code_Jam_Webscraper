#include <bits/stdc++.h>
using namespace std;
using ll = long long;
const ll MOD = 1000000007;

int memo[100][100][100][4];
int P;

int dfs(int r1, int r2, int r3, int p){
    if(r1 == 0 && r2 == 0 && r3 == 0) return 0;
    if(memo[r1][r2][r3][p] != -1) return memo[r1][r2][r3][p];
    int ret = 0;
    if(r1 > 0){
        ret = max(ret, dfs(r1-1, r2, r3, (p + 1) % P));
    }
    if(r2 > 0){
        ret = max(ret, dfs(r1, r2-1, r3, (p + 2) % P));
    }
    if(r3 > 0){
        ret = max(ret, dfs(r1, r2, r3-1, (p + 3) % P));
    }
    if(p == 0) ret++;
    memo[r1][r2][r3][p] = ret;
    return ret;
}

int main(){
    int T;
    cin >> T;
    for(int t=1;t<=T;t++){
        int N;
        cin >> N >> P;
        vector<int> count(4, 0);
        for(int i=0;i<N;i++){
            int g;
            cin >> g;
            count[g % P]++;
        }
        int ans = count[0];
        memset(memo, -1, sizeof(memo));
        ans += dfs(count[1], count[2], count[3], 0);
        printf("Case #%d: %d\n", t, ans);
    }

    return 0;
}