#include <cstdio>
#include <queue>
using namespace std;

priority_queue<int> max_heap;

int main(void)
{
    int i, T;
    
    scanf("%d", &T);
    for (i = 0; i < T; ++i) {
        int n, m;
        int maxs, mins;
        int cnt = 0;

        scanf("%d %d", &n, &m);
    
        max_heap = priority_queue<int>();
        max_heap.push(n);
        while (true) {
            int t = max_heap.top();

            maxs = t / 2;
            mins = t / 2 - (t%2 == 0 ? 1 : 0);

            cnt++;
            if (cnt == m) {
                printf("Case #%d: %d %d\n", i + 1, maxs, mins);
                break;
            }

            if (maxs != 0) max_heap.push(maxs);
            if (mins != 0) max_heap.push(mins);

            max_heap.pop();
        }
    }
}
