#include <iostream>
#include <string>
#include <vector>

bool flip(std::string &s, unsigned int start, unsigned int length)
{
    if(start >= 0 && start + length <= s.size()) {
        for (unsigned int i = start; i < start + length; ++i) {
            switch (s[i]) {
                case '+':
                    s[i] = '-';
                    break;
                case '-':
                    s[i] = '+';
                    break;
            }
        }
        return true;
    }
    else return false;
}

int main() {
    unsigned int T;
    std::cin >> T;

    for(unsigned int i = 0; i < T; ++i) {
        std::string s;
        unsigned int K;

        std::cin >> s;
        std::cin >> K;

        unsigned int c = 0;
        bool needsFlip = false;
        for(unsigned int j = 0; j < s.size(); ++j) {
            if(s[j] == '-') {
                needsFlip = true;
                if(flip(s, j, K)) {
                    c++;
                    needsFlip = false;
                }
            }
        }

        std::cout << "Case #" << (i + 1) << ": ";
        if(needsFlip) {
            std::cout << "IMPOSSIBLE";
        } else {
            std::cout << c;
        }
        if(i + 1 < T) std::cout << std::endl;
    }

    return 0;
}