#include <iostream>
#include <stdio.h>
#include <string>

using namespace std;

int main(int argc, char* argv[]) {
    int T; cin >> T;
    for (int t = 0; t < T; t++) {
        int D, N; cin >> D >> N;
        int K[1000], S[1000];
        double dest_time[1000];
        double min_dest_time;
        for (int i = 0; i < N; i++) {
            cin >> K[i] >> S[i];
            dest_time[i] = (double)(D-K[i])/(double)S[i];
            if (i == 0) min_dest_time = dest_time[i];
            else if (min_dest_time > dest_time[i]) min_dest_time = dest_time[i];
        }
        double v = (double)D/min_dest_time;
        for (int i = 0; i < N; i++) {
            if (v*dest_time[i] > D) v = D/dest_time[i];
        }
        printf("Case #%d: %.6f\n", t+1, v);
        //cout << "Case #" << (t+1) << ":" << endl;
    }
    return 0;
}

