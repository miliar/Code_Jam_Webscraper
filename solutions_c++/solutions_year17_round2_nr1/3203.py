#include <bits/stdc++.h>
using namespace std;
#define ll long long int


int main() {
    int t;
    ll i,n,ans;
    double d;
    scanf("%d",&t);
    for(int j=0;j<t;j++){

        scanf("%lf%lld",&d,&n);
        double pos[n],speed[n];

        double mini=-1.0;
        for(i=0;i<n;i++){
            scanf("%lf%lf",&pos[i],&speed[i]);
            double t1=(d-pos[i])/speed[i];
            mini=max(mini,t1);

        }

        cout<<"Case #"<<j+1<<": "<<fixed<<setprecision(6)<<double(d/mini)<<"\n";

    }

}

