#include <iostream>
#include <string>
#include <vector>
#include <algorithm>

std::string ReadData() {
    std::string n;
    std::cin >> n;
    return n;
}

std::string Work(const std::string &n) {
    std::vector<int> num;
    for (int i = 0; i < n.size(); ++i)
        num.push_back(n[i] - '0');
    std::reverse(num.begin(), num.end());
    int i;
    for (i = static_cast<int>(num.size()) - 1; i > 0 && num[i] <= num[i - 1]; --i)
        ;
    if (i > 0) {
        for (; i + 1 < num.size() && num[i] == num[i + 1]; ++i)
            ;
        for (int j = 0; j < i; ++j)
            num[j] = 9;
        int c = 1;
        for (; c != 0 && i < num.size(); ++i) {
            num[i] = num[i] - c;
            if (num[i] < 0) {
                num[i] += 10;
                c = 1;
            } else {
                c = 0;
            }
        }
        for (i = static_cast<int>(num.size()) - 1; i > 0 && num[i] == 0; --i)
            num.pop_back();
    }
    std::string result;
    for (int i = static_cast<int>(num.size()) - 1; i >= 0; --i)
        result += (num[i] + '0');
    return result;
}

void Output(int test, const std::string &result) {
    std::cout << "Case #" << test << ": " << result << std::endl;
}

int main() {
    int n;
    std::cin >> n;
    for (int i = 1; i <= n; ++i)
        Output(i, Work(ReadData()));
    return 0;
}

