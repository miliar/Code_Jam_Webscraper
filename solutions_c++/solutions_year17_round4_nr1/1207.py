#include <bits/stdc++.h>
using namespace std;
#define mp(X,Y) make_pair(X,Y)
#define F first
#define S second
typedef long long ll;
typedef pair<int,int> PII;
typedef pair<ll,ll> PLL;
int dp[101][101][101];
int cnt[101][101][101];
int num[10];
int main(){
    ios::sync_with_stdio(0);
    freopen("1.in","r",stdin);
    freopen("1.out","w",stdout);
    int cas = 1;
    int t;
    cin >> t;
    while(t--){
        cout << "Case #" << cas ++ << ": ";
        int n,p;
        cin >> n >> p;
        for(int i = 0 ;i < 9 ; i ++)num[i] = 0;
        for(int i = 0 ;i <n ; i ++){
            int a;
            cin >> a;
            a %= p;
            if(a) a= p - a;
            num[a]++;
        }
        for(int i = 0;i <= num[1];i++ ){
            for(int j = 0 ; j <= num[2]; j ++){
                for(int k = 0 ; k <= num[3];k++ ){
                    dp[i][j][k] = 0;
                    cnt[i][j][k] = (i + j * 2 + k * 3) % p;
                    //cout << i << "  " << j << "   " << k << "  " << cnt[i][j][k] <<endl;
                }
            }
        }
        for(int i = 0;i <= num[1];i++ ){
            for(int j = 0 ; j <= num[2]; j ++){
                for(int k = 0 ; k <= num[3];k++ ){
                    if(i){
                        dp[i][j][k] =max(dp[i][j][k], dp[i-1][j][k] + (cnt[i-1][j][k] == 0));

                    }
                    if(j){
                        dp[i][j][k] = max(dp[i][j][k],dp[i][j-1][k] + (cnt[i][j-1][k] == 0));
                    }
                    if(k){
                        dp[i][j][k] = max(dp[i][j][k],dp[i][j][k-1] + (cnt[i][j][k-1] == 0));
                    }
                }
            }
        }
        cout << dp[num[1]][num[2]][num[3]] + num[0] << endl;
       // cout << num[0] <<endl;



    }
    return 0;
}
