#include<stdio.h>
#include<string.h>
#include<algorithm>
#include<math.h>
using namespace std;
const double PI=acos(-1.0);

void fre(){
    freopen("B-small-attempt3.in","r",stdin);
    freopen("asdf.out","w",stdout);
}

int a[20000];

int main(){
    fre();
    int _,kcase = 0;
    scanf("%d",&_);
    while(_--){
        int ac,aj;
        memset(a,0,sizeof(a));
        scanf("%d %d",&ac,&aj);
        int l,r,act=0,ajt=0;
        for(int i=1;i<=ac;i++){
            scanf("%d%d",&l,&r);
            for(int j=l+1;j<=r;j++)      a[j%1440]=1,act++;
        }

        for(int i=1;i<=aj;i++){
            scanf("%d%d",&l,&r);
            for(int j=l+1;j<=r;j++)      a[j%1440]=2,ajt++;
        }

        printf("Case #%d: ",++kcase);
        if(ac+aj == 1)      puts("2");
        else {
            if(ac==1)       puts("2");
            else {
                int sum1,sum2 ,flag=0;
                for(int i=0;i<1440;i++){
                    sum1 = sum2 = 0;
                    for(int j=i;j<i+720;j++){
                        if(a[j%1440]==1) sum1++;
                        if(a[j%1440]==2) sum2++;
                    }
                    if(sum1 == act && sum2 == 0  ) flag = 1;
                    if(sum1 == 0   && sum2 == ajt) flag = 1;
                }
                if(flag)   puts("2");
                else       puts("4");
            }
        }
    }
    return 0;
}
