#include <iostream>
#include <cstdio>
#include <algorithm>
#include <cstring>
#include <set>
#include <vector>
#include <queue>
#include <stack>
#include <map>
#include <cmath>
#include <list>
#include <bitset>
using namespace std;

#define pi pair<int,int>
#define mp(x,y) make_pair(x,y)
#define fi first
#define se second
#define pl pair<long long,long long>
#define pb push_back
#define vi vector<int>
#define ll long long
#define ALL(c) c.begin(),c.end()
#define VAR(v,n) __typeof(n) v=(n)
#define FOREACH(i,c) for(VAR(i,(c).begin());i!=(c).end();++i)

const int MAXN=1005;
bool da[725][205][2],tmp[725][210][2];
int czyj[1500];

int main ()
{
    int a,b,c,d,e,f,g,num,n,k,j;
    scanf ("%d", &num);

    for (f=1; f<=num; f++)
    {
        scanf("%d%d", &c, &j);

        for (a=0; a<1500; a++)
            czyj[a]=0;

        while (c--)
        {
            scanf("%d%d", &a, &b);

            for (a++; a<=b; a++)
                czyj[a]=1;
        }

        while (j--)
        {
            scanf("%d%d", &a, &b);

            for (a++; a<=b; a++)
                czyj[a]=2;
        }

        for (a=0; a<=720; a++)
            for (b=0; b<=101; b++)
                da[a][b][0]=da[a][b][1]=0;

        da[0][0][0]=1;
        //cam uzyl czy_cam

        for (a=1; a<=1440; a++)
        {
            for (b=0; b<=720; b++)
                for (c=0; c<=101; c++)
                {
                    if (da[b][c][0])
                    {
                        if (czyj[a]!=2)
                            tmp[b+1][c][0]=1;

                        if (czyj[a]!=1)
                            tmp[b][c+1][1]=1;
                    }

                    if (da[b][c][1])
                    {
                        if (czyj[a]!=2)
                            tmp[b+1][c][0]=1;

                        if (czyj[a]!=1)
                            tmp[b][c][1]=1;
                    }
                }

            for (b=0; b<=720; b++)
                for (c=0; c<=101; c++)
                    for (d=0; d<2; d++)
                    {
                        da[b][c][d]=tmp[b][c][d];
                        tmp[b][c][d]=0;
                    }
        }

        for (a=1; !da[720][a][0]; a++);
        k=a;

        for (a=1; !da[720][a][1]; a++);
        k=min(k,a);

        //_______________________________________

        for (a=0; a<=720; a++)
            for (b=0; b<=101; b++)
                da[a][b][0]=da[a][b][1]=0;

        da[0][0][1]=1;
        //cam uzyl czy_cam

        for (a=1; a<=1440; a++)
        {
            for (b=0; b<=720; b++)
                for (c=0; c<=101; c++)
                {
                    if (da[b][c][0])
                    {
                        if (czyj[a]!=2)
                            tmp[b+1][c][0]=1;

                        if (czyj[a]!=1)
                            tmp[b][c][1]=1;
                    }

                    if (da[b][c][1])
                    {
                        if (czyj[a]!=2)
                            tmp[b+1][c+1][0]=1;

                        if (czyj[a]!=1)
                            tmp[b][c][1]=1;
                    }
                }

            for (b=0; b<=720; b++)
                for (c=0; c<=101; c++)
                    for (d=0; d<2; d++)
                    {
                        da[b][c][d]=tmp[b][c][d];
                        tmp[b][c][d]=0;
                    }
        }

        for (a=1; !da[720][a][1]; a++);
        k=min(k,a);

        for (a=1; !da[720][a][0]; a++);
        k=min(k,a);

        printf("Case #%d: %d\n", f, 2*k);
    }

    return 0;
}
