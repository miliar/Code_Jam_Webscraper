#include <bits/stdc++.h>
using namespace std ;
/*
An_Tea_Love.
Never_Give_Up.
*/
#define ft first
#define sd second
#define pb push_back
#define ll long long int
#define mp make_pair
#define loop(i, a, b) for(i=a; i<b; i++)
#define run	ios_base::sync_with_stdio(0)
const int mod = 1e9 + 7;
const ll INF = 1e17;
int main(){
    run;
    ll t,n,i,j,k,l,d,p=0;
    cin>>t;
    while(t--){
        p++;
        cin>>d>>n;
        double sp[n],ma=0;
        ll a[n],b[n];
        loop(i,0,n){
            cin>>a[i]>>b[i];
            sp[i]=(double)(d-a[i])/b[i];
            ma=max(ma,sp[i]);
        }
        printf("Case #%d: ",p);
        double ans=(double)d/ma;
        printf("%.15f\n",ans);
    }
return 0;

}