#include <algorithm>
#include <cstdio>
#include <cstring>
#include <vector>
using namespace std;
struct node {
    double k, s;
    bool operator<(const node& rhs)
    {
        return k > rhs.k;
    }
} h[1005];
int main()
{
    int T;
    double D;
    int N;
    scanf("%d", &T);
    for (int cases = 1; cases <= T; cases++) {
        scanf("%lf%d", &D, &N);
        for (int i = 0; i < N; i++) {
            scanf("%lf%lf", &h[i].k, &h[i].s);
        }
        sort(h, h + N);
        double t = 0;
        for (int i = 0; i < N; i++) {
            t = max(t, (D - h[i].k) / h[i].s);
        }
        printf("Case #%d: %.15f\n", cases, D / t);
    }
    return 0;
}
