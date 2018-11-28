#include<bits/stdc++.h>
using namespace std;

#define int long long
const int MAXN = 1e6 + 100;
ofstream fout("out.txt");
#define cout fout

int r[MAXN] , h[MAXN] , srt[MAXN];
int dp[MAXN] ;
bool cmp(int a , int b){
    if(r[a] == r[b])
        return h[a] < h[b] ;
    return r[a] < r[b] ;
}
int area(int R , int H){ return R * 2 * H ; }
int32_t main(){
    int t ; cin >> t ;
    for(int _ = 1 ; _ <= t ; _ ++){
        memset(dp , 0 , sizeof dp);
        int n ; cin >> n ;
        int k ; cin >> k ;
        for(int i = 0 ; i < n ; i ++)
            cin >> r[i] >> h[i];
        for(int i = 0 ; i < n ; i ++)
            srt[i] = i ;
        sort(srt  , srt + n , cmp) ;

        int ans = 0 ;
        for(int i = 0 ; i < n ; i ++){
            int now = srt[i] ;
            ans = max(dp[k - 1] + r[now] * r[now] + area(r[now] , h[now]) , ans) ;
            for(int j = k - 1 ; j > 0 ; j --)
                dp[j] = max(dp[j] , dp[j - 1] + area(r[now] , h[now])) ;
        }
        cout << fixed << setprecision(9);
        cout << "Case #" << _ << ": " ;
        cout << 1.00 * ans * M_PI << '\n' ;
    }
}
