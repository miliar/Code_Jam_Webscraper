#include<cstdio>
#include<cstring>

int t,a[30];
long long x;

int main()
{
    freopen("B-large.in","r",stdin);
    freopen("data.out","w",stdout);
    scanf("%d",&t);
    for(int k=1;k<=t;++k)
    {
        scanf("%lld",&x);
        int cnt=0;
        while(x)
        {
            a[++cnt]=x%10;x/=10;
        }
        //for(int i=1;i<=cnt;++i) printf("%d",a[i]);puts("");
        for(int i=1;i<cnt;++i) if(a[i]<a[i+1])
        {
            a[i+1]--;
            for(int j=1;j<=i;++j) a[j]=9;
        }
        printf("Case #%d: ",k);
        for(int i=cnt;i;--i) if(a[i]) printf("%d",a[i]);
        puts("");
    }
}
