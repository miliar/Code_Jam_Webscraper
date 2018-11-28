#include<cstdio>
#include<iostream>
#include<cstdlib>
#include<cstring>
#include<algorithm>
#include<queue>
#include<map>
using namespace std;
typedef long long LL;

map<LL, LL> M;

int main()
{
    freopen("C.in", "r", stdin);
    freopen("C.out", "w", stdout);
    int T;
    scanf("%d",&T);
    for (int t = 1; t <= T; t++)
    {
        LL n, k;
        scanf("%I64d%I64d", &n, &k);
        M.clear();
        M.insert(make_pair(n, 1LL));
        LL ans1, ans2;
        while (k > 0)
        {
            map<LL, LL>::reverse_iterator top = M.rbegin();
            ans1 = (top->first) >> 1;
            ans2 = ((top->first) - 1) >> 1;
            if (M.find(ans1) == M.end()) M.insert(make_pair(ans1, top->second));
            else M[ans1] += top->second;
            if (M.find(ans2) == M.end()) M.insert(make_pair(ans2, top->second));
            else M[ans2] += top->second;
            k -= min(top->second, k);
            M.erase(top->first);
        }
        printf("Case #%d: %I64d %I64d\n", t, ans1, ans2);
    }
    return 0;
}
