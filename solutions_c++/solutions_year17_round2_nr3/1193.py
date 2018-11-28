#include <iostream>
#include <string>
#include <cfloat>
#include <iomanip>
#include <stdio.h>

using namespace std;

void print_arr(int* a, int n) {
    for (int i=0; i<n; ++i) {
        cout << a[i] << " ";
    }
    cout << endl;
}

void print_arr(double* a, int n) {
    for (int i=0; i<n; ++i) {
        cout << a[i] << " ";
    }
    cout << endl;
}


int main() {
    int T;
    cin >> T;
    for (int tt=1; tt<=T; ++tt) {
        int temp;
        int N;
        cin >> N >> temp;
        int cap[N], speed[N], dist[N];
        double time[N];
        for (int i=0; i<N; ++i) {
            cin >> cap[i] >> speed[i];
        }
        for (int i=0; i<N; ++i) {
            for (int j=0; j<N; ++j) {
                cin >> temp;
                if (i+1 == j) {
                    dist[i] = temp;
                }
            }
        }

//        print_arr(cap, N);
//        print_arr(speed, N);
//        print_arr(dist, N);
        cin >> temp;
        cin >> temp;

        time[N-1] = 0;
        for (int i=N-2; i>=0; --i) {
            double min_time = DBL_MAX;
            int cur_dist = 0;
            for (int j=i+1; j<N; ++j) {
                cur_dist += dist[j-1];
                if (cur_dist > cap[i])
                    break;
                double new_time = (double)cur_dist / speed[i] + time[j];
                if (new_time < min_time)
                    min_time = new_time;
            }
            time[i] = min_time;
        }
        printf ("Case #%d: %.6lf\n", tt, time[0]);
    }
    return 0;
}
