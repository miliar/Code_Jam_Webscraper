#include <cstdio>
#include <cstring>
#include <iostream>
using namespace std;
typedef long long ll;
int T;
struct node{
    ll v,n;
}L,R;
ll n,k;
int main(void){
    freopen("C-large.in","r",stdin);
    freopen("out.txt","w",stdout);
    std::ios::sync_with_stdio(false);
    cin>>T;
    for(int t=1;t<=T;++t){
        cin>>n>>k;
        L.v=L.n=0;R.v=n;R.n=1;
        for(ll p=0;k>(1LL<<p);++p){
            k-=(1LL<<p);
            node PL=L,PR=R;
            R.n=L.n=0;
            if(PR.n){
                if(PR.v&1){
                    R.v=PR.v/2;
                    R.n+=2*PR.n;
                }else{
                    R.v=PR.v/2;
                    R.n+=PR.n;
                    L.v=PR.v/2-1;
                    L.n+=PR.n;
                }
            }
            if(PL.n){
                if(PL.v&1){
                    L.v=PL.v/2;
                    L.n+=2*PL.n;
                }else{
                    R.v=PL.v/2;
                    R.n+=PL.n;
                    L.v=PL.v/2-1;
                    L.n+=PL.n;
                }
            }
        }
        n=R.v;
        if(k>R.n)n=L.v;
        cout<<"Case #"<<t<<": "<<n/2<<" "<<(n-1)/2<<"\n";
    }
}
