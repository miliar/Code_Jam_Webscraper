#include<bits/stdc++.h>
using namespace std;
#define maxn 1000
double p[maxn];
int main(){
    FILE *fp1 = fopen("C:\\Users\\Hmc1994\\Downloads\\C-small-1-attempt1.in","r+");
    FILE *fp2 = fopen("C:\\Users\\Hmc1994\\Downloads\\ans.out","w+");
    int t;
    fscanf(fp1,"%d",&t);
    int ansn=1;
    while(t--){
        int n,k;
        fscanf(fp1,"%d%d",&n,&k);
        double u;
        fscanf(fp1,"%lf",&u);
        for(int i=1;i<=n;i++){
            fscanf(fp1,"%lf",&p[i]);
        }
        sort(p+1,p+1+n);
        double cur=0.0;
        int ma=n;
        for(int i=1;i<=n;i++){
            cur=0.0;
            for(int j=1;j<=i;j++){
                cur+=p[i]-p[j];
            }
            if(cur>u){
               ma=i-1;
               break;
            }
        }
        if(1){
            for(int i=1;i<=ma;i++){
                u-=p[ma]-p[i];
                p[i]=p[ma];


            }

            for(int i=1;i<=ma;i++){
                p[i]+=u/(double)ma;
            }
        }
        double ans=1.0;
        for(int i=1;i<=n;i++) ans*=p[i];

        cout<<ans<<endl;
        fprintf(fp2,"Case #%d: %.8lf\n",ansn++,ans);
       // fprintf(fp2,"Case #%d: %.8lf\n",ansn++,dp[n-1][k]);
    }
}

