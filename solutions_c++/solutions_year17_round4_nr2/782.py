#include <cstdio>
#include <algorithm>
#include <queue>

using namespace std;

void solvetp(int tpid)
{
    int n,c,m;
    scanf("%d%d%d",&n,&c,&m);
    vector <int> p1,p2;
    for (int i=1; i<=m; i++)
    {
        int pos,id;
        scanf("%d%d",&pos,&id);
        if (id==1)
            p1.push_back(pos);
        else
            p2.push_back(pos);
    }
    vector <int> E[1005];
    for (int i=0; i<p1.size(); i++)
    {
        for (int j=0; j<p2.size(); j++)
            if (p1[i]!=p2[j])
                E[i].push_back(j);
    }
    vector <int> pr1(1005,-1);
    vector <int> pr2(1005,-1);
    int matchsize=0;
    for (int itr=0; itr<p1.size(); itr++)
    {

        if (pr1[itr]==-1)
        {
            vector <int> bck(p1.size()+5,-1);
            int done=0;
            int endnode=0;
            queue <int> pq;
            pq.push(itr);
            while (pq.size() && done==0)
            {
                int u=pq.front();
                pq.pop();
                for (int i=0; i<E[u].size(); i++)
                {
                    int v=E[u][i];
                    if (pr2[v]==-1)
                    {
                        done=1;
                        endnode=v;
                        pr2[v]=u;
                        break;
                    }
                    else
                    {
                        int nu=pr2[v];
                        if (bck[nu]==-1)
                        {
                            bck[nu]=u;
                            pq.push(nu);
                        }
                    }
                }
            }
            if (done)
            {
                matchsize++;
                while (pr2[endnode]!=itr)
                {
                    int up=pr2[endnode];
                    int newend=pr1[up];
                    pr1[up]=endnode;
                    pr2[newend]=bck[up];
                    endnode=newend;
                }
                pr1[itr]=endnode;
            }
        }
    }
    if (p1.size()==p2.size() && p1.size()==matchsize)
    {
        printf("Case #%d: %d %d\n",tpid,p1.size(),0);
    }
    else
    {
        int unmatch;
        for (int i=0; i<p1.size(); i++)
            if (pr1[i]==-1)
                unmatch=p1[i];
        for (int i=0; i<p2.size(); i++)
            if (pr2[i]==-1)
                unmatch=p2[i];
        if (unmatch==1)
        {
            printf("Case #%d: %d %d\n",tpid,p1.size()+p2.size()-matchsize,0);
        }
        else
        {
            printf("Case #%d: %d %d\n",tpid,max(p1.size(),p2.size()),min(p1.size(),p2.size())-matchsize);
        }
    }
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
