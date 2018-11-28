#include<iostream>
#include<cstdio>
#include<queue>
#include<cstring>
#include<algorithm>
#define LL long long
using namespace std;
struct vv
{
    int st,en,du;
    char who;
} p[220];
bool operator <(vv x,vv y)
{
    return x.st<y.st;
}
struct cao
{
    int dd;
    cao(int _) {dd=_;}
};
bool operator <(cao x,cao y)
{
    return x.dd>y.dd;
}
priority_queue<cao> qc,qj;
int main()
{
    freopen("in.in","r",stdin);
    freopen("out.out","w",stdout);
    int t;
    scanf("%d",&t);
    for(int cas=0;cas<t;cas++)
    {
        while(!qc.empty())
            qc.pop();
        while(!qj.empty())
            qj.pop();
        int ac,aj;
        int tc=720,tj=720;
        scanf("%d%d",&ac,&aj);
        for(int i=0; i<ac; i++)
        {
            int s,e;
            scanf("%d%d",&s,&e);
            p[i].st=s;
            p[i].en=e;
            p[i].du=e-s;
            tj-=p[i].du;
            p[i].who='j';
        }
        int tot=ac+aj;
        for(int i=ac; i<tot; i++)
        {
            int s,e;
            scanf("%d%d",&s,&e);
            p[i].st=s;
            p[i].en=e;
            p[i].du=e-s;
            tc-=p[i].du;
            p[i].who='c';
        }
        sort(p,p+tot);
        for(int i=0; i<tot; i++)
        {
            if(p[i].who==p[(i+1)%tot].who)
            {
                if(p[i].who=='c')
                    qc.push(cao(((p[(i+1)%tot].st-p[i].en)%1440+1440)%1440));
                else qj.push(cao(((p[(i+1)%tot].st-p[i].en)%1440+1440)%1440));
            }
        }
        int numc=0,numj=0;
        while(tc>=0&&!qc.empty())
        {
            if(tc>=qc.top().dd)
            {
                tc-=qc.top().dd;
                numc++;
                qc.pop();
            }
            else break;
        }

        while(tj>=0&&!qj.empty())
        {
            if(tj>=qj.top().dd)
            {
                tj-=qj.top().dd;
                numj++;
                qj.pop();
            }
            else break;
        }
        int sumch=0;
        for(int i=0;i<tot;i++)
        {
            if(p[i].who!=p[(i+1)%tot].who)
                sumch++;
            else
            {
                sumch+=2;
            }

        }
        sumch-=(numc+numj)*2;
        printf("Case #%d: %d\n",cas+1,sumch);
    }
}
