#include<iostream>
#include<algorithm>
#include<iomanip>
using namespace std;

typedef long double ll;

bool comp(ll a[2], ll b[2]) {
    return (a[0]/a[1] > b[0]/b[1]);
}

int main() {

    int t; cin>>t;
    for(int j=1; j<=t; j++) {
        long long D, N; cin>>D>>N;
        ll *h[N];
        
        for(int i=0; i<N; i++) {
            int k, s; cin>>k>>s;
            h[i] = new ll[2];
            h[i][0] = D-k;
            h[i][1] = s;
        }

        sort(h, h+N, comp);
        double sp = D/(h[0][0]/h[0][1]);
        cout<<"Case #"<<j<<": "<<fixed<<setprecision(6)<<sp<<"\n";
    }
    return 0;
}