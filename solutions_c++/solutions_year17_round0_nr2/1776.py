
#include <iostream>
#include <vector>
#include <string>

main() {
    int T;
    std::cin >> T;
    for(int t = 1; t <= T; t++) {
        std::cout << "Case #" << t << ": ";
        std::string S;
        std::cin >> S;
        std::vector<int> digits;
        for(int i = 0; i < S.size(); i++)
            digits.push_back(S[i] - '0');

        for(int i = S.size(); i >= 0; i--) {
            std::vector<int> decreased;
            int decreasedIndex = i;
            for(int j = 0; j < digits.size(); j++) {
                if(j < decreasedIndex)
                    decreased.push_back(digits[j]);
                else if(j == decreasedIndex)
                    decreased.push_back(digits[j] - 1);
                else if(j > decreasedIndex)
                    decreased.push_back(9);
            }
            bool isValid = true;
            for(int j = 0; j < decreased.size() - 1; j++) {
                if(decreased[j] < 0 || decreased[j+1] < 0 || (decreased[j] > decreased[j+1]))
                    isValid = false;
            }
            if(isValid) {
                long long answer = 0LL;
                for(int j = 0; j < decreased.size(); j++) {
                    answer *= 10;
                    answer += decreased[j];
                }
                std::cout << answer << '\n';
                break;
            }
        }
    }
    return 0;
}
