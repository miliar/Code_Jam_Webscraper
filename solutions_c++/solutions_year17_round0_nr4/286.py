#include <iostream>
#include <string.h>
#include <stdio.h>
#include <vector>
using namespace std;

int t;
int n,m;
bool Bishops[111][111];
bool Rooks[111][111];
bool BishopsRem[111][111];
bool RooksRem[111][111];

///Rooks
bool BlockedRow[111];
bool BlockedCol[111];

void InitRooks()
{
    memset(BlockedRow,false,sizeof(BlockedRow));
    memset(BlockedCol,false,sizeof(BlockedCol));

    return;
}

void AddRook(int x,int y)
{
    BlockedRow[x]=true;
    BlockedCol[y]=true;
    Rooks[x][y]=true;

    RooksRem[x][y]=true;

    return;
}

void FinishRooks()
{
    int i,j;

    for (i=1;i<=n;i++)
    {
        for (j=1;j<=n;j++)
        {
            if (!BlockedRow[i] && !BlockedCol[j])
            {
                BlockedRow[i]=true;
                BlockedCol[j]=true;
                Rooks[i][j]=true;
            }
        }
    }

    return;
}

///Bishops

int IDSums[511];
int IDDifs[511];
int SOURCE,TARGET;

int Flow[511][511];
int Cap[511][511];

vector<int> Graph[511];

void InitBishops()
{
    int i,j;
    int ctr=0;

    memset(Flow,0,sizeof(Flow));
    memset(Cap,0,sizeof(Cap));

    for (i=2;i<=2*n;i++)
    {
        ctr++;
        IDSums[i]=ctr;
    }

    for (i=-(n-1);i<=(n-1);i++)
    {
        ctr++;
        IDDifs[i+n]=ctr;
    }

    SOURCE=ctr+1;
    TARGET=ctr+2;

    for (i=1;i<=ctr+2;i++)
    {
        Graph[i].clear();
    }

    return;
}

void AddBishop(int x,int y)
{
    Bishops[x][y]=true;

    BishopsRem[x][y]=true;

    return;
}

bool TFO[511];
vector<int> Path;

bool DFS(int ver)
{
    if (TFO[ver])
    return false;

    TFO[ver]=true;
    Path.push_back(ver);

    if (ver==TARGET)
    return true;

    int i;

    for (i=0;i<Graph[ver].size();i++)
    {
        if (Flow[ver][ Graph[ver][i] ]>=Cap[ver][ Graph[ver][i] ])
        continue;

        if ( DFS(Graph[ver][i]) )
        return true;
    }

    Path.pop_back();

    return false;
}

void SendPath()
{
    int i;
    int a,b;

    for (i=1;i<Path.size();i++)
    {
        Flow[ Path[i-1] ][ Path[i] ]++;
        Flow[ Path[i] ][ Path[i-1] ]--;
    }

    return;
}

void FinishBishops()
{
    int i,j;
    int d1,d2;

    for (i=1;i<=n;i++)
    {
        for (j=1;j<=n;j++)
        {
            d1=IDSums[i+j];
            d2=IDDifs[i-j+n];

            Cap[SOURCE][d1]=1;
            Cap[d1][d2]=1;
            Cap[d2][TARGET]=1;

            Graph[SOURCE].push_back(d1);
            Graph[d1].push_back(d2);
            Graph[d2].push_back(TARGET);
            Graph[d2].push_back(d1);

            if (Bishops[i][j])
            {
                Flow[SOURCE][d1]=1;
                Flow[d1][d2]=1;
                Flow[d2][TARGET]=1;
                Flow[d2][d1]=-1;
                Cap[d2][d1]=-1;
            }
        }
    }

    memset(TFO,false,sizeof(TFO));
    Path.clear();
    while(DFS(SOURCE))
    {
        SendPath();
        memset(TFO,false,sizeof(TFO));
        Path.clear();
    }

    for (i=1;i<=n;i++)
    {
        for (j=1;j<=n;j++)
        {
            d1=IDSums[i+j];
            d2=IDDifs[i-j+n];

            if (Flow[d1][d2]==1)
            {
                Bishops[i][j]=true;
            }
        }
    }

    return;
}

struct Change
{
    int x,y;
    int tp;
};

vector<Change> Changes;
Change C;

int main()
{
    freopen("D-large.in","r",stdin);
    freopen("D-large.out","w",stdout);

    int test;
    int x,y;
    char ch[3];
    int i,j;
    int total=0;

    scanf("%d",&t);

    for (test=1;test<=t;test++)
    {
        memset(Bishops,false,sizeof(Bishops));
        memset(Rooks,false,sizeof(Rooks));
        memset(BishopsRem,false,sizeof(BishopsRem));
        memset(RooksRem,false,sizeof(RooksRem));

        scanf("%d %d",&n,&m);

        InitRooks();
        InitBishops();

        for (i=1;i<=m;i++)
        {
            scanf("%s",ch);
            scanf("%d %d",&x,&y);

            if (ch[0]=='o')
            {
                AddRook(x,y);
                AddBishop(x,y);
            }
            else if (ch[0]=='+')
            {
                AddBishop(x,y);
            }
            else
            {
                AddRook(x,y);
            }
        }

        FinishRooks();
        FinishBishops();

        total=0;
        Changes.clear();
        for (i=1;i<=n;i++)
        {
            for (j=1;j<=n;j++)
            {
                if (Bishops[i][j]!=BishopsRem[i][j] || Rooks[i][j]!=RooksRem[i][j])
                {
                    C.x=i;
                    C.y=j;
                    if (Bishops[i][j] && Rooks[i][j])
                    C.tp=2;
                    else if (Bishops[i][j])
                    C.tp=1;
                    else if (Rooks[i][j])
                    C.tp=0;

                    Changes.push_back(C);
                }

                if (Bishops[i][j] || Rooks[i][j])
                {
                    total++;

                    if (Bishops[i][j] && Rooks[i][j])
                    total++;
                }
            }
        }

        printf("Case #%d: %d %d\n",test,total,(int)Changes.size());


        for (i=0;i<Changes.size();i++)
        {
            if (Changes[i].tp==0)
            printf("x ");
            else if (Changes[i].tp==1)
            printf("+ ");
            else
            printf("o ");

            printf("%d %d\n",Changes[i].x,Changes[i].y);
        }
    }

    return 0;
}
