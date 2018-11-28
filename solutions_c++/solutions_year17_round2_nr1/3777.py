#include<cstdio>
using namespace std;
int main()
{
    int t,z=1;
    scanf("%d",&t);
    while(z<=t)
    {
        int n;
        long d;
        long max=-1;
        scanf("%ld%d",&d,&n);
        for(int i=0;i<n;i++)
        {
            long d1;
            int p1;
            scanf("%ld%d",&d1,&p1);
            long n2=(d-d1)/p1;
            if(n2>max)
            max=n2;
        }
        float p=d;
        float c=max;
        float ans=p/c;
        printf("Case #%d: %f\n",z,ans);
        z++;
    }
    return 0;
}
