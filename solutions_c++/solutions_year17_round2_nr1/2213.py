#include <iomanip>
#include <fstream>
using namespace std;

int main() {
    ifstream    f("in.txt");
    ofstream    g("out.txt");
    int         T; f >> T;
    
    for (int test = 1; test <= T; test++) {
        int     D, N; f >> D >> N;
        double  X, H, S;

        X = 1e4*D + 1;
        for (int i = 0; i < N; i++) {
            f >> H >> S;
            X = min(X, (double)S*D/(D - H));
        }
        
        g << "Case #" << test << ": " << fixed << setprecision(6) << X << endl;
    }
    
    return 0;
}
