#include<bits/stdc++.h>

#define INF 9223372036854775807
#define mod 1000000007
#define ll  long long int
#define ld double
#define endl '\n'
#define sz 300005
#define fast() ios_base::sync_with_stdio(0); cin.tie(0); cout.tie(0)

using namespace std;
ll n,d,k[sz],v[sz];

int main(){
    ll t,i,j;
    ld tempv, temps;
    ld ans;
    scanf("%lld",&t);
    for(j = 1; j <= t; j++){
        scanf("%lld%lld",&d,&n);
        for(i = 0; i< n ;i++){
            scanf("%lld%lld",&k[i],&v[i]);
        }

        ans = 0.0;
        for(i = 0; i< n; i++){
            temps = d - k[i];
            tempv = v[i];
            ans = max(ans,temps/tempv);
        }
        ans = d/ans;
        printf("Case #%lld: ",j);
        printf("%lf\n",ans);
    }
    return 0;
}
