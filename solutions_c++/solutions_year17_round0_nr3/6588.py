#include <bits/stdc++.h>
using namespace std;

int main() {
    int T, K, N;
    scanf("%d", &T);
    for (int i=1;i<=T;i++){
        scanf("%d %d", &N, &K);
        priority_queue<int> empty_stalls;
        empty_stalls.push(N);
        int processed_hole_count, right, left;
        for (int j = 0; j<K ; j++){
            processed_hole_count = empty_stalls.top();
            empty_stalls.pop();
            left = (processed_hole_count - 1) / 2;
            right = processed_hole_count / 2;
            empty_stalls.push(left);
            empty_stalls.push(right);
        }
        printf("Case #%d: %d %d\n", i, max(left,right), min(left,right));
    }
}
