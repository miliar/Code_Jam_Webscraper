#include <bits/stdc++.h>
using namespace std;
typedef long long ll;
typedef pair<int,int> P;
int T;
int a[30],t;
int ans[30];
bool dfs(int x){
    if(x==0)return 1;
    if(a[x]<ans[x+1])return 0;
    ans[x]=a[x];
    if(dfs(x-1))return 1;
    if(a[x]-1<ans[x+1])return 0;
    ans[x]=a[x]-1;
    for(int i=x-1;i;--i)ans[i]=9;
    return 1;
}
ll solve(ll x){
    t=0;
    do{
        a[++t]=x%10;
    }while(x/=10);
    ans[t+1]=0;
    dfs(t);
    ll an=0;
    for(int i=t;i;--i)an=an*10+ans[i];
    return an;
}
int main(){
//    freopen("B-small-attempt0.in","r",stdin);
//    freopen("B-large.in","r",stdin);
//    freopen("B.out","w",stdout);
    scanf("%d",&T);
    for(int ca=1;ca<=T;++ca){
        ll n;
        scanf("%lld",&n);
        printf("Case #%d: ",ca);
        printf("%lld\n",solve(n));
    }
    return 0;
}
