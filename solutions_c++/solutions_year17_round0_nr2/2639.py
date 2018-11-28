#include <iostream>
#include <string>

int main()
{
    int T;
    std::cin >> T;

    for (int t = 1; t <= T; ++t) {
        std::string N;
        std::cin >> N;

        for (int i = 1; i < N.size(); ++i) {
            if (N[i] < N[i - 1]) {
                for (int j = i; j < N.size(); ++j) {
                    N[j] = '9';
                }
                for (int j = i - 1; ; --j) {
                    N[j] -= 1;
                    if (j == 0 || N[j] >= N[j - 1]) {
                        break;
                    }
                    N[j] = '9';
                }
                break;
            }
        }

        if (N[0] == '0') {
            N = N.substr(1);
        }

        std::cout << "Case #" << t << ": " << N << std::endl;
    }
}
