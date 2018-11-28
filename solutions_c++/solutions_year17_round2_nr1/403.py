#include <bits/stdc++.h>

void test(int t) {
    int D, N;
    std::cin >> D >> N;
    
    double tm = 0;
    for(int i=0; i<N; ++i) {
        double K, S;
        std::cin >> K >> S;
        
        double t = (D-K)/S;
        if(t > tm) {
            tm = t;
        }
    }
    
    std::cout << "Case #" << t << ": " << std::fixed << std::setprecision(9) << D/tm << std::endl;
}

int main() {
    int T;
    std::cin >> T;
    for(int i=1; i<=T; ++i) {
        test(i);
    }
}
