
#include<bits/stdc++.h>
using namespace std;
#define maxn 1005
int k[maxn],s[maxn];
int main(){
    FILE *fp1 = fopen("C:\\Users\\Hmc1994\\Downloads\\A-large (1).in","r+");
    FILE *fp2 = fopen("C:\\Users\\Hmc1994\\Downloads\\ans.out","w+");
    int t;
    fscanf(fp1,"%d",&t);
    int tot=1;
    while(t--){
        int d,n;
        fscanf(fp1,"%d%d",&d,&n);
        double t=0.0;
        double cur;
        for(int i=1;i<=n;i++){
            fscanf(fp1,"%d%d",&k[i],&s[i]);
            cur=((double)d-k[i])/s[i];
            t=max(t,cur);
        }
        double ans=(double)d/t;
        fprintf(fp2,"Case #%d: %lf\n",tot++,ans);
    }
}
