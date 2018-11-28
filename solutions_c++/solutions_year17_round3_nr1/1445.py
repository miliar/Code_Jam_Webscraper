#include <bits/stdc++.h>
using namespace std;

#define endl '\n'

void io(){
    ios_base::sync_with_stdio(false);
    cin.tie(0);
    cout.tie(0);
    cout.precision(15);
}
long long dp[1005][1005] ;
const long double PI = acos(-1.0) ;
vector< pair<long long,long long> > cakes ;
vector< pair<long long,long long> > C ;
int n,k ;
const int INF = 1e9 ;
long long solve(int pos,int rem){
    if(rem == 0){
        return 0 ;
    }
    else if(pos < 0){
        return -INF ;
    }
    long long &ret = dp[pos][rem] ;
    if(ret != -1){
      return ret ;
    }
    ret = 0 ;
    int i = pos ;
    ret = max(cakes[i].first*cakes[i].second + solve(pos - 1,rem - 1), solve(pos - 1,rem)) ;
    return ret ;
}
int main(int argc,char* argv[]) { 
    io() ;
    #ifndef ONLINE_JUDGE
        freopen("A-large.in", "r", stdin) ;
        freopen("out.txt", "w", stdout);
    #endif
    int t ;
    cin >> t ;
    int tc = 0 ;
    while(t--){
        tc++ ;
        cout << "Case #" << tc << ": " ;
        cakes.clear() ;
        long long r,h ;
        cin >> n >> k ;
        for(int i = 1 ; i <= n ; i++){
            cin >> r >> h ;
            cakes.push_back({r,h}) ;
        }
        sort(cakes.rbegin(), cakes.rend()) ;
        C.clear() ;
        // C.push_back(cakes[0]) ;
        // for(int i = 1 ; i < n ; i++){
        //     if(cakes[i].first == cakes[i-1].first){
        //         continue ;
        //     }
        //     C.push_back(cakes[i]) ;
        // }
        // n = C.size() ;
        // cakes = C ;
        reverse(cakes.begin(), cakes.end()) ;
        memset(dp,-1,sizeof(dp)) ;
        long double fans = 0.0 ;
        for(int i = n - 1 ; i >= 0 ; i--){
            long double temp_ans = 0.0 ;
            temp_ans = 2.0*solve(i - 1,k - 1) + 1.0*cakes[i].first*cakes[i].first + 2.0*cakes[i].first*cakes[i].second ;
            temp_ans = PI*temp_ans ;
            fans = max(fans,temp_ans) ;
        }
        cout << fixed << fans << endl ;
    }
    return 0 ; 
}