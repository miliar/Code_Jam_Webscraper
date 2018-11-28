#include <iostream>
#include <string>
#include <vector>

int main() {
    int T;
    std::cin >> T;
    for (int t=1; t <= T; ++t) {
        std::string N_str;
        std::cin >> N_str;
        //std::cout << "N_str: " << N_str << std::endl;

        std::vector<int> N(N_str.size());
        for (int i=0; i < N_str.size(); ++i) {
            N[i] = N_str[i] - '0';
        }

        int end = N.size();
        for (int i=0; i < N.size()-1; ++i) {
            int pos = N.size() - i - 1;
            if (N[pos] == 9) continue;
            if (N[pos] < N[pos-1]) {
                int start = pos-1;
                while (start > 0 && ( N[start] <= N[start-1] || N[start] == 0) ) {
                    start--;
                }
                N[start]--;
                for (int j=start+1; j < end; ++j) {
                    N[j] = 9;
                }
                end = start+1;
            }
        }

        std::cout << "Case #" << t << ": ";

        bool skipZero = true;
        for (int i=0; i < N.size(); ++i) {
            if (skipZero && N[i] == 0) continue;
            std::cout << N[i];
            skipZero = false;
        }
        std::cout << std::endl;
        
    }
    //std::cout << "Finished!" << std::endl;
    return 0;
}
