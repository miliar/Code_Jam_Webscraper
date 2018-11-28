#include <cstdio>
using namespace std;
int main()
{
    //freopen("test.txt","r",stdin);
    freopen("A-large.in","r",stdin);
    freopen("A-large.out","w",stdout);
    int testcase;
    scanf("%d",&testcase);
    for (int test=1;test<=testcase;test++)
    {
        int d,n;
        scanf("%d%d",&d,&n);
        double v=1e20;
        for (int i=0;i<n;i++)
        {
            int di,vi;
            scanf("%d%d",&di,&vi);
            double t=d/((((double)d)-di)/vi);
            if (v>t) v=t;
        }
        printf("Case #%d: %.8f\n",test,v);
    }
    return 0;
}
