#include<bits/stdc++.h>
using namespace std;

long long n,k;
int t;
map<pair<long long,long long>,long long> H;
set<pair<long long,long long> >S;
void solve(){
    scanf("%lld%lld",&n,&k,&t);
    priority_queue<pair<long long,long long> >Q;
    H.clear();
    S.clear();
    Q.push(make_pair((n-1)/2,n/2));
    H[make_pair((n-1)/2,n/2)]=1;
    S.insert(make_pair((n-1)/2,n/2));
    long long Now = 0;
    long long lax = 0,lay = 0,lans = 0;
    while(Now<k){
        pair<long long,long long> now = Q.top();
        Q.pop();
        lax = now.first,lay = now.second,lans = H[now];
        Now+=lans,H[now]=0;
        if(now.first!=0){
            pair<long long,long long> next = make_pair((now.first-1)/2,now.first/2);
            if(S.find(next)==S.end()){
                Q.push(next);
                S.insert(next);
            }
            H[next]+=lans;
        }
        if(now.second!=0){
            pair<long long,long long> next = make_pair((now.second-1)/2,now.second/2);
            if(S.find(next)==S.end()){
                Q.push(next);
                S.insert(next);
            }
            H[next]+=lans;
        }
    }
    printf("Case #%d: %lld %lld\n",++t,lay,lax);
}
int main(){
    freopen("C-large.in","r",stdin);
    freopen("C-large.out","w",stdout);
    int t;
    scanf("%d",&t);
    while(t--)solve();
    return 0;
}
