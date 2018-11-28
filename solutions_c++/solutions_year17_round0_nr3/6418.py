#include<cstdio>
#include<map>
#include<queue>
#include<iostream>
#include<algorithm>
using namespace std;
typedef long long ll;

ll n,k;

void solve() {
    priority_queue<ll> q;
    map<ll,ll> cnt;
    q.push(n);
    cnt[n]=1;

    ll sol=0;//solved
    for(;sol<k;) {
        ll now=q.top();q.pop();
        sol+=cnt[now];

        ll a=now/2,b=now-a-1;
        if(!cnt[a]) q.push(a);
        if(!cnt[b]) q.push(b);
        cnt[a]+=cnt[now];
        cnt[b]+=cnt[now];
        if(sol>=k) {
            cout<<max(a,b)<<" "<<min(a,b)<<endl;
            return ;
        }
        cnt[now]=0;
    }
}

int main() {
    freopen("C-large (2).in","r",stdin);
    freopen("C-large (2).out","w",stdout);
    int T;scanf("%d",&T);
    int ca=0;
    while(T--) {
        printf("Case #%d: ",++ca);
        cin>>n>>k;
        solve();
    }
    return 0;
}
