#include <cstdio>
#include <iostream>
#include <map>

using namespace std;

typedef long double ld;

int main()
{
    freopen("C-small-1-attempt1.in", "r", stdin);
    freopen("C-small-1-attempt1.out", "w", stdout);

    int T;
    scanf("%d", &T);

    for(int ct = 1; ct <= T; ct++)
    {
        map<ld, int> m;

        int K, N;
        scanf("%d%d", &N, &K);

        ld U;
        cin >> U;

        for(int i = 0; i < N; i++)
        {
            ld P;
            cin >> P;
            m[P]++;
        }

        while(U > 0)
        {
            if(m.size() == 1)   //tout le monde a la même valeur --> on leur ajoute tous ce qu'il reste
            {
                ld p = m.begin()->first;
                m.clear();

                m[p+U/N] = N;
                U = 0;
                break;
            }
            else
            {
                ld p = m.begin()->first;
                int nb = m.begin()->second;
                m.erase(m.begin());

                ld p2 = m.begin()->first;

                if(U >= (p2-p)*nb)
                {
                    m[p2] += nb;
                    U -= (p2-p)*nb;
                }
                else
                {
                    m[p+U/nb] += nb;
                    U = 0;
                }
            }
        }

        ld ans = 1;
        for(pair<double, int> p : m)
            for(int i = 0; i < p.second; i++)
                ans *= p.first;

        printf("Case #%d: %.06f\n", ct, (double)ans);
    }

    return 0;
}
