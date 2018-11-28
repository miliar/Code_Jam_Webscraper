#include <bits/stdc++.h>

using namespace std;
#define ll long long int
#define INF (int)(1e9+7)
#define PI acos(-1)
#define F first
#define S second
ll t,n ;

bool ok(ll x){
    ll last = 9 ;
    ll aux = x ;
    while(aux){
        if(aux%10<=last){
            last = aux%10 ;
            aux /= 10 ;
        }else{
            return false ;
        }
    }
    return true ;
}
int main(){

#ifndef ONLINE_JUDGE
    freopen("/home/montaf/Documents/in.in"   , "r" ,stdin  ) ;
    freopen("/home/montaf/Documents/out.out" , "w" ,stdout ) ;
#endif
    cin >> t ;
    int tc(1) ;
    while(t--){
        cin >> n ;
        ll ans = n ;
        if(!ok(n)){
            vector<ll > v ;
            ll aux = n ;
            while(aux){
                v.push_back(aux%10) ;
                aux /= 10 ;
            }
            reverse(v.begin(),v.end()) ;
            int idx(-1) ;
            for(int i = 1 ; i < v.size() ; i++){
                if(v[i]<v[i-1]){
                    idx = i ;
                    break;
                }
            }
            int to = idx ;
            for(int i = idx-1 ; i >= 0 ; i--){
                if(v[i] != v[idx-1]){break;}
                else to = i ;
            }
//            cout << idx << ' ' << to << endl;
            if(to == 0){
                if(v[0] == 1){
                    ans = 0 ;
                    for(int i = 0 ; i < v.size()-1 ; i++){
                        ans *= 10 ;
                        ans += 9 ;
                    }
                }else{
                    v[0]--;
                    for(int i = 1 ; i < v.size() ; i++)v[i] = 9 ;
                    ans = 0 ;
                    for(int i = 0 ; i < v.size() ; i++){
                        ans *= 10 ;
                        ans += v[i] ;
                    }
                }
            }else{
                    v[to]--;
                    for(int i = to+1 ; i < v.size() ; i++)v[i] = 9 ;
                    ans = 0 ;
                    for(int i = 0 ; i < v.size() ; i++){
                        ans *= 10 ;
                        ans += v[i] ;
                    }
                }

            }
            cout << "Case #"<<tc++<<": "<<ans<<endl;
    }

    return 0;
}
