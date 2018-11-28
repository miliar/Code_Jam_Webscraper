#include <iostream>
#include <string>
#include <vector>

void feedback(int index, std::vector<int>& answer) {
    int prev_index = index - 1;
    if (answer[prev_index] <= answer[index]) {
        return;
    }

    answer[prev_index]--;
    if (prev_index > 0) {
        feedback(prev_index, answer);
    }
    answer[index] = 9;
}

int main() {
    int T;
    std::cin >> T;

    for (int t = 0; t < T; t++) {
        std::string s;
        std::cin >> s;

        std::vector<int> answer(s.length());
        int latest = 0;

        for (int i = 0; i < s.length(); i++) {
            answer[i] = s[i] - '0';
            if (latest > answer[i]) {
                feedback(i, answer);
                break;
            }
            latest = answer[i];
        }

        bool is_leading_zero = true;
        bool is_end = false;
        std::cout << "Case #" << (t+1) << ": ";
        for (int i = 0; i < s.length(); i++) {
            if (answer[i] == 9 || is_end) {
                std::cout << 9;
                is_end = true;
            } else if (answer[i] != 0) {
                std::cout << answer[i];
                is_leading_zero = false;
            } else if (!is_leading_zero) {
                std::cout << answer[i];
            }
        }
        std::cout << std::endl;
    }
}
