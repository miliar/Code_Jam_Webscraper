#include<stdio.h>
struct fff
{
    long long num;
    long long cnt;
};
int main()
{
    freopen("C-large.in","r",stdin);
    freopen("c-b.out","w",stdout);
    int t;
    scanf("%d",&t);
    for(int cases=1;cases<=t;cases++)
    {
        long long n,k;
        scanf("%lld%lld",&n,&k);
        //printf("%d %d\n",n,k);
        printf("Case #%d: ",cases);
        fff f1,f2;
        f1.num=n;
        f1.cnt=1;
        f2.cnt=0;
        long long nowcnt=0;
        while(1)
        {
            if(nowcnt+f1.cnt>=k)
            {
                printf("%lld %lld\n",f1.num-1-(f1.num-1)/2,(f1.num-1)/2);
                break;
            }
            else if(nowcnt+f1.cnt+f2.cnt>=k)
            {
                printf("%lld %lld\n",f2.num-1-(f2.num-1)/2,(f2.num-1)/2);
                break;
            }
            else
            {
                nowcnt=nowcnt+f1.cnt+f2.cnt;
                fff newf1,newf2;
                long long a1,a2;
                a1=(f1.num-1)/2;
                a2=f1.num-1-a1;
                if(a1==a2)
                {
                    newf1.num=a2;
                    newf1.cnt=2*f1.cnt;
                    newf2.cnt=0;
                }
                else
                {
                    newf1.num=a2;
                    newf1.cnt=f1.cnt;
                    newf2.num=a1;
                    newf2.cnt=f1.cnt;

                }
                if(f2.cnt)
                {
                    a1=(f2.num-1)/2;
                    a2=f2.num-1-a1;
                    if(a1==a2)
                    {
                        newf2.cnt=newf2.cnt+2*f2.cnt;
                    }
                    else
                    {
                        newf2.num=a1;
                        newf1.cnt=newf1.cnt+f2.cnt;
                        newf2.cnt=newf2.cnt+f2.cnt;
                    }
                }
                f1=newf1;
                f2=newf2;
            }
        }
    }
    return 0;
}
