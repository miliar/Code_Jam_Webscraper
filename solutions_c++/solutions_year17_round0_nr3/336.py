#include <fstream>
using namespace std;

int main() {
    ifstream    f("in.txt");
    ofstream    g("out.txt");
    int         T; f >> T;
    
    for (int test = 1; test <= T; test++) {
        uint64_t    N, K; f >> N >> K;
        uint64_t    K1 = 1, K2 = 0;
        
        while (K1 + K2 < K) {
            K -= K1 + K2;
            if (N & 1) K1 = 2*K1 + K2; else K2 = 2*K2 + K1;
            N = (N - 1)/2;
        }
        if (K <= K2) N++;
        
        g << "Case #" << test << ": " << N/2 << " " << (N - 1)/2 << endl;
    }
    
    return 0;
}
