#include <iostream>
#include <string>
#include <algorithm>
#include <vector>

typedef long long lint;
int T;

void UnitTest(int CaseId) {
    lint n;
    std::cin >> n;
    std::string s = std::to_string(n);
    std::vector<int> nv;
    int ns = s.length();
    lint base = 1L, mul;
    for (int i = 0; i < ns; i ++) {
        nv.push_back(s[i] - '0');
        if (i) base *= 10L;
    }
    mul = base;
    int sort_prefix = 0;
    for (int i = 1; i < ns; i ++) {
        if (nv[i - 1] <= nv[i]) {
            sort_prefix = i;
        } else {
            break;
        }
    }
    if (sort_prefix == ns - 1) {
        std::cout << "Case #" << CaseId << ": " << n << '\n'; return ;
    }
    int d = 0;
    for (int i = sort_prefix; i; i --) {
        if (nv[i - 1] != nv[i]) {
            d = i;
            break;
        }
    }
    lint prefix = 0;
    for (int i = 0; i < d; i ++) {
        prefix = prefix + nv[i] * mul;
        mul /= 10L;
    }
    prefix = prefix + mul * (nv[d] - 1) + mul - 1;
    std::cout << "Case #" << CaseId << ": " << prefix << '\n';
}

int main() {
    std::cin >> T;
    for (int i = 1; i <= T; i ++) {
        UnitTest(i);
    }
    return 0;
}
