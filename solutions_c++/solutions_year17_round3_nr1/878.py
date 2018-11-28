#include<bits/stdc++.h>

#define INF 9223372036854775807
#define mod 1000000007
#define ep 0.000000001
#define ll  long long int
#define ld double
#define endl '\n'
#define sz 2005
#define pi 3.141592653589
#define fast() ios_base::sync_with_stdio(0); cin.tie(0); cout.tie(0)

using namespace std;

ld r[sz],h[sz],R;
ll n,k;

typedef pair<ld,pair<ld,ld> > pii;

vector<pii> v;

ld area(ld x, ld y){
    if(x - R > ep){
        return 2.0*pi*x*y + pi*x*x - pi*R*R;
    }
    else{
        return 2.0*pi*x*y;
    }
}

void update(){
    for(ll i = 0; i < (ll)v.size(); i++){
        v[i].first = area(v[i].second.first,v[i].second.second);
    }
}

ld solve(){
    ll i,j;
    ld temp,ans = 0;
    pii node;
    for(i = 0; i < k; i++){
        sort(v.begin(),v.end());
        node = v[(ll)v.size() -1];
        ans += node.first;
        v.pop_back();
        if(node.second.first  - R > ep){
            R = node.second.first;
            update();
        }
    }
    return ans;
}

int main(){
    ll t,i,j;
    scanf("%lld",&t);
    for(j = 1; j <= t; j++){
        cin>>n>>k;
        v.clear();
        R = 0;
        for(i = 0; i< n; i++){
            scanf("%lf%lf",&r[i],&h[i]);
            v.push_back(make_pair(area(r[i],h[i]),make_pair(r[i],h[i])));
        }
        printf("Case #%lld: %.8lf\n",j,solve());
    }
    return 0;
}
