#include <cstdio>

using namespace std;

int v[25];

int main()
{
    freopen("file.in", "r", stdin);
    freopen("file.out", "w", stdout);
    int test;
    scanf("%d",&test);
    for(int t=1;t<=test;t++)
    {
        long long n;
        int nr=0;
        scanf("%lld",&n);
        for(;n;n/=10) v[++nr]=n%10;
        v[0]=9;
        for(int i=nr;i;i--)
            if(v[i]>v[i-1])
            {
                for(int j=i-1;j>=1;j--) v[j]=9;
                v[i]--;
                for(int j=i+1;j<=nr;j++)
                    if(v[j]>v[j-1])
                    {
                        v[j-1]=9;
                        v[j]--;
                    }
                break;
            }
            if(v[nr]==0) nr--;
            printf("Case #%d: ",t);
            for(int i=nr;i;i--) printf("%d",v[i]);
            printf("\n");
    }
    return 0;
}
