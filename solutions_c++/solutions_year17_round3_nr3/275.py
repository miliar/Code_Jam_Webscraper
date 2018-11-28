#include <bits/stdc++.h>
using namespace std;
typedef double LD;
LD p[10000],u;
int T,n,k;
int main(){
    freopen("C.in","r",stdin);
    cin>>T;
    for(int ti(1);ti<=T;ti++){
        cin>>n>>k;
        cin>>u;
        for(int i(1);i<=n;i++)
            cin>>p[i];
        sort(p+1,p+n+1);
        for(int i(1);i<n;i++){
            LD tmp=min((p[i+1]-p[i])*LD(i),u);
            for(int j(1);j<=i;j++)
                p[j]+=tmp/LD(i);
            u-=tmp;
        }
        if(u!=0.0)
            for(int i(1);i<=n;i++)
                p[i]+=u/LD(n);
        LD ans=1.0;
        for(int i(1);i<=n;i++)
            ans*=p[i];
        printf("Case #%d: %lf\n",ti,ans);
    }
    return 0;
}