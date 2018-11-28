#include <bits/stdc++.h>
using namespace std;
struct nod
{
    int mn,mx,idx,st,en;

};
bool operator<(nod a,nod b)
{
    if (a.mn==b.mn)
    {
        if (a.mx==b.mx)
            return a.idx<b.idx;
        return a.mx>b.mx;
    }
    return a.mn>b.mn;
}
set<nod> s;
int main()
{
    freopen("C-small-2-attempt0.in","r",stdin);
    freopen("C-small-2-attempt0.out","w",stdout);
    int t;
    scanf("%d",&t);
    for (int test=1; test<=t; ++test)
    {
        int n,k;
        scanf("%d%d",&n,&k);
        s.clear();
        nod q;
        q.st=1,q.en=n;
        q.idx=(q.st+q.en)/2;
        int tx=q.idx-q.st;
        int ty=q.en-q.idx;
        q.mx=max(tx,ty);
        q.mn=min(tx,ty);
        s.insert(q);
        while(k--)
        {
            q=*s.begin();
            s.erase(s.begin());

            if (q.idx-q.st>=1)
            {
                nod a1;
                a1.st=q.st;
                a1.en=q.idx-1;
                a1.idx=(a1.st+a1.en)/2;
                int tx=a1.idx-a1.st;
                int ty=a1.en-a1.idx;
                a1.mx=max(tx,ty);
                a1.mn=min(tx,ty);
                s.insert(a1);
            }
            if (q.en-q.idx>=1)
            {
                nod a2;
                a2.en=q.en;
                a2.st=q.idx+1;
                a2.idx=(a2.st+a2.en)/2;
                int tx=a2.idx-a2.st;
                int ty=a2.en-a2.idx;
                a2.mx=max(tx,ty);
                a2.mn=min(tx,ty);
                s.insert(a2);
            }
        }
        printf("Case #%d: %d %d\n",test,q.mx,q.mn);
    }
}
