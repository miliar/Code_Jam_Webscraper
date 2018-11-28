#include <stdio.h>
#include <algorithm>
#include <map>
#include <functional>
#include <errno.h>

using namespace std;
typedef unsigned long long ull;

map<int, int> v;
int group[100];

int P2(map<int, int> &v)
{
    int s = v[1];
    return s % 2 == 0 ? s/2 : (s + 1)/2;
}

int P3(map<int, int> &v)
{
    int s1 = v[1];
    int s2 = v[2];

    int k1 = max(s1, s2);
    int k2 = min(s1, s2);

    int t = k1 - k2;
    return k2 + t/3 + (t % 3 == 0 ? 0 : 1);
}

int main()
{
    freopen("./input.txt", "rt", stdin);
    freopen("./output.txt", "wt", stdout);

    int num_test;
    scanf("%d", &num_test);
    for (int test = 0; test < num_test; test++)
    {
        int res = 0;
        v.clear();

        int N, P;
        scanf("%d %d", &N, &P);
        for (int i = 0; i < N; i++)
            scanf("%d", &group[i]);

        for (int i = 0; i < N; i++)
        {
            int r = group[i] % P;
            if (r == 0)
                res++;
            else
                v[r]++;
        }

        switch (P) {
        case 2:
            res += P2(v);
            break;
        case 3:
            res += P3(v);
        default:
            break;
        }

        printf("Case #%d: %d\n", test + 1, res);
    }

    return 0;
}
