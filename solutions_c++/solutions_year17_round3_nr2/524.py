#include <cstdio>
#include <iostream>
#include <algorithm>
#include <iterator>
#include <set>

using namespace std;

typedef long double ld;

int c[200], d[200];
int j[200], k[200];

struct Intervalle
{
    int d, f;
    char colour;

    Intervalle() {};
    Intervalle(int _d, int _f, char _c): d(_d), f(_f), colour(_c) {};

    bool operator< (const Intervalle& i) const
    {
        return d < i.d; //car intervalles disjoints
    }
};

int main()
{
    freopen("B-large.in", "r", stdin);
    freopen("B-large.out", "w", stdout);

    int T;
    scanf("%d", &T);

    for(int ct = 1; ct <= T; ct++)
    {
        int ac, aj;
        scanf("%d%d", &ac, &aj);

        set<Intervalle> s;
        int C = 0;
        for(int i = 0; i < ac; i++)
        {
            scanf("%d%d", &c[i], &d[i]);
            s.insert(Intervalle(c[i], d[i], 'C'));
            C += d[i] - c[i];
        }

        int J = 0;
        for(int i = 0; i < aj; i++)
        {
            scanf("%d%d", &j[i], &k[i]);
            s.insert(Intervalle(j[i], k[i], 'J'));
            J += k[i] - j[i];
        }

        while((int)s.size() > 1)    //sinon on a fini
        {
            set<Intervalle>::iterator best_C = s.end(), best_J = s.end();
            int ec_C = 1e9, ec_J = 1e9;

            for(set<Intervalle>::iterator it = s.begin(); it != s.end(); it++)
            {
                bool fin = next(it) == s.end();
                set<Intervalle>::iterator it_nxt = fin?s.begin():next(it);
                Intervalle act = *it, nxt = *it_nxt;

                int lg = (nxt.d - act.f + 1440)%1440;
                if((act.colour == 'C' && nxt.colour == 'C') && (lg < ec_C))
                {
                    ec_C = lg;
                    best_C = it;
                }
                else if((act.colour == 'J' && nxt.colour == 'J') && (lg < ec_J))
                {
                    ec_J = lg;
                    best_J = it;
                }
            }

            if(C + ec_C <= 720) //fail si ec_C = 1e9
            {
                C += ec_C;
                bool fin = next(best_C) == s.end();
                set<Intervalle>::iterator it_nxt = fin?s.begin():next(best_C);
                Intervalle act = *best_C, nxt = *it_nxt;
                s.erase(best_C);
                s.erase(it_nxt);
                s.insert(Intervalle(act.d, nxt.f, 'C'));    //merge
            }
            else if(J + ec_J <= 720)    //fail si ec_J = 1e9
            {
                J += ec_J;
                bool fin = next(best_J) == s.end();
                set<Intervalle>::iterator it_nxt = fin?s.begin():next(best_J);
                Intervalle act = *best_J, nxt = *it_nxt;
                s.erase(best_J);
                s.erase(it_nxt);
                s.insert(Intervalle(act.d, nxt.f, 'J'));    //merge
            }
            else    //plus rien a supprime
                break;
        }

        int nb_J = 0, nb_C = 0;
        for(set<Intervalle>::iterator it = s.begin(); it != s.end(); it++)
            if(it->colour == 'C')
                nb_C++;
            else
                nb_J++;

        int ans = s.empty()?2:(2*max(nb_J, nb_C));
        printf("Case #%d: %d\n", ct, ans);
    }

    return 0;
}
