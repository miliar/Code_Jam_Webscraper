#include<bits/stdc++.h>
using namespace std;
typedef long long ll;
int r_bitlength(ll n){
    return log2(n);
}
int main(){
    int t,x;
    ll n,k,m,l,r,s=2;
    cin>>t;
    for(x=1;x<=t;x++){
        cin>>n>>k;
        cout<<"Case #"<<x<<": ";
        //code here
        l=1,r=n,m=(l+r)/s;
        if(k==1LL){
            ll ls=m-l,rs=r-m;
            cout<<max(ls,rs)<<" "<<min(ls,rs)<<endl;
        }else{
            int bl=r_bitlength(k);
            for(int i=0;i<bl;i++){
                ll p=(1LL)<<i;
                if(k&p){
                    //one means going to sit in left
                    r=m-1LL;
                }else{
                    l=m+1LL;
                }
                m=(l+r)/s;
            }
            ll ls=m-l,rs=r-m;
            cout<<max(ls,rs)<<" "<<min(ls,rs)<<endl;
        }
    }
    return 0;
}
