#include <bits/stdc++.h>

using namespace std;

typedef long long ll;
typedef unsigned long long ull;
typedef unsigned int uint;
typedef double rl;

#define pb push_back
#define popb pop_back
#define mp make_pair
#define mt make_tuple

const int MAXN = 100;
int N, P;
int a[4];

int iteration;
int vis[109][109][109];
int answ[109][109][109];
struct state{
    int len, answ;
    int v[4];
    bool operator<(const state& rhs)const
    {
        if (len == rhs.len)
        {
            return answ < rhs.answ;
        }
        return len > rhs.len;
    }
};

priority_queue<state> q;

int solve()
{
    iteration++;
    int rem = 0;
    int maxlen = 0;
    for (int i=1; i<P; i++)
    {
        rem += a[ i ];
        maxlen += a[ i ] * i;
    }

    q = priority_queue<state>();
    q.push({0, 0, {0, a[1], a[2], a[3]}});

    while (q.empty() == false)
    {
        state a = q.top();
        q.pop();

        if (vis[a.v[1]][a.v[2]][a.v[3]] == iteration
                && answ[a.v[1]][a.v[2]][a.v[3]] >= a.answ)
            continue;

        vis[a.v[1]][a.v[2]][a.v[3]] = iteration;
        answ[a.v[1]][a.v[2]][a.v[3]] = a.answ;

        if (a.len != maxlen && a.len % P == 0)
            a.answ++;

        for (int i=1; i<P; i++)
        {
            if (a.v[i] > 0)
            {
                state targ = a;
                targ.len += i;
                targ.v[i] -= 1;
                q.push(targ);
            }
        }
    }

    return answ[0][0][0];
}

int main()
{
    int T;
    scanf("%d", &T);
    for (int t=1; t<=T; t++)
    {
        for (int i=0; i<4; i++)
            a[ i ] = 0;

        scanf("%d %d", &N, &P);
        for (int i=0; i<N; i++)
        {
            int tmp;
            scanf("%d", &tmp);
            a[ tmp % P ]++;
        }

        int answ = a[ 0 ];
        a[ 0 ] = 0;

        answ += solve();

        printf("Case #%d: %d\n", t, answ);
    }

    return 0;
}


