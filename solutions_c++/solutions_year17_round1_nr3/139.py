#include <cstdio>
#include <algorithm>
#include <queue>
#include <tuple>

using namespace std;

int reach[105][105][105][105];


int main()
{
    freopen("in.txt","r",stdin);
    freopen("out.txt","w",stdout);
    int tc;
    scanf("%d",&tc);
    for (int itr=1; itr<=tc; itr++)
    {
        //fprintf(stderr,"Case %d\n",itr);
        int MAXHP;
        int dh,da,kh,ka,b,d;
        scanf("%d%d%d%d%d%d",&dh,&da,&kh,&ka,&b,&d);
        MAXHP=dh;
        for (int i0=0; i0<=dh; i0++)
            for (int i1=0; i1<=kh; i1++)
                for (int i2=0; i2<=kh; i2++)
                    for (int i3=0; i3<=ka; i3++)
                        reach[i0][i1][i2][i3]=-1;
        reach[dh][da][kh][ka]=1;
        queue <tuple <int,int,int,int> > pq;
        pq.push(make_tuple(dh,da,kh,ka));
        int ret=-1;
        while (pq.size() && ret==-1)
        {
            auto pqf=pq.front();
            pq.pop();
            dh=get<0>(pqf);
            da=get<1>(pqf);
            kh=get<2>(pqf);
            ka=get<3>(pqf);
            //fprintf(stderr,"%d %d %d %d\n",dh,da,kh,ka);

            int cdist=reach[dh][da][kh][ka];
            int ndh,nda,nkh,nka;
            //do attack
            ndh=max(0,dh-ka);
            nda=da;
            nkh=max(0,kh-da);
            nka=ka;
            if (nkh==0)
                ret=cdist;
            if (ndh>0)
            {
                if (reach[ndh][nda][nkh][nka]==-1)
                {
                    reach[ndh][nda][nkh][nka]=reach[dh][da][kh][ka]+1;
                    pq.push(make_tuple(ndh,nda,nkh,nka));
                }
            }
            //do heal
            ndh=max(0,MAXHP-ka);
            nda=da;
            nkh=kh;
            nka=ka;
            if (ndh>0)
            {
                if (reach[ndh][nda][nkh][nka]==-1)
                {
                    reach[ndh][nda][nkh][nka]=reach[dh][da][kh][ka]+1;
                    pq.push(make_tuple(ndh,nda,nkh,nka));
                }
            }
            //do buff
            ndh=max(0,dh-ka);
            nda=min(da+b,kh);
            nkh=kh;
            nka=ka;
            if (ndh>0)
            {
                if (reach[ndh][nda][nkh][nka]==-1)
                {
                    reach[ndh][nda][nkh][nka]=reach[dh][da][kh][ka]+1;
                    pq.push(make_tuple(ndh,nda,nkh,nka));
                }
            }
            //do debuff
            nka=max(0,ka-d);
            ndh=max(0,dh-nka);
            nda=da;
            nkh=kh;
            if (ndh>0)
            {
                if (reach[ndh][nda][nkh][nka]==-1)
                {
                    reach[ndh][nda][nkh][nka]=reach[dh][da][kh][ka]+1;
                    pq.push(make_tuple(ndh,nda,nkh,nka));
                }
            }
        }
        printf("Case #%d: ",itr);
        if (ret==-1)
            printf("IMPOSSIBLE\n");
        else
            printf("%d\n",ret);

    }

}
