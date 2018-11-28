#include <bits/stdc++.h>
using namespace std;

typedef long long LL;

const int N=55;
double p[N];
int n,k;
double u,v;

void solve(int test){
    scanf("%d%d%lf",&n,&k,&u);
    for (int i=1;i<=n;i++) scanf("%lf",p+i);
    sort(p+1,p+1+n);
    p[n+1]=1;
    for (int i=1;i<=n;i++)
        if (p[i]<p[i+1]){
            v=min(u/i,p[i+1]-p[i]);
            for (int j=1;j<=i;j++) p[j]+=v;
            u-=v*i;
        }
    double ret=1;
    for (int i=1;i<=n;i++) ret*=p[i];
    printf("Case #%d: %.9f\n",test,ret);
}

int main(){
    int tot;
    scanf("%d",&tot);
    for (int i=1;i<=tot;++i) solve(i);
}
