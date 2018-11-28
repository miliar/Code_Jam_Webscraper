#include <stdio.h>
#include <vector>
#include <algorithm>
typedef struct node node;
struct node
{
    int s, e;
};
int compare(node a, node b)
{
    return a.s < b.s;
}
std::vector<node> C, J;
int main()
{
    freopen("B-small-attempt0.in", "r", stdin);
    freopen("B-small-attempt0.out", "w", stdout);
    int T, t;
    scanf("%d", &T);
    int Ac, Aj;
    int i, s, e;
    for (t = 1; t <= T; t++)
    {
        scanf("%d %d", &Ac, &Aj);
        C.clear();
        J.clear();
        for (i = 0; i < Ac; i++)
        {
            scanf("%d %d", &s, &e);
            C.push_back({s, e});
        }
        for (i = 0; i < Aj; i++)
        {
            scanf("%d %d", &s, &e);
            J.push_back({s, e});
        }
        std::sort(C.begin(), C.end(), compare);
        std::sort(J.begin(), J.end(), compare);

        if (Ac + Aj == 1)
            printf("Case #%d: 2\n", t);
        else
        {
            if (Ac == 2)
            {
                if (C[1].e - C[0].s > 720 && (C[0].e + 1440 - C[1].s) > 720)
                    printf("Case #%d: 4\n", t);
                else
                    printf("Case #%d: 2\n", t);
            }
            else if (Aj == 2)
            {
                if (J[1].e - J[0].s > 720 && (J[0].e + 1440 - J[1].s) > 720)
                    printf("Case #%d: 4\n", t);
                else
                    printf("Case #%d: 2\n", t);
            }
            else
                printf("Case #%d: 2\n", t);
        }
    }
}
