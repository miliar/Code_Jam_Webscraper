#include <iostream>

int main() {
    unsigned int T;
    std::cin >> T;

    for(unsigned int i = 0; i < T; ++i) {

        std::string str;
        std::cin >> str;

        unsigned int lastBigger = 0;
        bool sorted = true;
        for(unsigned int j = 0; j + 1 < str.size(); ++j) {
            if(str[j] > str[j + 1]) {
                sorted = false;
                break;
            } else if(str[j] < str[j + 1]) {
                lastBigger = j + 1;
            }
        }

        if(!sorted) {
            if(str[lastBigger] == '1') {
                str.pop_back();
            } else {
                str[lastBigger]--;
                lastBigger++;
            }

            for(unsigned int j = lastBigger; j < str.size(); ++j) {
                str[j] = '9';
            }
        }
        
        std::cout << "Case #" << (i + 1) << ": " << str;

        if(i + 1 < T) {
            std::cout << std::endl;
        }
    }

    return 0;
}