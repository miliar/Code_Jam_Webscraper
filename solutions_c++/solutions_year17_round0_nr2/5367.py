#include <iostream>
#include <deque>
#include <cassert>

using uint_t = uint64_t;
using container_t = std::deque<uint_t>;

bool is_tidy(container_t& number) {
    for (uint_t i = 0; i < number.size()-1; ++i) {
        if (number[i] > number[i+1]) {
            return false;
        }
    }
    return true;
}

container_t containerize(uint_t n) {
    container_t number;
    while (n != 0) {
        number.push_front(n % 10);
        n /= 10;
    }
    return number;
}

int main() {
    uint_t T;
    std::cin >> T;
    for (uint_t t = 1; t <= T; ++t) {
        std::cout << "Case #" << t << ": ";
        uint_t n;
        std::cin >> n;
        auto number = containerize(n);
        if (is_tidy(number)) {
            std::cout << n << std::endl;
            continue;
        }
        auto new_number(number);
        for (uint_t i = 0; i < number.size()-1; ++i) {
            if (number[i] > number[i+1])  {
                new_number[i] = number[i]-1;
                for (uint_t j = i+1; j < number.size(); ++j) {
                    new_number[j] = 9;
                }
                for (uint_t j = i; j >= 1; --j) {
                    if (new_number[j] <  new_number[j-1]) {
                        new_number[j] = 9;
                        --new_number[j-1];
                    }
                }
                break;
            }
        }
        
        assert(is_tidy(new_number));
        
        for (auto& element : new_number) {
            if (element != 0) {
                std::cout << element;
            }
        }
        std::cout << std::endl;       
        
    }
}
