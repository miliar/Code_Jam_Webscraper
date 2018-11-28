#include <cstdio>
#include <cstring>
#include <vector>
#include <queue>

#define INF 2e9

using namespace std;

typedef pair<int, int> ii;

int main()
{
    int T;
    scanf("%d", &T);

    for (int t = 1; t <= T; ++t) {

        char in[11];
        scanf(" %s", in);
        int n = strlen(in);
        int s = 0;
        for (int i = 0; i < n; ++i) {
            s <<= 1;
            if (in[i] == '+')
                s |= 1;
        }
        int k;
        scanf("%d", &k);

        vector<int> shortest(1024, INF);
        queue<ii> q;
        q.push({s, 0});
        while (!q.empty()) {
            int state = q.front().first;
            int dist = q.front().second;
            q.pop();
            if (shortest[state] != INF)
                continue;
            shortest[state] = dist;
            if (state == (1 << n) - 1)
                break;
            
            int mask = (1 << k) - 1;
            for (int i = 0; i < n-k+1; ++i) {

                int newState = state ^ mask;
                if (shortest[newState] == INF)
                    q.push({newState, dist+1});

                mask <<= 1;
            }
        }

        printf("Case #%d: ", t);
        int target = (1 << n) - 1;
        if (shortest[target] == INF)
            printf("IMPOSSIBLE");
        else
            printf("%d", shortest[target]);
        printf("\n");

    }

    return 0;
}