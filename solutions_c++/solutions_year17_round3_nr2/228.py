#include<bits/stdc++.h>
using namespace std;
inline void read(int &x){
    register char c=getchar();
    x=0;
    while(c<'0'||c>'9') c=getchar();
    for(;c>='0'&&c<='9';c=getchar())
        x=(x<<1)+(x<<3)+(c-'0');
}
inline void mini(int &x,int y){
    if(x>y) x=y;
}
const int INF=1e9+7;
int a[1444],f[725][725][2];
int main(){
    freopen("input.in","r",stdin);
    freopen("output.out","w",stdout);
    int tt,t,n,m,i,j;
    read(t);
    for(tt=1;tt<=t;++tt){
        for(i=0;i<1444;++i) a[i]=-1;
        read(n);read(m);
        while(n--){
            read(i);read(j);
            for(++i;i<=j;++i) a[i]=0;
        }
        n=INF;
        while(m--){
            read(i);read(j);
            for(++i;i<=j;++i) a[i]=1;
        }
        m=INF;
        if(a[1]!=0){
            for(i=0;i<2;++i) for(j=0;j<2;++j) f[i][j][0]=f[i][j][1]=INF;
            f[1][0][0]=0;
            for(i=1;i<=720;++i)
            for(j=0;j<=720;++j){
                if(i==1&&j==0) continue;
                if(a[i+j]!=0&&i>1) f[i][j][0]=min(f[i-1][j][0],f[i-1][j][1]+1); else f[i][j][0]=INF;
                if(a[i+j]!=1&&j>0) f[i][j][1]=min(f[i][j-1][1],f[i][j-1][0]+1); else f[i][j][1]=INF;
            }
            n=min(f[720][720][0],f[720][720][1]+1);
        }
        if(a[1]!=1){
            for(i=0;i<2;++i) for(j=0;j<2;++j) f[i][j][0]=f[i][j][1]=INF;
            f[0][1][1]=0;
            for(i=0;i<=720;++i)
            for(j=1;j<=720;++j){
                if(i==0&&j==1) continue;
                if(a[i+j]!=0&&i>0) f[i][j][0]=min(f[i-1][j][0],f[i-1][j][1]+1); else f[i][j][0]=INF;
                if(a[i+j]!=1&&j>1) f[i][j][1]=min(f[i][j-1][1],f[i][j-1][0]+1); else f[i][j][1]=INF;
            }
            m=min(f[720][720][1],f[720][720][0]+1);
        }
        printf("Case #%d: %d\n",tt,min(n,m));
    }
}
