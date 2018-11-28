#include<bits/stdc++.h>
using namespace std;
int main(){
    freopen("in.txt","r",stdin);
    freopen("out.txt","w",stdout);
    ios::sync_with_stdio(false);
    int tc;cin>>tc;
    for(int t=1;t<=tc;t++){
        double d;
        int n;
        cin>>d>>n;
        vector<double> D(n);
        for(int i=0;i<n;i++){
            double k,s;
            cin>>k>>s;
            D[i]=(d-k)/s; //  km/(km/h) = h
            D[i]=d/D[i]; //  km/h
        }
        double ans = *min_element(D.begin(),D.end());
        cout.precision(9);
        cout<<"Case #"<<t<<": ";
        cout<<fixed<<ans<<endl;
    }
}
