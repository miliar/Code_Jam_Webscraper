#include <cstdio>
#include <map>

using namespace std;

int D, N;
map<int, int> d;

int main()
{
    freopen("A-large.in", "r", stdin);
    freopen("A-large.out", "w", stdout);

    int nbT;
    scanf("%d", &nbT);
    for(int ct = 1; ct <= nbT; ct++)
    {
        scanf("%d%d", &D, &N);

        for(int i = 0; i < N; i++)
        {
            int k, s;
            scanf("%d%d", &k, &s);
            d[k] = s;
        }

        double current_time = 0;
        for(map<int, int>::reverse_iterator it = d.rbegin(); it != d.rend(); it++)
        {
            int k = it->first, s = it->second;
            double time = (double)(D-k)/s;
            current_time = max(current_time, time);
        }

        d.clear();
        printf("Case #%d: %.07f\n", ct, D/current_time);
    }

    return 0;
}
