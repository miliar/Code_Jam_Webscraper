#include <iostream>
#include <cstdio>
#include <cstdlib>
#include <algorithm>

using namespace std;

struct ty
{
    int k, s;
}h[1001];

//bool cmp(struct ty &x, const ty &y)
//{
//    return x.k < y.k;
//}

int main()
{
    freopen("x.in", "r", stdin);
    freopen("x.txt", "w", stdout);
    int T;
    cin>>T;
    for (int cas = 1; cas <= T; cas++)
    {
        int D, N;
        cin>>D>>N;
        for (int i = 0; i < N; i++)
        {
            cin>>h[i].k>>h[i].s;
        }
        //sort(h, h + N, cmp);
        double t = 0.0;
        for (int i = 0; i < N; i++)
            t = max(t, (double)(D - h[i].k) / (double)h[i].s);
        printf("Case #%d: %.8f\n", cas, (double)D / t);
    }
    return 0;
}
