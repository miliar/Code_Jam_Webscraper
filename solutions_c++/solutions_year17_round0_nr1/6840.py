#include <iostream>

int main() {
    int cc;
    std::cin >> cc;

    std::size_t f;
    for(int c = 0; c < cc; c++) {
        std::string cl; std::cin >> cl;
        int K; std::cin >> K;

        std::cout << "Case #" << (c+1) << ": ";

        int cnt = 0;
        bool flag = false;
        std::size_t f = cl.find('-');
        if(f == std::string::npos)
            std::cout << "0";
        else {
            for(int i = 0; i < cl.length() && !flag; i++) {
                if(cl[i] == '-') {
                    cnt++;
                    for(int j = i; j < i + K && !flag; j++) {
                        if(j >= cl.length())
                            flag = true;
                        else
                            cl[j] = cl[j] == '+' ? '-' : '+';
                    }
                }
            }

            if(flag)
                std::cout << "IMPOSSIBLE";
            else
                std::cout << cnt;
        }

        std::cout << std::endl;
    }
    return 0;
}