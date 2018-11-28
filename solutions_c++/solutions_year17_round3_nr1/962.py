#include<bits/stdc++.h>
using namespace std;
typedef long long ll;
typedef long double ld;
bool cmp(pair<ll,ll> a, pair<ll,ll> b){
    if(a.first > b.first) return true;
    if(a.first == b.first){
        if(a.second > b.second) return true;
    }
    return false;
}
#define PI acos(-1)
int main(){
    ios_base::sync_with_stdio(false);
    freopen("A-large.in.txt","r",stdin);
    freopen("largeout.txt","w",stdout);
    ll T;
    cin >> T;
    for(ll t = 1; t <= T; t++){
        ll N,K;
        cin >> N >> K;
        vector<pair<ll,ll> > v;
        for(ll i = 0; i < N; i++){
            ll a,b;
            cin >> a >> b;
            v.push_back(make_pair(a,b)); /// radius, height
        }
        sort(v.begin(),v.end(),cmp);
        ld maxi = 0;
        for(ll i = 0; i < N; i++){
            ld temp = v[i].first * v[i].first + 2 * v[i].first * v[i].second;
            vector<ll> v1;
            for(ll j = i+1; j < N; j++){
                v1.push_back(2*v[j].first * v[j].second);
            }
            sort(v1.begin(),v1.end(),greater<ll>());
            for(ll j = 0; j < min((ll)v1.size(),K-1); j++){
                temp += v1[j];
            }
            maxi = max(maxi,(ld)temp*PI);
        }
        cout << std::fixed;
        cout << std::setprecision(9);
        cout << "Case #" << t << ": " << maxi << "\n";
    }
    return 0;
}
