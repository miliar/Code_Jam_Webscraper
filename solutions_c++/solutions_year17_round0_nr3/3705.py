#include <cstdio>
#include <cstring>
#include <algorithm>
#include <queue>

using namespace std;

void solve() {
    int n, k;
    scanf("%d%d", &n, &k);
    priority_queue<int> q;
    q.push(n);
    for(int i = 0; i < k - 1; ++i) {
        int b = q.top(); q.pop();
        int l = b / 2;
        int r = max(0, b - 1 - l);
        q.push(l); q.push(r);
    }
    int b = q.top();
    int l = b / 2;
    int r = max(0, b - 1 - l);
    printf("%d %d\n", max(l, r), min(l, r));
}

int main() {
    int ntests;
    scanf("%d", &ntests);
    for(int tc = 1; tc <= ntests; ++tc) {
        printf("Case #%d: ", tc);
        solve();
    }
    return 0;
}