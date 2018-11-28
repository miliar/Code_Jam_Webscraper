#include <cstdlib>
#include <iostream>
#include <iomanip>

using namespace std;

const int N_MAX = 1000;
long K[N_MAX];
long S[N_MAX];

double solve(long D, long N) {
    double max_time = 0;
    double time;
    
    for(long i = 0; i < N; ++i) {
        time = 1. * (D - K[i]) / S[i];
        
        if(time > max_time) {
            max_time = time;
        }
    }
    
    return D / max_time;
}

int main(int argc, char** argv) {
    int T;
    cin >> T;
    
    for(int i = 1; i <= T; ++i) {
        long D, N;
        cin >> D >> N;
        
        for(long k = 0; k < N; ++k) {
            cin >> K[k] >> S[k];
        }
        
        double result = solve(D, N);
        cout << "Case #" << i << ": " << setprecision(6) << fixed << result << "\n";
    }
    
    return 0;
}

