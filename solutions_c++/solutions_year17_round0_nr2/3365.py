#include <iostream>

void check_back_borrow(std::string &s, int pos) {
    if (pos == 0) {
        s[pos] -= 1;
        return;
    }
    if (s[pos] == '0') {
        s[pos] = '9';
        check_back_borrow(s, pos - 1);
        return;
    }
    s[pos] -= 1;
    if (s[pos] < s[pos - 1]) {
        s[pos] = '9';
        check_back_borrow(s, pos - 1);
    }
    return;
}

int main() {
    int loop;
    std::cin >> loop;
    //std::cout << loop << std::endl;
    for (int i = 0; i < loop; ++i) {
        std::string s;
        std::cin >> s;
        bool back_borrow = false;
        //std::cout << s << std::endl;
        for (int j = 0; j < s.size(); ++j) {
            if (j == 0)
                continue;
            if (back_borrow)
                s[j] = '9';
            if (s[j] >= s[j - 1])
                continue;
            //s[j - 1] -= 1;
            s[j] = '9';
            back_borrow = true;
            check_back_borrow(s, j - 1);
        }
        std::cout << "Case #" << i + 1 << ": " << std::stol(s) << std::endl;
    }

    return 0;
}
