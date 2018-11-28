#include <iostream>
#include <string>
#include <vector>

void Flip(std::vector<int> &data, int pos, int flips) {
    for (int i = 0; i < flips; ++i)
        data[pos + i] = 1 - data[pos + i];
}

int Work(const std::string &d, int flips) {
    int n = d.size();
    std::vector<int> data(n);
    for (int i = 0; i < n; ++i)
        if (d[i] == '+')
            data[i] = 1;
    int res = 0;
    for (int i = 0; i <= n - flips; ++i) {
        if (data[i] == 1)
            continue;
        ++res;
        Flip(data, i, flips);
    }
    for (int i = 0; i < n; ++i)
        if(data[i] != 1)
            return -1;
    return res;
}

void Output(int test, int result) {
    std::cout << "Case #" << test << ": ";
    if (result >= 0)
        std::cout << result;
    else
        std::cout << "IMPOSSIBLE";
    std::cout << std::endl;
}

int main() {
    int n;
    std::cin >> n;
    for (int i = 1; i <= n; ++i) {
        std::string data;
        int k;
        std::cin >> data >> k;
        Output(i, Work(data, k));
    }
    return 0;
}

