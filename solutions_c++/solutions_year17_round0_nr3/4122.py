#include <bits/stdc++.h>

using namespace std;
#define ll long long int
#define INF (int)(1e9+7)
#define PI acos(-1)
#define F first
#define S second
#define state pair< pair < int , int > , pair < int , int > >
///                         d     D            from    to
ll t,n,k ;

int main(){

#ifndef ONLINE_JUDGE
    freopen("/home/montaf/Documents/in.in"   , "r" ,stdin  ) ;
    freopen("/home/montaf/Documents/out.out" , "w" ,stdout ) ;
#endif
    ios_base::sync_with_stdio(false) ;
    cin.tie(0) ;
    cout.tie(0) ;
    cin >> t ;
    int tc(1) ;
    while(t--){
        cin >> n >> k ;
        priority_queue<state > Q ;
        Q.push({{min((n-1)/2,n/2),max((n-1)/2,n/2)},{0,n+1}}) ;
        int mind = min((n-1)/2,n/2) ;
        int maxd = max((n-1)/2,n/2) ;
        for(int i = 0 ; i < k ; i++){
            state st = Q.top() ;
            Q.pop() ;
            int from = st.S.F ;
            int to   = st.S.S ;
            int d    = st.F.F ;
            int D    = st.F.S ;
            mind = d ;
            maxd = D ;
            Q.push({{min((d-1)/2,d/2),max((d-1)/2,d/2)},{from,from+d+1}}) ;
            Q.push({{min((D-1)/2,D/2),max((D-1)/2,D/2)},{from+d+1,to}}) ;
        }
        cout << "Case #"<<tc++<<": "<<maxd<<" "<<mind << endl;
    }
    return 0;
}
