#include <bits/stdc++.h>

using namespace std;
#define ll long long int
#define INF (int)(1e9+7)
#define PI acos(-1)
#define F first
#define S second
#define ld long double
int n,k ;
ld U ;
ld tab[55] ;

int main(){

#ifndef ONLINE_JUDGE
    freopen("/home/montaf/Documents/in.in"   , "r" ,stdin  ) ;
    freopen("/home/montaf/Documents/out.out" , "w" ,stdout ) ;
#endif
    int t ;
    cin >> t ;
    int tc(1) ;
    while(t--){
        cin >> n >> k ;
        cin >> U ;
        for(int i = 0 ; i < n ; i++)cin >> tab[i] ;
        sort(tab,tab+n) ;
        for(int i = 1 ; i < n ; i++){
            ld sum = (tab[i]-tab[i-1])*i ;
            if(sum<=U){
                for(int j = 0 ; j < i ; j++)tab[j] = tab[i] ;
                U -= sum ;
            }
            else{
                for(int j = 0 ; j < i ; j++)tab[j] += (U/(ld)i) ;
                U = 0 ;
                break;
            }
        }
        for(int i = 0 ; i < n ; i++)tab[i] += ( U/(ld)n ) ;
        ld ans = 1.0 ;
        for(int i = 0 ; i < n ; i++)ans *= tab[i] ;
        cout << "Case #"<<tc++<<": "<<fixed << setprecision(6) << ans << endl;
    }


    return 0;
}
