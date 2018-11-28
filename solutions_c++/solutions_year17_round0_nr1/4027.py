#include <bits/stdc++.h>

using namespace std;
#define ll long long int
#define INF (int)(1e9+7)
#define PI acos(-1)
#define F first
#define S second
int t,n,k;
string s ;

int main(){

#ifndef ONLINE_JUDGE
    freopen("/home/montaf/Documents/in.in"   , "r" ,stdin  ) ;
    freopen("/home/montaf/Documents/out.out" , "w" ,stdout ) ;
#endif
    cin >> t ;
    int tc(1) ;
    while(t--){
        cin >> s >> k ;
        n = s.size() ;
        /*
        int msk = (1<<(n-k+1))-1 ;
        int ans = INF ;

        for(int i = 0 ; i <= msk ; i++){
            vector<bool > tmp(n) ;
            for(int j = 0 ; j < n ; j++)tmp[j] = ( s[j] == '-' ? false : true ) ;
            for(int j = 0 ; j < n ; j++){
                if((i&(1<<j))!=0){
                    for(int p = j ; p < j+k ; p++)tmp[p] = !tmp[p] ;
                }
            }
            bool ok(true) ;
            for(int j = 0 ; j < n ; j++){
                if(tmp[j] == false){
                    ok = false ;
                    break;
                }
            }
            if(ok){
                ans = min(ans,(int)(__builtin_popcount(i) )) ;
            }
        }
        */

        vector<bool > v(n) ;
        for(int i = 0 ; i < n ; i++){
            v[i] = (s[i] == '-' ? false : true ) ;
        }
        int cnt(0) ;
        for(int i = 0 ; i < n-k+1 ; i++){
            if(v[i] == false){
                cnt++;
                for(int j = i ; j < i+k ; j++){
                    v[j] = !v[j] ;
                }
            }
        }
        bool ok(true) ;
        for(int i = n-k+1 ; i < n ; i++){
            if(v[i] == false){
                ok = false ;
                break;
            }
        }
        if(ok){
            cout << "Case #"<<tc++<<": "<<cnt << endl;
        }else{
            cout << "Case #"<<tc++<<": IMPOSSIBLE" << endl;
        }

    }


    return 0;
}
