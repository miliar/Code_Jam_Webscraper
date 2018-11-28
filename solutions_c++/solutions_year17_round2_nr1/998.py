#include <stdio.h>
#include <stdlib.h>
#include <string.h>

const int NN = 4000;

int main()
{
    int t, T;
    scanf("%d", &T);

    for (int t = 1; t <= T; t++)
    {
        int n;
        int road;
        double answer;

        scanf("%d %d", &road, &n);

        double worstTime = 0;
        for (int i = 0; i < n; i++)
        {
            int d, v;
            scanf("%d %d", &d, &v);
            double time = ((double)(road - d)) / (double) v;
            if (time > worstTime) {
                worstTime = time;
            }
        }

        answer = ((double) road) / worstTime;

        printf("Case #%d: %.6lf\n", t, answer);
    }

    return 0;
}
