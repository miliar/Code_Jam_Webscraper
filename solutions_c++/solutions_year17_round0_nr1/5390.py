#include <iostream>
#include <vector>
#include <string>
#include <algorithm>

using uint_t = uint64_t;

template <typename Iterator>
void flip(Iterator first, Iterator last) {
    for (auto it = first; it != last; ++it) {
        (*it).flip();
    }
}


int main() {
    uint_t T;
    std::cin >> T;
    for (uint_t t = 1; t <= T; ++t) {
        std::string line;
        uint_t K;
        std::vector<bool> pancakes;
        std::cin >> line >> K;
        for (auto& symbol : line) {
            pancakes.push_back( (symbol == '+') );
        }
 
        bool possible = true;
        uint_t iterations = 0;
        auto position = pancakes.begin();
        uint_t to_flip = std::count(pancakes.begin(), pancakes.end(), false);
        
        for (auto it = pancakes.begin(); it != pancakes.end()-K+1; ++it) {
            if (*it ==  0){
                flip(it, it+K);
                ++iterations;
            }
        }
        
        possible = (std::count(pancakes.begin(), pancakes.end(), false) == 0);
        
        std::cout << "Case #" << t << ": ";
        if (possible) {
            std::cout << iterations << std::endl;
        } else {
            std::cout << "IMPOSSIBLE" << std::endl;
        }
    }
    return 0;
}
