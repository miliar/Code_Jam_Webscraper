#include <cstdio>
#include <cstdlib>
#include <cstring>
#include <cmath>
#include <algorithm>
#include <vector>
using namespace std;
double p[55];
int main()
{
    int T;
    scanf("%d",&T);
    for(int cases=1;cases<=T;cases++){
        int n,k;
        double u;
        scanf("%d%d",&n,&k);
        scanf("%lf",&u);
        double sum=u;
        for(int i=0;i<n;i++){
            scanf("%lf",&p[i]);
            sum+=p[i];
        }
        sort(p,p+n);
        double pr=1;
        int i=n;
        while(true){
            if(p[i-1]>sum/i) {
                sum-=p[i-1];
                pr*=p[i-1];
                i--;
            }else{
                break;
            }
        }
        double sum2=u;
        for(int j=0;j<i;j++){
            sum2+=p[j];
        }
        sum2/=i;
        printf("Case #%d: %.15f\n",cases,pow(sum2,i)*pr);
    }
    return 0;
}

