#include<bits/stdc++.h>
using namespace std;
typedef long long LL;
int n , pp;
int p[4];
int dp[101][101][101];
int main () {
    freopen("input.txt", "r", stdin);
        freopen("output.txt", "w", stdout);
    int t, cas = 0;
    cin >> t;
    while (t --) {
        cout << "Case #" << ++ cas << ": ";
        cin >> n >> pp;
        memset (p, 0 , sizeof (p));
        for(int i = 0 ; i < n ; i ++) {
            int k;cin >> k;
            p[k % pp] ++;
        }
        int ans = p[0];
        if(pp == 2) {
            if(p[1]) {
            int ret = (p[1] + 1) / 2;
            ans += max(ret , 1);
            }
        }
        else if(pp == 3){
            if(p[1] + p[2]) {
            int ret = min(p[1], p[2]); 
            if(p[1] > p[2]) {
                ret += (p[1] - p[2] + 2) / 3;
            }
            else {
                ret += (p[2] - p[1] + 2) / 3;
            }
            ans += max(ret , 1);

            }
        }
        else {
            if(p[1] + p[2] + p[3]) {
            memset (dp, 0 , sizeof (dp));
            for(int i = 0 ; i <= p[1]; i ++) {
                for(int j = 0 ; j <= p[2]; j ++) {
                    for(int k = 0 ; k <= p[3] ; k ++) {
                        for(int x = 0; x <= pp && x + i <= p[1] ; x ++) {
                            for(int y = 0; y <= pp && y + j <= p[2] ; y ++) {
                                for(int z = 0; z <= pp && z + k <= p[3] ; z ++) {
                                    if((x + 2 * y + 3 * z) % pp == 0) {
                                        dp[x + i][y + j][z + k] = max(dp[x + i][y + j][z + k], dp[i][j][k] + 1);
                                    }
                                }
                            }
                        }
                    }
                }
            }
            int ret = dp[p[1]][p[2]][p[3]];
            for(int i = 0 ; i <= p[1] ; i ++) {
                for(int j = 0 ; j <= p[2]; j ++) {
                    for(int k = 0 ; k <= p[3] ; k ++) {
                        if(i != p[1] || j != p[2] || k != p[3]) {
                            ret = max(ret , dp[i][j][k] + 1);
                        }
                    }
                }
            }
            ans += ret;
        }
        }
        cout << ans << endl;
    }

    return 0;
}

