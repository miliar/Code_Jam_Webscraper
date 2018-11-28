
#include <cstdio>
#include <iostream>
#include <vector>
#include <queue>
#include <fstream>
#include <string>
using namespace std;

long long int T, D, N;
long long int K[1001], S[1001];
int main () {
    cin >> T;
    
    for(int tcase=1;tcase <= T; tcase++) {
        cin >> D >> N;
        for(int i = 0; i < N; i++) {
            cin >> K[i] >> S[i];
        }
        double t = 0.0;
        for(int i = N-1;i >= 0; i--) {
            double s = (double)(D - K[i]) / (double)S[i];
            if(s > t) {
                t = s;
            }
        }
        printf("Case #%d: %.6f\n", tcase, (double) D / t);
    }
    
    return 0;
}
