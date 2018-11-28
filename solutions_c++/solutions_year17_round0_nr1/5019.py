#include <iostream>
#include <unordered_set>
#include <string>

#define IMPOSSIBLE "IMPOSSIBLE"
void flip(char& pancake) {
    pancake == '+' ? pancake = '-' : pancake = '+';
}

std::string oversizedFilpper(std::string pancakes, int n) {
    int l = pancakes.size();
    int count = 0;
    if (l < n) {
        return IMPOSSIBLE;
    }
    for (int j = 0; j <= l - n; j++) {
        // std::cout << pancakes << std::endl;
        if (pancakes[j] == '-') {
            for (int k = j; k < j + n; k++) {
                flip(pancakes[k]);
            }
            count++;
        }
    }

    for (int k = l - n + 1; k < l; k++) {
        if (pancakes[k] == '-') {
            return IMPOSSIBLE;
        }
    }

    return std::to_string(count);
}

int main() {
    int t;
    std::cin >> t;
    for (int i = 1; i <= t; i++) {
        std::string pancakes;
        int n;
        std::cin >> pancakes >> n;
        
        std::cout << "Case #" << i << ": " << oversizedFilpper(pancakes, n) << std::endl;
    }
    return 0;
}

