#include <cmath>
#include <stdio.h>
#include <string>
#include <iostream>
#include <sstream>
#include <algorithm>
using namespace std;

std::string readline()
{
	std::string l;
	std::getline(cin, l);
	//cout << l << endl;
	return l;
}

struct Ingredient
{
    int64_t g, pmin, pmax;
};

int P, N;

int numKits(int64_t q[50][50], int64_t r[50])
{
    int kits = 0;
    for(int j = 0; j < P; j++)
    {
        int64_t pmin = 0;
        int64_t pmax = 100000000;

        for(int i = 0; i < N; i++)
        {
            int64_t ij_pmax = floor((double(q[i][j]/90.0) * 100.0) / double(r[i]));
            int64_t ij_pmin = ceil((double(q[i][j]/110.0) * 100.0) / double(r[i]));

            //printf("[(%lldg)  %lld  %lld]", q[i][j], ij_pmin, ij_pmax);

            pmin = max(pmin, ij_pmin);
            pmax = min(pmax, ij_pmax);
        }

        if(pmin > 0 && pmin <= pmax)
            kits++;
        //printf("\n");
    }
    //printf("kits=%d\n\n\n", kits);

    return kits;
}

void docase(int casenum)
{
    int kits = 0;
    cin >> N >> P;

    int64_t q[50][50];
    int64_t r[50];

    for(int i = 0; i < N; i++)
        cin >> r[i];

    for(int i = 0; i < N; i++)
        for(int j = 0; j < P; j++)
            cin >> q[i][j];

    int PP = 1, NP = 1;
    for(int j = 1; j <= P; j++)
        PP *= j;
    for(int j = 1; j <= N; j++)
        NP *= j;

    //printf("P=%d NP=%d PP=%d\n", P, NP, PP);

    for(int p1 = 0; p1 < NP; p1++)
    {
        for(int i = 0; i < N; i++)
        {
            for(int j = 0; j < P; j++)
            {
                for(int p2 = 0; p2 < PP; p2++)
                {
                    next_permutation(&q[i][0], &q[i][P]);
                    kits = max(kits, numKits(q, r));
                }
            }

            next_permutation(&q[i][0], &q[i][P]);
        }
    }

    printf("Case #%d: %d\n", casenum+1, kits);
}
#if 0
void docase(int casenum)
{
    int P, N;
    cin >> N >> P;
    //printf("N=%d P=%d\n", N, P);

    Ingredient q[50][50];
    int64_t r[50];
    //bool used[50][50];
    //memset(used, 0, sizeof(bool) * 50*50);

    for(int i = 0; i < N; i++)
        cin >> r[i];

    for(int i = 0; i < N; i++)
        for(int j = 0; j < P; j++)
            cin >> q[i][j].g;


    for(int i = 0; i < N; i++)
    {
        for(int j = 0; j < P; j++)
        {
            q[i][j].pmax = floor((double(q[i][j].g/90.0) * 100.0) / double(r[i]));
            q[i][j].pmin = ceil((double(q[i][j].g/110.0) * 100.0) / double(r[i]));
        }
    }

#if 0
    printf("qminmax\n");
    for(int i = 0; i < N; i++)
    {
        for(int j = 0; j < P; j++)
            printf("[(%lldg)  %lld  %lld]", q[i][j], qmin[i][j], qmax[i][j]);
        printf("\n");
    }
#endif

#if 0
    int64_t min_range = 1000000000;
    int min_idx = -1;

    for(int j = 0; j < P; j++)
    {
        if(used[i][j])
            continue;

        int64_t range = qmax[i][j] - qmin[i][j];

        if(range < min_range)
        {
            min_idx = j;
            min_range = range;
        }
    }

    if(min_idx = -1)
        break;
#endif

    for(int i = 0; i < N; i++)
    {
        std::sort(&q[i][0], &q[i][P], 
                [](Ingredient a, Ingredient b) {
                return a.pmin < b.pmin || b.pmin > b.pmax;   
                });
    }

#if 1
    for(int i = 0; i < N; i++)
    {
        for(int j = 0; j < P; j++)
            printf("[(%lldg)  %lld  %lld]", q[i][j].g, q[i][j].pmin, q[i][j].pmax);
        printf("\n");
    }
#endif

    int kits = 0;
    for(int j = 0; j < P; j++)
    {
        int64_t pmin = q[0][j].pmin;
        int64_t pmax = q[0][j].pmax;

        for(int i = 0; i < N; i++)
        {
            pmin = max(pmin, q[i][j].pmin);
            pmax = min(pmax, q[i][j].pmax);
        }

        printf("%lld  %lld\n", pmin, pmax);
        if(pmin <= pmax)
            kits++;
        else
            break;
    }

    printf("Case #%d: %d\n", casenum+1, kits);
}
#endif

int main()
{
    int T;
    cin >> T;

    for(int i = 0; i < T; i++)
    {
        docase(i);
    }
	return 0;
}
