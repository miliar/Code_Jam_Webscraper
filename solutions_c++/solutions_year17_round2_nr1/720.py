#include <iostream>
#include <stdio.h>

using namespace std;

int main ()
{
    int T;
    cin >> T;

    for (int t = 1; t <= T; ++t)
    {
        int D, N;
        cin >> D >> N;

        double arr_time = 0.0;
        for (int n = 0; n < N; ++n)
        {
            int k, s;
            cin >> k >> s;

            double t = (double)(D - k) / (double)(s);
            arr_time = max(arr_time, t);
        }

        double speed = (double)D/(double)(arr_time);
        printf("Case #%d: %.6f\n", t, speed);
    }
}
