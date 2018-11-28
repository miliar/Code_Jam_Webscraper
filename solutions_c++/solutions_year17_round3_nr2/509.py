#include <cstdio>
#include <iostream>
#include <cstring>
#include <cmath>
#include <vector>
#include<bits/stdc++.h>
using namespace std;
double pi=acos(-1);
int T,a[1600],n,m,x,y,f[1500][1500][4][4];
int main()
{
    scanf("%d",&T);
    //freopen("B.out","w",stdout);
    for(int cas=1;cas<=T;cas++){
        scanf("%d %d",&n,&m);
        memset(a,0,sizeof(a));
        for (int i=1;i<=n;i++) {
            scanf("%d %d",&x,&y);
            for (int j=x;j<y;j++) a[j]=1;
        }
        for (int i=1;i<=m;i++){
            scanf("%d %d",&x,&y);
            for (int j=x;j<y;j++) a[j]=2;
        }
        for(int i=0;i<=1440;i++) for (int j=0;j<=1440;j++) for (int k=0;k<=2;k++) for (int l=0;l<=2;l++) f[i][j][k][l]=2000;
        if (a[0]!=1) f[0][1][1][1]=0;
        if (a[0]!=2) f[0][0][2][2]=0;
        for (int i=1;i<1440;i++){
            for (int j=0;j<=720;j++){
                for (int l=1;l<=2;l++){
                    if (a[i]!=1){
                        if (j>1) f[i][j][1][l]=min(f[i-1][j-1][1][l],f[i-1][j-1][2][l]+1);
                    }
                    if (a[i]!=2){
                        f[i][j][2][l]=min(f[i-1][j][1][l]+1,f[i-1][j][2][l]);
                    }
                    //if (i==1439 && k!=l) f[i][j][k][l]++;
                 //   if (f[i][j][1][l]!=2000) cout<<i<<" "<<j<<" "<<1<<" "<<l<<" "<<f[i][j][1][l]<<endl;
                 //   if (f[i][j][2][l]!=2000) cout<<i<<" "<<j<<" "<<2<<" "<<l<<" "<<f[i][j][2][l]<<endl;
                }
            }
        }
        int N=1440;
        f[N-1][N/2][1][2]++;
        f[N-1][N/2][2][1]++;
        int ans=min(min(f[N-1][N/2][1][1],f[N-1][N/2][1][2]),min(f[N-1][N/2][2][1],f[N-1][N/2][2][2]));
        printf("Case #%d: %d\n",cas,ans);
    }
    return 0;
}
