#include<stdio.h>
#include<algorithm>
#include<math.h>
typedef long long LL;
struct data
{
    LL r,h;
    bool operator<(const data &X)const{
        return r>X.r;
    }
};

data a[1005],b[1005];

LL max(LL a, LL b)
{
    if(a<b)return b;
    return a;
}

bool cmp(data a, data b)
{
    return a.r*a.h>b.r*b.h;
}

int main()
{
    freopen("input.txt", "r", stdin);
    freopen("output.txt", "w", stdout);
    LL n,i,j,k,res,lt,l,ans;
    scanf("%lld", &lt);
    for(l=1;l<=lt;l++){
        scanf("%lld %lld", &n, &k);
        ans=0;
        for(i=1;i<=n;i++){
            scanf("%lld %lld", &a[i].r, &a[i].h);
        }
        std::sort(a+1,a+n+1);
        for(i=1;i<=n-k+1;i++){
            res=2*a[i].r*a[i].h+a[i].r*a[i].r;
            for(j=i+1;j<=n;j++)b[j]=a[j];
            std::sort(b+i+1,b+n+1,cmp);
            for(j=1;j<k;j++){
                res+=2*b[i+j].r*b[i+j].h;
            }
            ans=max(res,ans);
        }
        printf("Case #%lld: %lf\n", l, M_PI*ans);
    }
    return 0;
}
