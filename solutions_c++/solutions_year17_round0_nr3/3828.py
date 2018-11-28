#include <bits/stdc++.h>

using namespace std;

bool compare (pair<int, int> a, pair<int, int> b) {
    int x = min(a.first, a.second) - min(b.first, b.second);

    if (x != 0)return x < 0;

    return max(a.first, a.second) < max(b.first, b.second);
}
priority_queue<pair<int, int> , vector<pair<int, int> >, decltype(&compare)> q(&compare);

int main()
{
    freopen("C-small-2-attempt0.in", "r", stdin);
    freopen("out.txt", "w", stdout);
    int n, t, k, cases = 1;
    scanf("%d", &t);
    while (t--) {
        while(!q.empty())q.pop();
        scanf("%d%d", &n, &k);

        q.push({(n - 1) / 2, n / 2});

        while (--k) {
            pair<int, int> p = q.top();
            q.pop();
            q.push({(p.first - 1) / 2, p.first / 2});
            q.push({(p.second - 1) / 2, p.second / 2});
        }

        printf("Case #%d: %d %d\n", cases ++ , max(q.top().first, q.top().second), min(q.top().first, q.top().second));
    }
    return 0;
}
