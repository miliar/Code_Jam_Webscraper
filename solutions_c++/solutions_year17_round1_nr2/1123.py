#include <stdio.h>
#include <set>
#include <map>
#define INF 1e9
typedef struct node node;
struct node
{
    int s, e;
};
bool operator<(node a, node b)
{
    return (a.s < b.s);
}
int max(int a, int b)
{
    return (a > b)?a:b;
}
std::multiset<node> Can[50];
std::map<int, int> Next;
int main()
{
    freopen("B-small-attempt0.in", "r", stdin);
    freopen("B-small-attempt0.out", "w", stdout);
    int T, t;
    int N, P;
    int R[50];
    int Q[50][50];
    std::set<node>::iterator p[50];
    int i, j;
    int s, e;
    int sz, ans;
    scanf("%d", &T);
    for (t = 1; t <= T; t++)
    {
        scanf("%d %d", &N, &P);
        for (i = 0; i < N; i++)
            scanf("%d", &R[i]);
        for (i = 0; i < N; i++)
            Can[i].clear();
        for (i = 0; i < N; i++)
        {
            for (j = 0; j < P; j++)
            {
                scanf("%d", &Q[i][j]);
                s = (Q[i][j]*10)/(R[i]*11);
                while (s*R[i]*11 < Q[i][j]*10) s++;
                e = (Q[i][j]*10)/(R[i]*9);
                if (s <= e)
                    Can[i].insert({s, e});
            }
        }
        for (i = 0; i < N; i++)
        {
            if (Can[i].size() == 0)
            {
                printf("Case #%d: 0\n", t);
                break;
            }
        }
        if (i < N)
            continue;

        sz = 0;
        ans = 0;
        for (i = 0; i < N; i++)
        {
            p[i] = Can[i].begin();
            Next.insert(std::make_pair(p[i]->e, i));
            sz = max(sz, p[i]->s);
        }
        while (!Next.empty())
        {
            while (!Next.empty() && sz > (Next.begin())->first)
            {
                i = (Next.begin())->second;
                Next.erase(Next.begin());
                p[i]++;
                if (p[i] != Can[i].end())
                {
                    Next.insert(std::make_pair(p[i]->e, i));
                    sz = max(sz, p[i]->s);
                }
                else
                    sz = INF;
            }
            if (sz <= (Next.begin())->first)
            {
                ans++;
                Next.clear();
                for (i = 0; i < N; i++)
                {
                    p[i]++;
                    if (p[i] != Can[i].end())
                    {
                        Next.insert(std::make_pair(p[i]->e, i));
                        sz = max(sz, p[i]->s);
                    }
                    else
                        sz = INF;
                }
            }
        }
        printf("Case #%d: %d\n", t, ans);
    }
}
