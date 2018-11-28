#include <cstdio>
#include <queue>
#include <vector>
#include <iostream>

int main() {
    int N;
    scanf("%d",&N);
    for (int i = 0; i < N; ++i) {
        std::priority_queue<int> pq;
        int n,k;
        scanf("%d %d",&n,&k);
        pq.push(n);
        int max, min;
        for (int j = 0; j < k; ++j) {
            int proceed;
            proceed = pq.top();
            pq.pop();
            if (proceed & 1) {
                max = min = (proceed-1) >> 1;
            }
            else {
                max = proceed >> 1;
                min = max - 1;
            }
            if (max < 0 || min < 0) {
                max = 0; min = 0;
            }
            pq.push(max);
            pq.push(min);
            //printf("max = %d min = %d\n", max, min);
        }
        printf("Case #%d: %d %d\n", i+1, max, min);
    }
}
