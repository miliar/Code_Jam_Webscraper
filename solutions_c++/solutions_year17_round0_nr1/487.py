#include <iostream>
#include <algorithm>
#include <string>
#include <vector>


bool flipK(int start_index, int K, std::vector<int>& cakes) {
    if (start_index > cakes.size() - K ) return false;
    for (int i=0; i < K; ++i) {
        int pos = start_index + i;
        cakes[pos] ^= 1;
    }
    return true;
}


void printv(const std::vector<int>&  v) {
    //for (int i=0; i < v.size(); ++i) std::cout << v[i];
    //std::cout << std::endl;
}

void print_loc(int loc) {
    //for (int i=0; i < loc; ++i) std::cout << " ";
    //std::cout << "^" << std::endl;
}

int main() {
    int T;
    std::cin >> T;
    // std::cout << "T: " << T << std::endl;
    for (int t=1; t <= T; ++t) {
        std::string S;
        int K;
        std::cin >> S >> K;
        //std::cout << "S: " << S << " | K: " << K << std::endl;
        
        int y=0;
        std::vector<int> cakes(S.size(),0);
        for (int i=0; i < S.size(); ++i) {
            if (S[i] == '+') cakes[i] = 1;
        }
        for (int i=0; i <= cakes.size() - K; ++i) {
            printv(cakes);
            if (cakes[i] == 0) {
                bool successFlip = flipK(i, K, cakes);
                if (successFlip) {
                    y++;
                    print_loc(i);
                }
                else {
                    break;
                }
            }
        }

        bool is_possible = true;
        for (int i=cakes.size()-1; i >= cakes.size() - K; --i) {
            //std::cout << i << ": " << cakes[i] << " | " << cakes.size() << " | " << K <<  std::endl;
            if (cakes[i] == 0) {
                is_possible = false;
                break;
            }
            if (i == cakes.size() - K) break;
        }

        if (is_possible) std::cout << "Case #" << t << ": " << y << std::endl;
        else std::cout << "Case #" << t << ": IMPOSSIBLE" << std::endl;

    }
    //std::cout << "Finished!" << std::endl;
    return 0;
}
