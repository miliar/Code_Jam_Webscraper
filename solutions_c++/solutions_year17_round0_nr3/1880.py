#include "bits/stdc++.h"
using namespace std;
typedef long long ll;
typedef pair<int,int> pii;
#define rep(i,n) for(ll i=0;i<(ll)(n);i++)
#define all(a)  (a).begin(),(a).end()
#define pb emplace_back
#define INF (1e9+1)
//#define INF (1LL<<59)

#define int ll
signed main(){
    int T;
    cin>>T;
    
    vector<int> C;
    
    for(int i=0;;i++){
        if((1ULL<<i)-1>2000000000000000000ULL)break;
        C.pb((1ULL<<i)-1);
    }
    
   rep(t,T){
       int n,k;
       cin>>n>>k;
       int d;
       
       rep(i,C.size()){
           if(C[i]>=k){
               d = i-1;
               break;
           }
       }
       
       int sd0 = n;
       rep(i,d) sd0 = (sd0-1)/2;
       
       int abs_sd = 1LL<<d;
       int num_of_not_sd0 = n - abs_sd * sd0 - C[d];
       
       
       k -= C[d];
       
       if(k<=num_of_not_sd0){   //+1部分を消費中に終了する場合
           int x = (sd0+1)/2;
           int y = (sd0)/2;
           cout<<"Case #"<<t+1<<": ";
           cout<<x<<" "<<y<<endl;
       }else{
           int x = (sd0)/2;
           int y = (sd0-1)/2;
           cout<<"Case #"<<t+1<<": ";
           cout<<x<<" "<<y<<endl;
       }
    }
}