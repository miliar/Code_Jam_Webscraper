#include <stdio.h>
int N;
bool check()
{
    int temp,d1,d2;
    temp=N;
    if(temp<10)return true;
    if(temp==10)return false;
    d1=temp%10;
    temp/=10;
    while(temp!=0)
    {
        d2=temp%10;
        temp/=10;
        //printf("%d %d\n",d1,d2);
        if(d1<d2)
        {
            return false;
        }
        d1=d2;
    }
    return true;
}
int main()
{
    freopen("B-small-attempt3.in","r",stdin);
    freopen("output.txt","w",stdout);
    int T,ans;
    scanf("%d",&T);
    for(int t=1;t<=T;++t)
    {
      scanf("%d",&N);
      for(;N>=1;--N)
      {
        if(check())
        {
            printf("Case #%d: %d\n",t,N);
            break;
        }
      }
    }
}
