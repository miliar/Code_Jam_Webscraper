#include<cstdio>
#include<cmath>
#include<cstdlib>
#include<algorithm>
using namespace std;
double num[1003][2];
double dp[1003][1003];
int cmp(const void *a,const void *b) {
    double *aa=(double *)a;
    double *bb=(double *)b;
    for(int i=0;i<2;i++) {
        if(aa[i]>bb[i]) return -1;    
        if(aa[i]<bb[i]) return 1;
    }
    return 0;
}
int main () {
    int T;scanf("%d",&T);
    for(int t=0;t<T;t++) {
        int n,k;
        double mr=0,mh=0;
        scanf("%d%d",&n,&k);
        for(int i=0;i<=1000;i++) for(int j=0;j<=1000;j++) dp[i][j]=0;
        for(int i=0;i<n;i++) {
            double h,r;
            scanf("%lf%lf",&r,&h);
            num[i][1]=2*M_PI*r*h;
            num[i][0]=r;
        }
        qsort(num,n,sizeof(num[0]),cmp);
        dp[0][1]=num[0][0]*num[0][0]*M_PI+num[0][1];
        for(int i=1;i<n;i++) {
            for(int j=0;j<=k;j++) {
                if(dp[i-1][j]>0) {
                    double tmp=dp[i-1][j]+num[i][1];
                    dp[i][j+1]=max(dp[i][j+1],tmp);
                    dp[i][j]=max(dp[i][j],dp[i-1][j]);
                }
            }
            dp[i][1]=max(dp[i][1],num[i][1]+num[i][0]*num[i][0]*M_PI);
        }
        double ans=0;
        for(int i=0;i<n;i++)
            if(dp[i][k]>0) ans=max(ans,dp[i][k]);
        printf("Case #%d: %.9lf\n",t+1,ans);
    }
    return 0;
}
