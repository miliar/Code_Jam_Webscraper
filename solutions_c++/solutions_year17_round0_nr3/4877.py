#include <iostream>
#include <cstdio>
#define MAXN 1000050

using namespace std;

int t, n, k;

struct elem
{
    int st, dr, maxi, mini, pos, v;
    bool operator>(const elem &e) const
    {
        if (mini != e.mini)
            return mini > e.mini;
        if (maxi != e.maxi)
            return maxi > e.maxi;
        return pos > e.pos;
    }
};

inline void cp(elem &dest, const elem &src)
{
    dest.maxi = src.maxi;
    dest.mini = src.mini;
    dest.pos = src.pos;
}

elem combine(const elem &e, const elem &f)
{
    elem rez;
    rez.st = e.st;
    rez.dr = f.dr;
    rez.v = e.v | f.v;

    if (e.v == 0 && f.v == 1)
        rez.st = f.st, rez.dr = f.dr;
    if (e.v == 1 && f.v == 0)
        rez.st = e.st, rez.dr = e.dr;
    int cs, cd;
    if (e.v == 0)
        cs = e.st-1;
    else
        cs = e.dr;
    if (f.v == 0)
        cd = f.dr+1;
    else
        cd = f.st;
    rez.pos = (cd+cs)/2;
    rez.mini = min(rez.pos-cs, cd-rez.pos);
    rez.maxi = max(rez.pos-cs, cd-rez.pos);
    if (e > rez)
        cp(rez, e);
    if (f > rez)
        cp(rez, f);
    return rez;
}

struct aint
{
    elem e[4*MAXN];
    aint()
    {
        //reset(1, n);
    }

    void reset(int st, int dr, int nod = 1)
    {
        if (st == dr)
        {
            e[nod].v = 0;
            e[nod].pos = st;
            e[nod].mini = e[nod].maxi = 1;
            e[nod].st = e[nod].dr = st;
            return;
        }
        int mid = (st+dr) >> 1;
        reset(st, mid, nod<<1);
        reset(mid+1, dr, nod<<1 | 1);
        e[nod] = combine(e[nod<<1], e[nod<<1 | 1]);
    }

    void update(int pos, int st = 1, int dr = n, int nod = 1)
    {
        if (st == dr)
        {
            e[nod].v = 1;
            e[nod].st = e[nod].dr = st;
            e[nod].maxi = e[nod].mini = -1;
            return ;
        }
        int mid = (st + dr) >> 1;
        if (pos <= mid)
            update(pos, st, mid, nod<<1);
        else
            update(pos, mid+1, dr, nod << 1 | 1);
        e[nod] = combine(e[nod<<1], e[nod<<1 | 1]);
    }
};
aint tree;

void solve()
{
    //if (n != 1 || k != 1) {
        tree.reset(1, n);
        elem e;
        for (int i = 1; i <= k; i++) {
            e = tree.e[1];
            tree.update(e.pos);
        }
        printf("%d %d", e.maxi-1, e.mini-1);
    //}
    //else
        //printf("0 0");
}

int main()
{
    freopen("stalls.in", "r", stdin);
    freopen("stalls.out", "w", stdout);

    scanf("%d", &t);
    for (int i = 1; i <= t; i++) {
        scanf("%d %d", &n, &k);
        printf("Case #%d: ", i);
        solve();
        printf("\n");
    }

    return 0;
}
