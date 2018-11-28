#include <bits/stdc++.h>

using namespace std;

#define FILE_IO

int main()
{
    #ifdef FILE_IO
    freopen("1.in", "r", stdin);
    freopen("1.out", "w", stdout);
    #endif

    int T;
    scanf("%d", &T);
    for(int test = 1; test <= T; test++)
    {
        printf("Case #%d: ", test);
        int N, K;
        scanf("%d%d", &N, &K);

        priority_queue <int> pq;
        pq.push(N);

        int pos, lft, rgt;
        for(int i = 1; i <= K; i++)
        {
            int l = pq.top();
            pq.pop();

            pos = (l + 1) / 2;
            lft = pos - 1;
            rgt = l - pos;

            pq.push(lft);
            pq.push(rgt);
        }

        printf("%d %d\n", rgt, lft);
    }


    return 0;
}
