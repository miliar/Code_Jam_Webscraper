#include <bits/stdc++.h>
using namespace std;
#define ll long long

int main(){

    int t;
    cin>>t;
    for(int tt=1;tt<=t;tt++){
        printf("Case #%d: ",tt);
        ll d,n;
        cin>>d>>n;
        double tim,max=0;
        for(int i=0;i<n;i++){
            ll k,s;
            cin>>k>>s;
            tim = (double)(d-k)/(double)s;
            if(tim > max)
              max = tim;
        }
        double ans = (double)d/max;
       printf("%.7lf\n",ans);
    }
}