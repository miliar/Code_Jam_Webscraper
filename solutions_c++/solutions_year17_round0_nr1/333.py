#include <string>
#include <fstream>
using namespace std;

int main() {
    ifstream    f("in.txt");
    ofstream    g("out.txt");
    int         T, K; f >> T;
    string      S;
    
    for (int test = 1; test <= T; test++) {
        f >> S >> K;
        
        int flips   = 0;
        int N       = (int)S.size();
        for (int i = 0; i + K <= N; i++) if (S[i] == '-') {
            flips++;
            for (int k = 0; k < K; k++) S[i + k] = '+' + '-' - S[i + k];
        }
        
        for (int i = N - K; i < N; i++) if (S[i] == '-') flips = -1;
        
        g << "Case #" << test << ": " << ((flips == - 1) ? "IMPOSSIBLE" : to_string(flips)) << endl;
    }
    

    return 0;
}
