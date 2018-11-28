#include <iostream>
#include <string>

int f(std::string S, int K) {
    int len = S.size();
    int flip = 0;
    for (int i = 0; i < len - K + 1; ++i) {
        
        if (S[i] == '-') {
            ++flip;
            for (int j = 0; j < K; ++j)
                S[i + j] = S[i + j] == '-' ? '+' : '-';
        }
    }
    
    for (int i = 0; i < len; ++i)
        if (S[i] == '-') return -1;
    return flip;
}


int main() {
    int n;
    std::cin >> n;
    for (int i = 0; i < n; ++i) {
        std::string S;
        int K;
        std::cin >> S >> K;
        int res = f(S, K);
        if (res != -1)
            std::cout << "Case #" << (i+1) << ": " << res << std::endl;
        else
            std::cout << "Case #" << (i+1) << ": IMPOSSIBLE" << std::endl;
    }

    return 0;
}