#include<bits/stdc++.h>
#include <math.h>
using namespace std;
#define pb push_back
#define ll long long
#define pii pair<int,int>
#define vi vector<int>
#define vb vector<bool>
#define vii vector<pii>
#define pllll pair<ll,ll>
#define vll vector<ll>
#define vllll vector<pllll>
void solve(){
    int n,k;
    scanf("%d %d",&n,&k);
    vllll v(n);
    for(int i=0;i<n;i++){
        scanf("%lld %lld",&v[i].first,&v[i].second);
    }
    sort(v.begin(),v.end(),greater<pllll>());
    vll mx(n);
    priority_queue<ll,vll,greater<ll> > pq;
    ll mxx=0;
    for(int i=n-1;i>=0;i--){
        mx[i]=mxx;
        // printf("->%d %lld\n",i,mxx);
        ll x=v[i].second*v[i].first;
        mxx+=x;
        pq.push(x);
        if(pq.size()==k){
            mxx-=pq.top();
            pq.pop();
        }
    }
    double ans=0;
    for(int i=0;i<n;i++){
        double ansnow=v[i].first*v[i].first;
        ansnow+=2*v[i].second*v[i].first;
        ansnow+=mx[i]*2;
        // printf("ansnow %lf\n",ansnow);
        ans=max(ans,ansnow);
    }
    printf("%lf\n",ans*3.14159265358979323846);
}
int main(){
    int n;
    scanf("%d",&n);
    for(int i=1;i<=n;i++){
        printf("Case #%d: ",i);
        solve();
    }
}
