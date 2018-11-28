#include <bits/stdc++.h>

using namespace std;

typedef long long ll;
typedef unsigned long long ull;
typedef unsigned int uint;
typedef long double rl;

#define pb push_back
#define popb pop_back
#define mp make_pair
#define mt make_tuple

const int MAXN = 100;

int N, Q;
int D[MAXN + 1][MAXN + 1];
struct city{
    int E, S;
    bool vis;
}c[MAXN + 1];

struct CC{
    rl t;
    int city, horse, endurance;
    bool operator<(const CC& rhs)const
    {
        return t > rhs.t;
    }
};

priority_queue<CC> q;
set<tuple<int, int>> vis;

void GoNeighb(rl t, int city, int horse, int remendurance)
{
    int speed = c[ horse ].S;

    for (int i=0; i<N; i++)
    {
        if (D[city][i] != -1)
        {
            int dist = D[city][i];
            if (dist > remendurance)
                continue;

            rl addt = dist / (rl)speed;
            q.push({t+addt, i, horse, remendurance - dist});
        }
    }
}

rl solve(int F, int T)
{
    q = priority_queue<CC>();
    for (int i=0; i<N; i++)
        c[ i ].vis = false;
    vis.clear();

    q.push({0, F, T, -1});

    while (true)
    {
        CC act = q.top();
        q.pop();

        if (act.city == T)
            return act.t;

        if (vis.count(mt(act.city, act.horse)) > 0)
            continue; // Šis zirgs vairs neinterese
        vis.insert(mt(act.city, act.horse));

        if (c[act.city].vis == false)
        {
            c[act.city].vis = true;
            int horse = act.city;
            GoNeighb(act.t, act.city, horse, c[horse].E);
        }
        GoNeighb(act.t, act.city, act.horse, act.endurance);
    }
    assert(false);
}

int main()
{
    //freopen("input.txt", "r", stdin);
    //freopen(".out", "w+", stdout);
    //ios_base::sync_with_stdio( false );cin.tie(0); cout.tie(0);

    int T;
    scanf("%d", &T);
    for (int test = 1; test<=T; test++)
    {
        printf("Case #%d:", test);
        scanf("%d %d", &N, &Q);
        for (int i=0; i<N; i++)
            scanf("%d %d", &c[ i ].E, &c[ i ].S);

        for (int i=0; i<N; i++)
            for (int j=0; j<N; j++)
                scanf("%d", &D[ i ][ j ]);

        for (int q=0; q<Q; q++)
        {
            int F, T;
            scanf("%d %d", &F, &T);
            --F, --T;
            printf(" %.7Lf", solve(F, T));
        }
        printf("\n");
    }

    return 0;
}


