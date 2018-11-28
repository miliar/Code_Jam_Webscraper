#include<bits/stdc++.h>
#define pb push_back
#define mp make_pair
using namespace std;

typedef long long ll;
typedef pair<ll,ll> ii;
typedef vector<ll> vll;

#define inst freopen("in.txt", "r", stdin)
#define oust freopen("out.txt", "w", stdout)

int main() {
    inst;oust;
    ll t, cs = 1;
    ii arr[1009];
    cin>>t;
    while(t--) {
        ll n,d;
        cin>>d>>n;
        for(int i=0;i<n;i++) cin>>arr[i].first>>arr[i].second;
        sort(arr, arr+n);
        ll a, b;
        a=d-arr[n-1].first;b=arr[n-1].second;
        for(int i=n-2;i>=0;i--) {
            ll p =d - arr[i].first;
            ll q= arr[i].second;
            if(p*b>q*a) {
                a=p;b=q;
            }
        }
        double ans = d*b*1.0/a;
        printf("Case #%lld: %.10lf\n", cs++, ans);
    }
    return 0;
}
