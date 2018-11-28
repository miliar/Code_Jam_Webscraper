#include <stdio.h>
#include <string.h>
#include <algorithm>
#include <vector>
#include <map>

using namespace std;


int main(int argc, char **argv)
{
    freopen("input.txt", "rt", stdin);
    freopen("output.txt", "wt", stdout);

    int T;
    scanf("%d", &T);

    for (int test = 1; test <= T; test++) {
        printf("Case #%d: ", test);
        
        int D, N;
        scanf("%d %d", &D, &N);

        double max_time = -1;
        for (int n = 0; n != N; n++) {
            int K, S;
            scanf("%d %d", &K, &S);

            double dist = D - K;
            double ttime = dist / S;
            if (max_time < ttime) 
                max_time = ttime;
        }

        double ans = D/max_time;

        printf("%0.7f\n", ans);
    }
	return 0;
}

