#include <iostream>
#include <cstdio>
#include <vector>
#include <algorithm>
#include <cstring>
#include <string>
#include <queue>
#include <cmath>
using namespace std;

double p[55],U;
int main()
{
    freopen("data.out","w",stdout);
    int T;
    scanf("%d",&T);
    for(int kase=1;kase<=T;kase++){
        int n,k;
        scanf("%d%d",&n,&k);
        scanf("%lf",&U);
        for(int i=0;i<n;i++) scanf("%lf",&p[i]);
        sort(p,p+n);
        double sum=0;
        int i;
        bool ok=true;
        for(i=0;i<n;i++){
            if((U+sum+p[i])/(i+1)<p[i]){
                ok=false;break;
            }
            sum+=p[i];
            if(i==n-1) break;
        }
        if(!ok) i--;
        for(int j=0;j<=i;j++){
            p[j]=(sum+U)/(i+1);
        }
           double res=1.0;

        for(int i=0;i<n;i++) res*=p[i];
        printf("Case #%d: %.9f\n",kase,res);
    }
    return 0;
}
