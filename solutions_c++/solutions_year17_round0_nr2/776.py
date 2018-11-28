#include <bits/stdc++.h>

std::string number;

void init() {
    std::cin >> number;
}

void work() {
    std::string answer;
    int cur = 0;
    for (int i = 0; i < (int)number.length(); i++) {
        for (int j = cur; j <= 9; j++) {
            std::string tmp = answer;
            for (int k = i; k < (int)number.length(); k++) {
                tmp += (char)('0' + j);
            }
            if (tmp <= number) {
                cur = j;
            } else {
                break;
            }
        }
        answer += (char)('0' + cur);
    }
    while (answer[0] == '0') {
        answer.erase(0, 1);
    }
    std::cout << answer << std::endl;
}

int main() {
    freopen("b.in", "r", stdin);
    freopen("b.out", "w", stdout);

    int testCount;
    std::cin >> testCount;
    for (int i = 1; i <= testCount; i++) {
        printf("Case #%d: ", i);
        init();
        work();
    }

    return 0;
}
