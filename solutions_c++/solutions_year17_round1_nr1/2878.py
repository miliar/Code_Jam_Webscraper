#include <bits/stdc++.h>
#define f first
#define s second

using namespace std;

int R,C,N;
char r[30][30];
int dir[30][30];
int sum[30][30];
char ans[30][30];
vector<pair<int,int> >::iterator it;

bool check(char c,int x,int y,int X,int Y)
{
    int i,j,p,q;
//    if(sum[X][Y]-sum[X][y-1]-sum[x-1][Y]+sum[x-1][y-1]!=(X-x+1)*(Y-y+1)-1)
//        return 0;
    for(i=x;i<=X;++i)
    {
        for(j=y;j<=Y;++j)
        {
            if(ans[i][j]!='-'&&r[i][j]!=c)
                return 0;
        }
    }
    for(i=x;i<=X;++i)
    {
        for(j=y;j<=Y;++j)
        {
            ans[i][j] = c;
        }
    }
    return 1;
}

bool recur(int lv,vector<pair<int,int> > &V)
{
    int i,j;
    if(lv==N)
    {
        for(i=1;i<=R;++i)
            for(j=1;j<=C;++j)
                if(ans[i][j]=='-')
                    return 0;
//        printf("Here\n");
        for(i=1;i<=R;++i)
        {
            printf("%s\n",ans[i]+1);
        }
        return 1;
    }
    int p,q,m,n,RR=V[lv].f,CC=V[lv].s;
    bool found=1;
    for(i=1;i<=RR;++i)
    {
        for(j=1;j<=CC;++j)
        {
            for(p=RR;p<=R;++p)
            {
                for(q=CC;q<=C;++q)
                {
                    if(check(r[RR][CC],i,j,p,q))
                    {
//                        printf(">> %d__%d %d %d %d\n",lv,i,j,p,q);
                        if(recur(lv+1,V))
                            return 1;
                        for(m=i;m<=p;++m)
                        {
                            for(n=j;n<=q;++n)
                            {
                                ans[m][n] = '-';
                            }
                        }
                        ans[RR][CC] = r[RR][CC];
                    }
                    else
                        break;
                }

            }

        }

    }
    return 0;
}

int main()
{
    freopen("As.out","w",stdout);
    int T,t;
    scanf("%d",&T);
    int i,j,p,q;
    for(t=1;t<=T;++t)
    {
        printf("Case #%d:\n",t);
        memset(ans,'-',sizeof ans);
        memset(sum,0,sizeof sum);
        vector<pair<int,int> > V;
        scanf("%d%d",&R,&C);
        for(i=1;i<=R;++i)
        {
            scanf("%s",r[i]+1);
            ans[i][C+1] = '\0';
        }

        for(i=1;i<=R;++i)
        {
            for(j=1;j<=C;++j)
            {
                sum[i][j]=sum[i-1][j]+sum[i][j-1]-sum[i-1][j-1];
                if(r[i][j]=='?')
                {
                    ++sum[i][j];
                }
                else
                {
                    V.push_back({i,j});
                }
            }
        }
        N = V.size();
        recur(0,V);
    }
    return 0;
}
