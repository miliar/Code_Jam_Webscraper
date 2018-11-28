#include<bits/stdc++.h>
#define ll long long
#define max(a,b) a<b ? b : a
#define min(a,b) a<b ? a : b
using namespace std;
class sol {
private :
    ll mn,mx;
public :
    sol(){
    mn=mx=-1;
    }
    sol(ll a,ll b){
        mx = a;
        mn = b;
    }
    void output(){
        cout<<mx<<" "<<mn<<endl;
    }
    bool operator<(sol x){
        if(mn<x.mn) return 1;
        if(mn>x.mn) return 0;
        if(mx>x.mx) return 0;
        if(mx<x.mx) return 1;
        return 1;

    }
  /*  bool operator ==(sol(x)){
    return x.mn==mn && x.mx==mx;
    }*/
};
unordered_map<ll,unordered_map<ll,sol>>m;
unordered_map<ll,unordered_map<ll,bool>>c;
sol solve(ll n,ll k){
    if(k==0){
            m[n][k] = sol(n,n);
            c[n][k] = 1;
            return m[n][k];
    }
    if(k==n){
            m[n][k] = sol(0,0);
            c[n][k] = 1;
            return m[n][k];
    }
    if(n==1){
            m[n][k] = sol(0,0);
            c[n][k] = 1;
             return m[n][k];
    }
    if(k==1){
            m[n][k] =  sol(n/2,(n-1)/2);
            c[n][k] = 1;
            return m[n][k];
    }
    if(c[n][k]) return m[n][k];
    sol ans ;
    ll a = n/2,b=k/2;
    if(n%2){
        if(k%2) ans =  solve(a,b);
        else    ans =  min(solve(a,b),solve(a,b-1));
    }
    else{
        if(k%2) ans = min(solve(a-1,b),solve(a,b));
        else    ans = min(solve(a-1,b-1),solve(a,b));
    }
    c[n][k] = 1;
    m[n][k] =  ans;
    return ans;
}
int main(){
    freopen("in.txt","r",stdin);
    freopen("out.txt","w",stdout);
    ios::sync_with_stdio(false);
    int tc;cin>>tc;
    for(int t=1;t<=tc;t++){
        ll k,n;
        cin>>n>>k;
        sol ans = solve(n,k);
        cout<<"Case #"<<t<<": ";
        ans.output();

    }
}
