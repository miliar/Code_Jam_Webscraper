#include<bits/stdc++.h>
#define ll long long
#define pb push_back
#define all(v) v.begin(),v.end()
#define mp make_pair
#define ff first
#define ss second
#define MAX  1e6+5;
using namespace std;


int main(){
    ios::sync_with_stdio(false);
    cin.tie(0);
    ll t,n;
    double d,a,b,c;
    cin>>t;
    for(ll i=0;i<t;i++){
        cin>>d>>n;
        double e=DBL_MIN;
        double f;
        for(ll j=0;j<n;j++){
            cin>>a>>b;
            c=((d-a)*1.0)/b;
            e=max(e,c);
        }
        f=(d*1.0)/e;
        cout<<"Case #"<<i+1<<": "<<fixed<<setprecision(13)<<f<<endl;
    }


    return 0;
}

