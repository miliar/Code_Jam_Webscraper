#include<bits/stdc++.h>

#define mp make_pair
#define pb push_back
#define ts to_string
#define ll long long
#define vll vector<ll>
#define pll pair<ll,ll>

using namespace std;

vll sort(vll v, ll flag) {
    ll n=v.size();
    for(ll i=n-1;i>0;i--) {
        if(v[i]>=v[i-1]) {
            continue;
        } else {
            v[i]=9;
            if(flag==0) {
                v[i-1]=v[i-1]-1;
            }
            vll v1 (v.begin()+(i),v.end());
            vll v3=sort(v1,1LL);
            for(ll j=i;j<n;j++) {
                v[j]=v3[j-i];
            }
        }
    }
    return v;
}

int main() {
    ll t;
    cin>>t;
    for(ll t1=0;t1<t;t1++) {
        string a;
        cin>>a;
        ll siz = (ll)a.size();
        vll v(siz);
        for(ll i=0;i<siz;i++) {
            v[i]=(ll)(a.at(i)-'0');
        }
        v=sort(v,0LL);
        printf("Case #%lld: ",t1+1);
        for(ll i=0;i<siz;i++) {
            while(v[i]==0) {
                i++;
            }
            printf("%lld",v[i]);
        }
        printf("\n");
    }
    return 0;
}
