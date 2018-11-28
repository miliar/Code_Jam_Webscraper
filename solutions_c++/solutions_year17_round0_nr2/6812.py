#include <iostream>

int main() {
    int cc;
    std::cin >> cc;

    for(int c = 0; c < cc; c++) {
        std::string n; std::cin >> n;
        unsigned long long int nn = std::stoull(n.c_str());
        n = std::to_string(nn);

        std::cout << "Case #" << (c+1) << ": ";

        if(n.length() > 1) {
            bool flag = false;
            while(!flag) {
                const char* nc = n.c_str();
                for(int i = 1; i < n.length(); i++) {
                    for(int j = 0; j < i; j++) {
                        flag = (nc[i] - '0') >= (nc[j] - '0');

                        if(!flag) break;
                    }

                    if(!flag)
                        break;
                }
                n = std::to_string(--nn);
            }

            nn++;
        }

        std::cout << nn;

        std::cout << std::endl;
    }
    return 0;
}