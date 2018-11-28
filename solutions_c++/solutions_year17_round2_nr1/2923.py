#include <iostream>

int T;
long long int D, N;
long long K, S;
double max;

int main(){
    std::cin >> T;
    for (int t = 1; t <= T; t++){
        std::cin >> D >> N;
        max = 0;
        for (int i = 0; i < N; i++){
            std::cin >> K >> S;
            double tmp = (double)(D-K) / S;
            if (max < tmp){
                max = tmp;
            }
        }
        printf("Case #%d: %lf\n", t, D/max);
    }
    return 0;
}
