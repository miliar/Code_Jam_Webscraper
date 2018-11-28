#include <sstream>
#include <iostream>


bool is_tidy(size_t& n) {
    int highest = 0;
    std::string letters(std::to_string(n));

    bool reset = false;

    for (size_t i=0; i < letters.length(); ++i) {
        char& c=letters[i];

        if (reset) {
            letters[i] = '9';
            //std::cout << "reset " << i << ", " << letters << std::endl;
            continue;
        }

        int digit = (int)c;
        if (digit < highest) {
            // broken! lower number
            letters[i-1] = (char) ((int)letters[i-1] - 1);
            //c = (char)highest;
            c = '9';
            reset = true;
            //std::cout << "Broken: " << letters << std::endl;
        }

        highest = std::max(highest, digit);
        //std::cout << letters << std::endl;

    }

    if (letters[0] == '0') {
        letters.erase(0, 1);
    }
    n = std::stoul(letters);
    //std::cout << n << "=" << letters << std::endl;

    if (!reset) {
        return true;
    }

    return false;

}
size_t work(size_t num) {
    while (!is_tidy(num)) {
    }
    return num;
}

int main() {
    size_t cases = 0;
    std::cin >> cases;

    for (size_t i = 1; i < cases + 1; ++i) {
        size_t num;
        std::cin >> num;

        std::cout << "Case #" << i << ": ";
        auto ans = work(num);
        std::cout << ans << '\n';
    }
}

