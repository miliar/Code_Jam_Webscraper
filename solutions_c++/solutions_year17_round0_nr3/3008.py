#include <bits/stdc++.h>
using namespace std;
typedef long long int lld;

int main(){
    int t,ncase=1;
    lld n,k,smin,smax, aux, p,soul;
    cin>>t;
    p = 1;
    while (t>0){
        cin>>n>>k;
        t--;
        smax = 1,smin = 0, p =soul = 1;
        while (k-p>0){
            if (n%2==0)smin = smax + 2*smin;
            else smax = smax*2 + smin;
            n/=2;
            soul*=2;
            p = soul+p;
        }
        soul = k-p+soul;
        if (soul<=smax)soul = n;
        else soul = n-1;
        if (soul%2==0)smin=soul/2-1,smax=soul/2;
        else smin = smax = soul/2;

        cout<<"Case #"<<ncase++ << ": "<<smax<<" "<<smin<<endl;
    }
}
