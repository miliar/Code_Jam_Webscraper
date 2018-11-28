#include <iostream>

int main() {
    int loop;
    std::cin >> loop;
    //std::cout << loop << std::endl;
    for (int i = 0; i < loop; ++i) {
        std::string s;
        int limit, count = 0;
        bool impossible = false;
        std::cin >> s >> limit;
        //std::cout << s << ": " << limit << std::endl;
        for (int j = 0; j < s.size(); ++j) {
            if (s[j] == '+')
                continue;
            if (s[j] == '-') {
                if (j + limit > s.size()) {
                    impossible = true;
                    break;
                }
                for (int k = 0; k < limit; ++k) {
                    s[j + k] = s[j + k] == '-' ? '+' : '-';
                }
                ++count;
            }
        }
        if (impossible)
            std::cout << "Case #" << i + 1 << ": IMPOSSIBLE" << std::endl;
        else
            std::cout << "Case #" << i + 1 << ": " << count << std::endl;
    }

    return 0;
}
