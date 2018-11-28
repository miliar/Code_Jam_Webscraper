#include<bits/stdc++.h>
using namespace std;

int main(){
    ios_base::sync_with_stdio(0);cin.tie(0);
    freopen("input.in","r",stdin);
    freopen("output.txt","w",stdout);
    cout<<fixed<<setprecision(6);
    int t,i,n,d,k,s;
    double z;
    cin>>t;
    for(i=1;i<=t;++i){
        z=0.0;
        cin>>d>>n;
        while(n--){
            cin>>k>>s;
            z=max(z,(double)(d-k)/s);
        }
        cout<<"Case #"<<i<<": "<<d/z<<"\n";
    }
}
