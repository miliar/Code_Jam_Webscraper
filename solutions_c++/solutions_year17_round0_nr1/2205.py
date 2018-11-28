#include <iostream>
#include <vector>
#include <algorithm>
#include <queue>
#include <string>
using namespace std;


int main()
{
    int T_T, t_t;
    std::cin >> T_T;
    for (t_t = 1; t_t <= T_T; ++t_t) {
        std::cout << "Case #" << t_t << ": ";
        std::string s;
        int N;
        std::cin >> s;
        std::cin >> N;
        int cnt = 0;
        for (int i = 0; i <= s.length()-N; ++i) {
            if (s[i] == '-') {
                ++cnt;
                for (int j = 0; j < N; ++j) {
                    if (s[i+j] == '-')
                        s[i+j] = '+';
                    else 
                        s[i+j] = '-';
                }
            }
        }
        for (int i = s.length()-N; i < s.length(); ++i) {
            if (s[i] == '-') {
                cnt = -1;
                break;
            }
        }
        if (cnt == -1)
            std::cout << "IMPOSSIBLE" << std::endl;
        else
            std::cout << cnt << std::endl;
    }
    return 0;
}
