#include <stdio.h>
#include "stdlib.h"

int main() {
    freopen("B-small-attempt0.in.txt", "r", stdin);
    freopen("B-small-attempt0.out.txt", "w", stdout);

    long t;
    scanf("%ld",&t);
    for (long tt=1;tt<=t;tt++){
        long ac,aj;
        scanf("%ld%ld",&ac,&aj);
        if (ac<=1&&aj<=1){
            for (int i=0;i<ac+aj;i++){
                long t1,t2;
                scanf("%ld%ld",&t1,&t2);
            }
            printf("Case #%ld: %d\n",tt,2);
        }
        else {
            long s1,e1,s2,e2;
            scanf("%ld%ld",&s1,&e1);
            scanf("%ld%ld",&s2,&e2);
            long int1=s2-e1,int2=s1-e2;
            if (int1<0)
                int1+=1440;
            if (int2<0)
                int2+=1440;
            int ans;
            if (int1>=720||int2>=720)
                ans=2;
            else
                ans=4;
            printf("Case #%ld: %d\n",tt,ans);
            
        }
    }
    return 0;
}
