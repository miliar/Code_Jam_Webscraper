#include <bits/stdc++.h>
using namespace std;
 
typedef pair<int,int> pii;
typedef long long ll;

void fastStream(){cin.tie(0);std::ios_base::sync_with_stdio(0);}


int N, P;
int G[110];
int dp[110][110][110][5];

int dfs(int m1, int m2, int m3, int left){
    if(dp[m1][m2][m3][left] >= 0)
        return dp[m1][m2][m3][left];
    int ans = 0;
    if(m1 == 0 && m2 == 0 && m3 == 0){
        ans = 0;
    }
    else{
        if(m1 > 0){
            ans = max(ans, dfs(m1 - 1, m2, m3, (left - 1 + P) % P) + (left == 0));
        }
        if(m2 > 0){
            ans = max(ans, dfs(m1, m2 - 1, m3, (left - 2 + P) % P) + (left == 0));
        }
        if(m3 > 0){
            ans = max(ans, dfs(m1, m2, m3 - 1, (left - 3 + P) % P) + (left == 0));
        }
    }
    return dp[m1][m2][m3][left] = ans;
}

int main(){
    fastStream();
    int T;
    cin >> T;
    for(int t = 1; t <= T; t++){
        cout << "Case #" << t << ": ";
        cin >> N >> P;
        for(int i = 0; i < N; i++) cin >> G[i];
        int D[4] = {};
        for(int i = 0; i < N; i++){
            D[G[i] % P]++;
        }
        memset(dp, -1, sizeof(dp));
        int ans = D[0];
        ans += dfs(D[1], D[2], D[3], 0);
        cout << ans << endl;
    }
    return 0;
}
