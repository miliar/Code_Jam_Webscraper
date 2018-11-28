#include<stdio.h>

long long table[2][2],tmp;

int main()
{
    freopen("C-large.in","r",stdin);
    freopen("txt.txt","w",stdout);
    int t,ti;
    long long n,k,b,space,cnt;
    scanf ("%d",&t);
    for (ti=0;ti<t;++ti)
    {
        scanf ("%lld %lld",&n,&k);
        tmp = n;
        table[0][0]=1;
        table[0][1] = table[1][0] = table[1][1] = 0;
        cnt=0;
        while(1)
        {
            //printf ("%lld:%lld %lld:%lld\n",tmp,table[0][0],tmp+1,table[0][1]);
            if (tmp%2)
            {
                //tmp+1
                if (table[0][1]+cnt >= k)
                {
                    space = tmp+1;
                    break;
                }
                cnt+=table[0][1];
                table[1][0] += table[0][1];
                table[1][1] += table[0][1];
                //tmp
                if (table[0][0]+cnt >= k)
                {
                    space = tmp;
                    break;
                }
                cnt+=table[0][0];
                table[1][0] += 2*table[0][0];
                //other
                tmp = (tmp-1)/2;
            }
            else
            {
                //tmp+1
                if (table[0][1]+cnt >= k)
                {
                    space = tmp+1;
                    break;
                }
                cnt+=table[0][1];
                table[1][1] += 2*table[0][1];
                //tmp
                if (table[0][0]+cnt >= k)
                {
                    space = tmp;
                    break;
                }
                cnt+=table[0][0];
                table[1][0] += table[0][0];
                table[1][1] += table[0][0];
                //other
                tmp = tmp/2-1;
            }
            table[0][0] = table[1][0];
            table[0][1] = table[1][1];
            table[1][0] = table[1][1] = 0;
        }
        if (space % 2)printf ("Case #%d: %lld %lld\n",ti+1,space/2,space/2);
        else printf ("Case #%d: %lld %lld\n",ti+1,space/2,space/2-1);
    }
    return 0;
}
