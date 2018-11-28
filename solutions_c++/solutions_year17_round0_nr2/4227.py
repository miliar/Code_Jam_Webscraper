#include <cstdio>
#include <algorithm>

using namespace std;

int v[30],v1[30];

int main()
{
    freopen("file.in","r",stdin);
    freopen("file.out","w",stdout);
    int t;
    long long n;
    scanf("%d",&t);
    for(int test=1;test<=t;test++)
    {
        scanf("%lld",&n);
        int l=0;
        while(n>0)
        {
            v[++l]=n%10;
            n/=10;
        }
        reverse(v+1,v+l+1);
        for(int i=1;i<=l;i++)
            if(v[i]>=v[i-1]) v1[i]=v[i];
            else
            {
                int a=i-1;
                while(1)
                {
                    if(v[a]>v[a-1]) {v1[a]--;break;}
                    a--;
                }
                for(int j=a+1;j<=l;j++) v1[j]=9;
                break;
            }
        int b=1;
        while(v1[b]==0) b++;
        printf("Case #%d: ",test);
        for(int i=b;i<=l;i++) printf("%d",v1[i]);
        printf("\n");
    }
    return 0;
}
