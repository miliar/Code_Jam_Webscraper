#include <stdio.h>
#include <algorithm>
#include <vector>
#include <map>
#include <string.h>
#include <math.h>
#define lo long long
#define fi first
#define se second
#define mp make_pair
#define pb push_back

using namespace std;

lo t,n,p,r[110],q[110][110],qnum[110][110];
int main()
{
    freopen("input2.in","r",stdin);
    freopen("output2.out","w",stdout);

    scanf("%lld",&t);
    for (lo i=1;i<=t;i++)
    {
        scanf("%lld %lld",&n,&p);

        for (lo j=0;j<n;j++)
        {
            scanf("%lld",&r[j]);
        }

        for (lo j=0;j<n;j++)
        {
            for (lo k=0;k<p;k++)
            {
                scanf("%lld",&q[j][k]);
                qnum[j][k]=round(((double)q[j][k])/r[j]);
            }
            sort(q[j],q[j]+p);
            sort(qnum[j],qnum[j]+p);
            //for (lo k=0;k<p;k++) printf("%lld(%lld) ",q[j][k],q[j][k]*r[j]); printf("\n");
        }

        lo cou=0;
        lo now[110];
        for (lo j=0;j<110;j++) now[j]=0;

        while(true)
        {
            lo sum=0;
            for (lo j=0;j<n;j++) sum+=qnum[j][now[j]];
            sum=round(((double)sum)/n);

            //cek memenuhi
            bool cek=1;
            for (lo j=0;j<n;j++)
            {
                if (9*sum*r[j]<=10*q[j][now[j]] && 10*q[j][now[j]]<=11*sum*r[j]) continue;
                cek=0;
            }

            if (cek)
            {
                cou++;
                for (lo j=0;j<n;j++)
                {
                    now[j]++;
                    if (now[j]>=p) goto aaa;
                }
                continue;
            }

            //naikkan qnum terendah
            lo simind=-1;
            lo minpem=10000000000,minpeny=1;;
            for (lo j=0;j<n;j++)
            {
                if (minpeny*q[j][now[j]]<r[j]*minpem)
                {
                    simind=j;
                    minpem=q[j][now[j]];
                    minpeny=r[j];
                }
            }

            now[simind]++;
            if (now[simind]>=p) break;
        }

        aaa:;
        printf("Case #%lld: %lld\n",i,cou);
    }
    return 0;
}
