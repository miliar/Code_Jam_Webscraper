#include <cstdio>
#include <iostream>
#include <cstring>
#include <cstdlib>
#include <algorithm>
#include <vector>
#include <list>
#include <set>
using namespace std;

int main()
{
    freopen("A-large.in","r",stdin);
    freopen("A_output_large.txt","w",stdout);
    int T;
    int D,N;
    double K,S;
    scanf("%d",&T);
    for (int index=1;index<=T;index++){
        scanf("%d%d",&D,&N);
        double ans=-1;
        for (int i=0;i<N;i++){
            scanf("%lf%lf",&K,&S);
            double v=(double)D*S/((double)D-K);
            ans=(ans<0)?v:min(ans,v);
        }
        printf("Case #%d: %.6lf\n",index,ans);
    }
    return 0;
}
