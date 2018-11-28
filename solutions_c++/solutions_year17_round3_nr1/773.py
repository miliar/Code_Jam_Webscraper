#include <bits/stdc++.h>

#define rep(i, n) for(int i = 0;i < n;i++)
#define REP(i, a, n) for(int i = a;i < n;i++)
#define all(i) i.begin(), i.end()


using namespace std;

typedef pair<int, int> P;

long double dp[1002][1002];
double PI = acos(-1);

int main(){

    int T;
    cin >> T;

    rep(_, T){
        cout << "Case #" << _ + 1 << ": ";

        int n, k;
        cin >> n >> k;

        vector<P> a(n);
        rep(i, n){
            cin >> a[i].first >> a[i].second;
        }
        sort(all(a));
        reverse(all(a));
        rep(i,1000)rep(j,1000){
            dp[i][j] = -1e9;
        }
        dp[0][0] = 0;
        
        rep(i, n){
            rep(j, k + 1){
                long long r = a[i].first;
                long long h = a[i].second;

                dp[i + 1][j] = max(dp[i + 1][j], dp[i][j]);

                if(j == 0){
                    dp[i + 1][j + 1] = max(dp[i + 1][j + 1], dp[i][j] + r * r + 2.0 * r * h);
                }else{
                    dp[i + 1][j + 1] = max(dp[i + 1][j + 1], dp[i][j] + 2.0 * r * h);
                }
            }
        }

        cout << fixed << setprecision(30) <<dp[n][k] * PI << endl;

    }



    return 0;
}