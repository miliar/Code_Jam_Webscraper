#include <bits/stdc++.h>

#define M_PI           3.14159265358979323846

using namespace std;

int main(){
    ifstream input("a.in");
    ofstream output;
    output.open ("a.out");
    unsigned long long T;

    input >> T;
    for(unsigned int i = 0; i < T; i++) {
        cout << "Progress " << i << " / " << (T - 1) << endl;
        int N, K;
        input >> N >> K;
        int R[N];
        int H[N];
        double Sh[N];
        for(int j = 0; j < N; j++) {
            input >> R[j] >> H[j];
            Sh[j] = 2 * M_PI * (double)R[j] * (double)H[j];
        }
        double surface = 0;
        double biggest_top = 0;
        int max_idx = 0;
        for(int j = 0; j < K - 1; j++) {
            for(int k = 0; k < N; k++) {
                if(Sh[k] > Sh[max_idx]) {
                    max_idx = k;
                }
            }
            if(M_PI * R[max_idx] * R[max_idx] > biggest_top) {
                biggest_top = M_PI * R[max_idx] * R[max_idx];
            }
            surface += Sh[max_idx];
            Sh[max_idx] = 0;
            R[max_idx] = 0;
        }
        int max_top_idx = 0;
        for(int k = 0; k < N; k++) {
            if(Sh[k] > Sh[max_idx]) {
                max_idx = k;
            }
            if(M_PI * R[k] * R[k] > M_PI * R[max_top_idx] * R[max_top_idx]) {
                max_top_idx = k;
            }
        }
        if(M_PI * R[max_idx] * R[max_idx] > biggest_top) biggest_top = M_PI * R[max_idx] * R[max_idx];
        double surface2 = surface + Sh[max_top_idx] + M_PI * R[max_top_idx] * R[max_top_idx];
        surface += Sh[max_idx] + biggest_top;
        if(surface2 > surface) surface = surface2;
        output << "Case #" << (i + 1) << ": " << fixed << surface << endl;
    }
    output.close();
    return 0;
}
