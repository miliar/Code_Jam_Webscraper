#include <iostream>
#include <cstdio>
#include <iomanip>
using namespace std;


int T, D, N;

long double solve(int D, int N) {
    int K, S;
    long double aux, res = -1;
    
    for (int i = 0; i < N; ++i) {
        cin >> K >> S;
        aux = (D - K) / (static_cast<long double>(S));
        aux = D / aux;
        
        if (aux < res || res == -1) {
            res = aux;
        }
    }
    
    return res;
}


int main() {
    cin >> T;
    
    for (int i = 1; i <= T; ++i) {
        cin >> D >> N;
        long double res = solve(D, N);
        cout << "Case #" << i << ": "<< fixed << setprecision(6) << res << "\n";
    }
    
    return 0;
}
