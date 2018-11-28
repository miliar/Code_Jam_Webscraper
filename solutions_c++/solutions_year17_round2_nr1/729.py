#include <cstdio>
#include <algorithm>

using namespace std;

int main(){
    int t;
    scanf("%d",&t);

    for(int cas=1;cas<=t;cas++){
        int d,n;
        scanf("%d%d",&d,&n);
        double time=0;
        for(int i=0;i<n;i++){
            int k,s;
            scanf("%d%d",&k,&s);
            time = max(time,(double)(d-k) / (double)s);
        }
        printf("Case #%d: %.6f\n",cas,d/time);


    }
}
