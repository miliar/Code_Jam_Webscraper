#include<bits/stdc++.h>
using namespace std;
typedef long long ll;
map<ll,ll>m;
int main(){
    ios_base::sync_with_stdio(0);
    int tc,cc=0;
    ll n,k,x,y;
    cin>>tc;
    while(cc<tc){
        cin>>n>>k;
        m[n]=1;
        while(1){
            x=(m.rbegin())->first;
            y=(m.rbegin())->second;
            if(k-y<=0){
                cout<<"Case #"<<++cc<<": ";
                if(x&1)cout<<((x-1)>>1)<<' '<<((x-1)>>1)<<'\n';
                else cout<<(x>>1)<<' '<<(x>>1)-1<<'\n';
                m.clear();
                break;
            }
            else{
                k-=y;
                if(x&1)m[((x-1)>>1)]+=(y<<1);
                else{
                    m[(x>>1)]+=y;
                    m[(x>>1)-1]+=y;
                }
                m.erase(x);
            }
        }
    }
    return 0;
}
