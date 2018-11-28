#include <bits/stdc++.h>

#define st first 
#define nd second 
using namespace std;

typedef long long LL;

LL n,m;
priority_queue<LL> a;
map<LL,LL> cnt;

void solve(int cs){
    scanf("%lld %lld",&n,&m);
    while (!a.empty()) a.pop();
    cnt.clear();
    cnt[n]=1; a.push(n);
    LL x,y;
    while (m){
        LL cur=a.top(); a.pop();
        x=cur/2; y=(cur-1)/2;
        LL v=cnt[cur]; cnt[cur]=0;
        m=max(0LL,m-v);
        if (cnt[x]!=0) cnt[x]+=v; 
            else cnt[x]=v,a.push(x);
        if (cnt[y]!=0) cnt[y]+=v; 
            else cnt[y]=v,a.push(y);
    } 
    printf("Case #%d: %lld %lld\n",cs,x,y);
}

int main(){
    int tot;
    scanf("%d",&tot);
    for (int i=1;i<=tot;++i) solve(i);
}
