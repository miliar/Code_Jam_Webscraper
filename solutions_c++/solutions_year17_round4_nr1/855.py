#include <cstdio>
#include <algorithm>
#include <queue>
#include <map>
#include <tuple>
#include <unordered_map>

using namespace std;

struct state
{
    int cnt[4];
    inline bool operator < (const state &op) const
    {
        int sm0=0;
        int sm1=0;
        for (int i=0; i<4; i++)
        {
            sm0+=cnt[i];
            sm1+=op.cnt[i];
        }
        return sm0<sm1;
    }
};

long long compress(state &op)
{
    return op.cnt[0]+op.cnt[1]*105ll+op.cnt[2]*105ll*105ll+op.cnt[3]*105ll*105ll*105ll;
}

state revert(long long &op)
{
    state ret;
    ret.cnt[0]=op%105ll;
    ret.cnt[1]=(op/105ll)%105ll;
    ret.cnt[2]=(op/105ll/105ll)%105ll;
    ret.cnt[3]=(op/105ll/105ll/105ll)%105ll;
    return ret;
}

unordered_map <long long,int> dp;

int st0[4];

void solvetp(int tpid)
{
    int n,p;
    scanf("%d%d",&n,&p);
    dp.clear();
    for (int i=0; i<4; i++)
        st0[i]=0;
    int startsum=0;
    for (int i=1; i<=n; i++)
    {
        int x;
        scanf("%d",&x);
        //printf("ADD %d\n",x);
        startsum+=x;
        st0[x%p]++;
    }
    //printf("SS %d\n",startsum);
    int totals=0;
    for (int i=0; i<p; i++)
        totals+=st0[i]*i;
    int fexact;
    if (totals%p==0)
        fexact=1;
    else
        fexact=0;

    state nw;
    long long compd;
    for (int i=0; i<4; i++)
        nw.cnt[i]=st0[i];
    compd=compress(nw);
    dp[compd]=0;
    queue <long long> pq;
    pq.push(compd);
    int mxsol=0;
    while (pq.size())
    {
        compd=pq.front();
        pq.pop();
        state cur=revert(compd);
        /*
        printf("%lld\n",compd);
        for (int i=0; i<p; i++)
            printf("%d ",cur.cnt[i]);
        printf("\n");
        */
        int csol=dp[compd];
        for (int i=0; i<p; i++)
        {
            if (cur.cnt[i]>0)
            {
                state nxt=cur;
                nxt.cnt[i]--;

                int nsum=0;
                for (int i=0; i<4; i++)
                    nsum+=nxt.cnt[i]*i;
                int nsol=csol;
                if ((startsum-nsum)%p==0)
                    nsol++;
                /*
                printf("NX ");
                for (int j=0; j<p; j++)
                    printf("%d ",nxt.cnt[j]);
                printf("\n");
                printf("%d %d %d %d\n",csol,nsol,startsum,nsum);
                //*/

                long long ncomp=compress(nxt);
                if (dp.find(ncomp)==dp.end())
                {
                    dp[ncomp]=nsol;
                    pq.push(ncomp);
                }
                else
                {
                    if (dp[ncomp]<nsol)
                    {
                        dp[ncomp]=nsol;
                    }
                }
                if (nsol>mxsol)
                {
                    mxsol=nsol;
                }
            }
        }
    }
    printf("Case #%d: %d\n",tpid,1+mxsol-(fexact==1));
}

int main()
{
    freopen("inf.txt","r",stdin);
    freopen("outf.txt","w",stdout);
    int tp;
    scanf("%d",&tp);
    for (int itr=1; itr<=tp; itr++)
        solvetp(itr);

}
