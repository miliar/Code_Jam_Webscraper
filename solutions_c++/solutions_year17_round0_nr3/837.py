#include <iostream>
#include <vector>
#include <stdint.h>
#include <algorithm>
#include <map>

int main() {
    int T;
    std::cin >> T;
    for(int C = 1; C <= T; C ++) {
        uint64_t N, K;
        std::cin >> N >> K;

        //std::vector<std::pair<uint64_t, uint64_t>> groups;
        std::map<uint64_t, uint64_t> groups;

        //groups.push_back(std::make_pair(1, N));
        groups[N] = 1;

        //std::cout << "Starting with N = " << N << " and K = " << K << std::endl;
        while(K > 0) {
            uint64_t largest = groups.rbegin()->first;
            uint64_t count = groups[largest];

            //std::cout << "\tgroups:" << std::endl;
            //for(auto g : groups) {
                //std::cout << "\t\tgroups[" << g.first << "] = " << g.second << std::endl;
            //}
            //std::cout << "\tlargest found: " << largest << std::endl;

            if(count < K) {
                K -= count;
                if(largest % 2 == 1) {
                    groups[largest / 2] += count * 2;
                }
                else {
                    groups[largest / 2] += count;
                    groups[(largest / 2) - 1] += count;
                }
            }
            else {
                //std::cout << "largest: " << largest << std::endl;
                largest --;
                uint64_t min = largest / 2;
                uint64_t max = largest - min;
                std::cout << "Case #" << C << ": " << max << " " << min << std::endl;
                break;
            }

            groups.erase(groups.find(largest));
        }
    }
    return 0;
}
