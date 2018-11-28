#include<stdio.h>
#include<queue>
int main()
{
    int T, N, K;
    scanf("%d",&T);
    for(int i = 1; i <= T; i++) {
        scanf("%d%d",&N,&K);
        int ans = 0, ans2 = 0;
        std::priority_queue<int> is;
        is.push(N);
        for(int j = 0; j < K; j++) {
            int max = is.top();is.pop();
            ans = max >> 1;
            ans2 = (max & 1 || max == 0) ? ans : (ans-1);
            is.push(ans);
            is.push(ans2);
        }
        printf("Case #%d: %d %d\n", i, ans, ans2);
    }
    return 0;
}
