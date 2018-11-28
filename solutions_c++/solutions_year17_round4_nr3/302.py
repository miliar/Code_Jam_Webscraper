#include <cstdio>
#include <cstdlib>
#include <cstring>
#include <cmath>
#include <algorithm>
#include <vector>
#include <string>
#include <stack>
#include <queue>
#include <set>
#include <map>
#include <list>
#include <deque>
#include <tuple>
#include <iterator>

using namespace std;

#define TEST_NUM "pp"
//#define DEBUGGGGGGGGGGGGGGGGGGGGGGGGGG

/*
1
1 2
.|
*/

char arr[60][60];
int pos[110][2];
vector<int> tmp[60][60];
int val[220];
bool use[110];

vector<int> adj[220];

int dx[4] = { 0, 1, 0, -1 };
int dy[4] = { 1, 0, -1, 0 };

void add(int x, int y)
{
    int p = x<0 ? -2*x : 2*x;
    int q = y<0 ? -2*y : 2*y;
    adj[x<0 ? p : p+1].push_back(y<0 ? q+1 : q);
    adj[y<0 ? q : q+1].push_back(x<0 ? p+1 : p);
}

bool f(int x, int y, int d, int k, int r, int c)
{
    if(x < 0 || x >= r || y < 0 || y >= c || arr[x][y] == '#')
        return 1;

    if(arr[x][y] == '-' || arr[x][y] == '|')
        return 0;

    if(arr[x][y] == '.')
    {
        tmp[x][y].push_back(k);
        return f(x+dx[d], y+dy[d], d, k, r, c);
    }

    if(arr[x][y] == '/')
    {
        d = 3 - d;

        return f(x+dx[d], y+dy[d], d, k, r, c);
    }

    if(arr[x][y] == '\\')
    {
        if(d <= 1)
            d = 1 - d;
        else
            d = 5 - d;

        return f(x+dx[d], y+dy[d], d, k, r, c);
    }

    fprintf(stderr, "?????????");
    exit(1);
}

int dis[220];
bool vit[220];
bool fin[220];
int stk[220];
int scc[220];
int num, siz, tim;
int fff(int x)
{
    int r = dis[x] = tim++;
    vit[x] = 1;
    stk[siz++] = x;
    for(int y : adj[x])
    {
        if(!vit[y])
            r = min(r, fff(y));
        else if(dis[y]<dis[x] && !fin[y])
            r = min(r, dis[y]);
    }

    if(r==dis[x])
    {
        while(1)
        {
            scc[stk[--siz]] = num;
            if(stk[siz]==x)
                break;
        }
        num++;
    }

    fin[x] = 1;
    return r;
}

void process()
{
    bool u;
    int r, c, p, x, y, i, j;
    scanf("%d%d", &r, &c);
    for(i = 0; i<r; i++)
        scanf("%s", arr[i]);

    memset(val, 0, sizeof(val));
    memset(use, 0, sizeof(use));
    for(i = 0; i<r; i++)
        for(j = 0; j<c; j++)
            tmp[i][j].clear();

    for(i = 0; i<220; i++)
        adj[i].clear();
    memset(dis, 0, sizeof(dis));
    memset(vit, 0, sizeof(vit));
    memset(fin, 0, sizeof(fin));
    memset(stk, 0, sizeof(stk));
    memset(scc, 0, sizeof(scc));
    num = siz = tim = 0;


    p = 1;
    for(i = 0; i<r; i++)
    {
        for(j = 0; j<c; j++)
        {
            if(arr[i][j] == '-' || arr[i][j] == '|')
            {
                u = 0;
                if(arr[i][j] == '|')
                {
                    u = 1;
                    p = -p;
                }

                if(!f(i, j-1, 2, p, r, c) || !f(i, j+1, 0, p, r, c))
                {
                    if(!f(i-1, j, 3, -p, r, c) || !f(i+1, j, 1, -p, r, c))
                    {
                        printf("IMPOSSIBLE");
                        return;
                    }

                    arr[i][j] = '|';
                    val[p+100] = 2;
                    val[-p+100] = 1;
                }
                else
                {
                    if(!f(i-1, j, 3, -p, r, c) || !f(i+1, j, 1, -p, r, c))
                    {
                        arr[i][j] = '-';
                        val[-p+100] = 2;
                        val[p+100] = 1;
                    }
                    else
                    {
                        int pt = p < 0 ? -p : p;
                        use[pt] = 1;
                        pos[pt][0] = i;
                        pos[pt][1] = j;
                    }
                }

                if(u)
                    p = -p;

                p++;
            }
        }
    }

    for(i = 0; i<r; i++)
    {
        for(j = 0; j<c; j++)
        {
            if(arr[i][j] != '.')
                continue;
            
            u = 0;
            x = y = -10000;

            bool tau[110];
            memset(tau, 0, sizeof(tau));

            for(int &e: tmp[i][j])
            {

                if(val[e+100] == 1)
                {
                    u = 1;
                    break;
                }
                if(val[e+100] == 0)
                {
                    int et = e < 0 ? -e : e;

                    if(tau[et])
                    {
                        u = 1;
                        break;
                    }
                    else
                        tau[et] = 1;

                    if(x == -10000)
                        x = e;
                    else if(y == -10000)
                        y = e;
                    else
                    {
                        fprintf(stderr, "!!!!!!");
                        exit(1);
                    }
                }
            }
            if(u)
                continue;

            if(x == -10000)
            {
                printf("IMPOSSIBLE");
                return;
            }

            if(y == -10000)
                y = x;

            add(x, y);
        }
    }


    for(i = 2; i<=2*p+1; i++)
        if(!vit[i])
            fff(i);

    for(i = 1; i<=p; i++)
    {
        if(use[i] && scc[2*i]==scc[2*i+1])
        {
            printf("IMPOSSIBLE");
            return;
        }
    }

    printf("POSSIBLE\n");
    for(i = 1; i<=p; i++)
    {
        if(use[i])
        {
            if(scc[2*i] >= scc[2*i+1])
            {
                x = pos[i][0];
                y = pos[i][1];

                if(arr[x][y] == '-')
                    arr[x][y] = '|';
                else
                    arr[x][y] = '-';
            }
        }
    }
    
    printf("%s", arr[0]);
    for(i = 1; i<r; i++)
        printf("\n%s", arr[i]);
}

void pre_process()
{

}

int main()
{
#ifndef DEBUGGGGGGGGGGGGGGGGGGGGGGGGGG
#ifdef _DEBUG
    fprintf(stderr, "\nYou are using DEBUG MODE!!!\n\n");
#endif
    char inname[100];
    char outname[100];
    sprintf(inname, "%s.in", TEST_NUM);
    sprintf(outname, "%s.out", TEST_NUM);

    //sprintf(inname, "c.in");
    //sprintf(outname, "ccc.out");

    freopen(inname, "r", stdin);
    freopen(outname, "w", stdout);
#endif
    int tn, ti;
    scanf("%d", &tn);
    pre_process();
    for(ti = 1; ti<=tn; ti++)
    {
        fprintf(stderr, "Case %d/%d\n", ti, tn);
        printf("Case #%d: ", ti);
        process();
        printf("\n");
    }
    return 0;
}