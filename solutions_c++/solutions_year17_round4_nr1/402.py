#include <bits/stdc++.h>
using namespace std;

int N, P;
map<pair<int, vector<int> >, int> res;

int calc(int r, vector<int>& cur)
{
    if (res.count({r, cur}))
        return res[{r, cur}];

    int best = 0;
    for (int p = 1; p < P; ++p)
        if (cur[p-1] > 0) {
            --cur[p-1];
            int z = (r==0) + calc((r+P-p)%P, cur);
            ++cur[p-1];
            best = max(z, best);
        }

    res[{r, cur}] = best;
    return best;
}

int main()
{
    int T; scanf("%d", &T);
    for (int t = 0; t < T; ++t) {
        res.clear();
        scanf("%d%d", &N, &P);

        int answer = 0;

        vector<int> cur(P-1);
        for (int i = 0; i < N; ++i) {
            int G; scanf("%d", &G);
            if (G%P == 0) ++answer; else ++cur[G%P - 1];
        }

        answer += calc(0, cur);
        printf("Case #%d: %d\n", t+1, answer);
    }

    return 0;
}
