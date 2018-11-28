#include <cstdio>
#include <algorithm>
#include <vector>
#include <queue>
using namespace std;

int main() {
    int t, k, n;
    scanf("%d", &t);
    for (int tt = 1; tt <= t; tt++) {
        printf("Case #%d: ", tt);
        std::priority_queue<int> heap;
        scanf("%d%d", &n, &k);
        heap.push(n);
        for (int i = 0; i < k-1; i++) {
            int top = heap.top();
            heap.pop();
            if (top % 2) {
                heap.push(top/2);
            } else {
                heap.push(top/2-1);
            }
            heap.push(top/2);
        }
        int ans = heap.top();
        if (ans % 2) {
            printf("%d %d\n", ans/2, ans/2);
        } else {
            printf("%d %d\n", ans/2, ans/2-1);
        }
    }
    return 0;
}
