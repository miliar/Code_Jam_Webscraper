#include <string>
#include <vector>
#include <fstream>
#include <iomanip>
using namespace std;

int main() {
    ifstream    f("in.txt");
    ofstream    g("out.txt");
    int         T; f >> T;
    
    for (int test = 1; test <= T; test++) {
        int                 N, K; f >> N >> K;
        double              U; f >> U;
        vector<double>      P(N);
        
        for (int i = 0; i < N; i++) f >> P[i];
        sort(P.begin(), P.end());

        double lo = 0; double hi = 1;
        for (int steps = 0; steps < 100; steps++) {
            double X = (lo + hi) / 2;
            double C = 0;
            for (int i = 0; i < N; i++) if (P[i] < X) C += X - P[i];
            if (C > U) hi = X; else lo = X;
        }
        
        double X = (lo + hi)/2;
        for (int i = 0; i < N; i++) if (P[i] < X) P[i] = X;
        
        double ans = 1;
        for (int i = 0; i < N; i++) ans *= P[i];
        
        g << setprecision(7) << fixed << "Case #" << test << ": " << ans << endl;
    }
    
    return 0;
}
