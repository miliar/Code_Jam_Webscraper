#include<stdio.h>
#include<algorithm>

double a[100005];

int main()
{
    freopen("input.txt", "r", stdin);
    freopen("output.txt", "w", stdout);
    int n,k,l,i,lt,j;
    double u,res,v;
    scanf("%d", &lt);
    for(l=1;l<=lt;l++){
        res=1;
        scanf("%d %d", &n, &k);
        scanf("%lf", &u);
        for(i=1;i<=n;i++){
            scanf("%lf", &a[i]);
        }
        std::sort(a+1,a+n+1);
        a[n+1]=1;
        for(i=1;i<=n;i++){
            v=a[i+1]-a[i];
            if(v*i>u){
                for(j=1;j<=i;j++)a[j]+=u/i;
                break;
            }
            else{
                for(j=1;j<=i;j++)a[j]=a[i+1];
                u-=v*i;
            }
        }
        for(i=1;i<=n;i++){
            res*=a[i];
        }
        printf("Case #%d: %lf\n", l, res);
    }
    return 0;
}
