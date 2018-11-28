#include <bits/stdc++.h>

using namespace std;

double d,k,s;
int n;

int main()
{
    ios_base::sync_with_stdio(false);cin.tie(0);cout.tie(0);
    freopen("in.txt","r",stdin);
    freopen("out.txt","w",stdout);
    int t,cs(0);
    cin>>t;
    while(t--){
        cin>>d>>n;
        double ans(0.0);
        for(int i=0;i<n;++i){
            cin>>k>>s;
            if(k<d){
                ans = max(ans,(d-k)/s);
            }
        }
        ++cs;
        cout<<"Case #"<<cs<<": "<<fixed<<setprecision(6)<<d/ans<<"\n";
    }
    return 0;
}
