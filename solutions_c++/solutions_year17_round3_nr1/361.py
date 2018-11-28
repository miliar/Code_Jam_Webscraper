#include <bits/stdc++.h>

using namespace std;

#define st first
#define nd second
typedef long long LL;

const int N=1E6+10;
LL r[N],h[N];
int n,m;

void solve(int css){
    scanf("%d%d",&n,&m);
    for (int i=1;i<=n;++i) scanf("%lld%lld",r+i,h+i);
    LL ans=0;
    for (int i=1;i<=n;++i){
        vector<LL> c; c.clear();
        LL cur=r[i]*r[i]+2*r[i]*h[i];
        for (int j=1;j<=n;++j)
            if (r[j]<=r[i] && i!=j) c.push_back(2*r[j]*h[j]);
        sort(c.begin(),c.end());
        if (c.size()<m-1) continue;
        for (int j=1;j<m;++j)
            cur+=c[c.size()-j];
        ans=max(ans,cur);
    }
    printf("Case #%d: %.10lf\n",css,ans*M_PI);
}

int main(){
    int tot;
    scanf("%d",&tot);
    for (int i=1;i<=tot;++i) solve(i);
}
