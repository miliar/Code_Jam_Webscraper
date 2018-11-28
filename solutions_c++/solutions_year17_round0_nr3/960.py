#include <bits/stdc++.h>
using namespace std;
int cas;
int T;
using ll=long long;
/////////////////////////////////////////////////////

const int N=25;
// ll a[N];
vector<ll> a;

// map<ll,ll> sz;
map<ll,ll, greater<ll>> cnt;


int main(){
    for(cin>>T; T--; ){
        printf("Case #%d: ", ++cas);
        /////////////////////////////////////
        ll n, k;
        cin >> n >> k;
        cnt.clear();
         // [n]=1;
        cnt[n]=1;
        for(ll i=k; i; ){
            ll x=cnt.begin()->first, y=cnt.begin()->second;
            if(y >= i){
                cout << x/2 << ' ' << (x-1)/2 << endl;
                break;
            }
            else{
                cnt[(x-1)/2]+=y;
                cnt[x/2]+=y;
                cnt.erase(cnt.begin());
                i-=y;
            }
        }
    }
    return 0;
}