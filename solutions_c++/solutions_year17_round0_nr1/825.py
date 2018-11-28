#include <iostream>
#include <string>
#include <vector>

int main() {
    int T;
    std::cin >> T;
    for(int C = 1; C <= T; C ++) {
        std::string line;
        std::cin >> line;
        int K;
        std::cin >> K;

        std::vector<int> state;
        for(auto c : line) state.push_back(c == '+'? 1 : 0);
        int N = line.length();

        int count = 0;
        for(int i = 0; i + K <= N; i ++) {
            //std::cout << "i = " << i << std::endl;
            //std::cout << "    state: ";
            //for(auto i : state) std::cout << i;
            //std::cout << std::endl;
            if(state[i] == 0) {
                count ++;
                for(int j = 0; j < K; j ++) state[i+j] = 1 - state[i+j];
            }
        }

        bool success = true;
        for(auto i : state) success = success && (i == 1);

        std::cout << "Case #" << C << ": ";
        if(success) std::cout << count << std::endl;
        else std::cout << "IMPOSSIBLE" << std::endl;
    }
    return 0;
}
