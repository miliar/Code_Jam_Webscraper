#include<iostream>
#include<cstdio>
#include<algorithm>

using namespace std;

typedef pair<pair<int, int>, bool> P;


const int MAX_N = 200;
P sch[MAX_N];
int Caida[MAX_N];
int Jaida[MAX_N];

int main(void)
{
    int T;  cin >> T;

    for (int t = 1; t <= T; t ++)
    {
        int AC, AJ, cai, jai;
        int res = 0;
        scanf("%d %d", &AC, &AJ);

        int ACT = 720, AJT = 720;

        for (int i = 0; i < AC; i ++)
        {
            scanf("%d %d", &sch[i].first.first, &sch[i].first.second);
            ACT -= sch[i].first.second - sch[i].first.first;
            sch[i].second = true;
        }

        for (int i = 0; i < AJ; i ++)
        {
            scanf("%d %d", &sch[i+AC].first.first, &sch[i+AC].first.second);
            AJT -= sch[i+AC].first.second - sch[i+AC].first.first;
            sch[i+AC].second = false;
        }

        sort(sch, sch + AC + AJ);
        cai = 0, jai = 0;

        res = AC + AJ;

        for (int i = 0; i < AC + AJ - 1; i ++)
        {
            if (sch[i].second == sch[i+1].second)
            {
                if (sch[i].second == true)
                    Caida[cai++] = sch[i+1].first.first - sch[i].first.second;
                else
                    Jaida[jai++] = sch[i+1].first.first - sch[i].first.second;
            }
        }

            if (sch[0].second == sch[AC+AJ-1].second)
            {
                if (sch[0].second == true)
                    Caida[cai++] = 1440 + sch[0].first.first - sch[AC+AJ-1].first.second;
                else
                    Jaida[jai++] = 1440 + sch[0].first.first - sch[AC+AJ-1].first.second;
            }

        sort(Caida, Caida + cai);
        sort(Jaida, Jaida + jai);

        for (int i = 0; i < cai; i ++)
        {
            if (ACT >= Caida[i])
            {
                res --;
                ACT -= Caida[i];
            }
            else
                res++;
        }

        for (int i = 0; i < jai; i ++)
        {
            if (AJT >= Jaida[i])
            {
                res --;
                AJT -= Jaida[i];
            }
            else
                res++;
        }

        printf("Case #%d: %d\n", t, res);
    }
}
