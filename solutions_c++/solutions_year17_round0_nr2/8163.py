#include <stdio.h>

using namespace std;
typedef long long int ll;
int main()
{

    int i,t,d,k,l,digit[25],m;
    ll n,j;
    scanf("%d",&t);
    for(i=1;i<=t;i++)
    {
        scanf("%lld",&n);
        k=-1;
        for(j=n;j>0;j/=10)
        {
            d=j%10;
            digit[++k]=d;
        }
        for(l=1;l<=k;l++)
        {
            if(digit[l-1]<digit[l])
            {
                digit[l]--;
                for(m=l-1;m>=0;m--)
                {
                    digit[m]=9;
                }
            }
        }
        j=0;
        for(l=k;l>=0;l--)
        {
            j=j*10+digit[l];
        }
        printf("Case #%d: %lld\n",i,j);
    }
    return 0;
}
