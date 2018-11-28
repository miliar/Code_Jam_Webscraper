#include <iostream>
#include <cstdio>
using namespace std;

int main()
{
    int T;
    cin >> T;
    for (int t = 0; t < T; t++) {
        double maxt = 0;
        int D, N, K, S;
        cin >> D >> N;
        for (int i = 0; i < N; i++) {
            cin >> K >> S;
            if ((double)(D - K) / S > maxt) maxt = (double)(D - K) / S;
            //printf("%d %d %.6f\n", K, S, maxt);
        }
        printf("Case #%d: %.6f\n", t + 1, D / maxt);
    }
    return 0;
}