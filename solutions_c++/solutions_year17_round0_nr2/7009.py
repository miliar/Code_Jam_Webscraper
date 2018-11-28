#include<bits/stdc++.h>
#define ll long long int
#define ite iterator
#define mp make_pair
#define ff first
#define ss second
#define pb push_back
#define ioS ios::sync_with_stdio(false);
#define re0 return 0;
using namespace std ;

ll n,i,j,k,y,x,q,z,t,mod,m,flag,ans,lo,md,hi,l,r ;
ll inf = 10000000000000 ;

vector<ll>v  ;
ll a[3000]  ;
map<ll,ll> m1  ;
map<ll,ll>::iterator itr,itr1 ;
int main(){
    ioS ;
       freopen("input.txt","r",stdin) ;
          freopen("output.txt","w",stdout) ;
    cin >> t ;
    for(int ss=1;ss<=t;ss++){
 cin >> n ;
 v.clear() ;
 k=n;
 while(k){
    v.pb(k%10);k/=10;
 }
 k=v.size() ;
 x=1;
 for(i=1;i<k;i++){
    x = x*10+1;
 }

 cout << "Case #" << ss << ": " ;
reverse(v.begin(),v.end());
 if(n<x){
    for(i=1;i<k;i++){
        cout << "9";
    }cout << endl ;
 }
 else{x=0;
     flag=1;k=v.size() ;
    for(i=1;i<k;i++){
        if(v[i]<v[i-1]){flag=0;x=i-1;break;}
    }
    if(x>=1){while(x>=1&&v[x]==v[x-1]){
        x--;
        if(x<1){break;}
    }}

    if(flag==0){for(i=0;i<x;i++){cout << v[i];}
    cout << v[i]-1 ;
    for(j=i+1;j<k;j++){cout << "9";}
    cout<< endl ;}
    else{cout <<n << endl;}
 }

}
}
