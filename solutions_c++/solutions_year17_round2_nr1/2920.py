#include<cstdio>
#include<cstdlib>
#include<string>
#include<string.h>
#include<math.h>
#include<algorithm>
using namespace std;
int main(){
    freopen("inputA","r",stdin);
    freopen("outputA.out","w",stdout);
    int T;
    scanf("%d",&T);
    for(int t=1;t<=T;t++){
        float d;
        int n;
        scanf("%f%d",&d,&n);
        int k[n],s[n];
        double fk[n],fs[n];
        for(int i=0;i<n;i++){
            scanf("%d%d",&k[i],&s[i]);
            fk[i]=(double)k[i];fs[i]=(double)s[i];
        }
        double ans=INFINITY;
        for(int i=0;i<n;i++){
            ans=min(ans,d/((d-fk[i])/fs[i]));
        }
        printf("Case #%d: %f\n",t,ans);
    }
}
