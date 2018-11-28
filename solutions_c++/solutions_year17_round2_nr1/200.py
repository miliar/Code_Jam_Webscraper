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

const int MAXN = 1000;
int n;

struct Horse{
    int k, s;
    bool operator<(const Horse& r)const
    {
        return k > r.k;
    }
}h[MAXN];

int main()
{
    int T;
    scanf("%d", &T);
    for (int test = 1; test<=T; test++)
    {
        int D, N;
        scanf("%d %d", &D, &N);
        for (int i=0; i<N; i++)
            scanf("%d %d", &h[ i ].k, &h[ i ].s);

        sort(h, h+n);

        rl maxtime = 0;

        for (int i=0; i<N; i++)
        {
            int d = D - h[ i ].k;
            rl t = d / (rl)h[ i ].s;
            maxtime = max(maxtime, t);
        }
        rl answ = D / maxtime;
        printf("Case #%d: %.7Lf\n", test, answ);
    }

    return 0;
}


