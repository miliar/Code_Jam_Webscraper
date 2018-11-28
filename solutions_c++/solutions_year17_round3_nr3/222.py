#include<bits/stdc++.h>
using namespace std;
inline void read(int &x){
    register char c=getchar();
    x=0;
    while(c<'0'||c>'9') c=getchar();
    for(;c>='0'&&c<='9';c=getchar())
        x=(x<<1)+(x<<3)+(c-'0');
}
inline void reaf(double &z){
    int x,y;
    read(x);read(y);
    z=x+y/10000.0;
}
double p[55],f[55][55];
int main(){
    freopen("input.in","r",stdin);
    freopen("output.out","w",stdout);
    cout<<fixed<<setprecision(9);
    int tt,t,n,i,j,k;
    double l,r,u,v,m;
    read(t);
    for(tt=1;tt<=t;++tt){
        read(n);read(k);k=n+1-k;
        reaf(u);
        for(i=1;i<=n;++i) reaf(p[i]); sort(p+1,p+1+n);
        l=0.0;r=1.0;
        for(i=0;i<50;++i){
            m=(l+r)/2;
            v=0.0;
            for(j=k;j<=n;++j)
                if(p[j]<m)
                    v+=m-p[j];
            if(u<v) r=m; else l=m;
        }
        for(j=k;j<=n;++j) if(p[j]<m) p[j]=m;
        k=n+1-k;
        f[0][0]=1.0;
        for(i=1;i<=n;++i) f[0][i]=0.0;
        for(i=1;i<=n;++i){
            f[i][0]=f[i-1][0]*(1.0-p[i]);
            for(j=1;j<=n;++j)
                f[i][j]=f[i-1][j]*(1.0-p[i])+f[i-1][j-1]*p[i];
        }
        v=0.0;
        for(i=k;i<=n;++i) v+=f[n][i];
        cout<<"Case #"<<tt<<": "<<v<<"\n";
    }
}
