#include <iostream>

long long int T;
long long int N, K;

int main(){
    std::cin >> T;
    for (long long int t = 1; t <= T; t++){
        std::cin >> N >> K;
        long long int s;
        long long int s2;
        for (s = 1; s*2 <= K; s*=2);
        K -= s;
        for (s2 = 1; s2 < s; s2*=2){
            if (K & s2){
                N--;
                K -= s2;
            }
            N /= 2;
        }
        long long int max = N/2;
        long long int min = (N-1)/2;
        std::cout << "Case #" << t << ": " << max << " " << min << std::endl;
    }
    return 0;
}
