#include <iostream>
#include <string>
#include <bitset>

const int N = 1000 + 1;
int T;

std::bitset<N> bs;

void UnitTest(int CaseId) {
    int k; std::string s;
    std::cin >> s >> k;
    const int ns = s.length();
    bs.reset();
    for (int i = 0; i < ns; i ++) {
        bs.set(i, s[i] == '-');
    }
    int answer = 0;
    for (int i = 0; i <= ns - k; i ++) {
        if (bs[i]) {
            for (int j = 0; j < k; j ++) {
                bs.flip(i + j);
            }
            answer ++;
        }
    }
    std::cout << "Case #" << CaseId << ": " << (bs.count() ? "IMPOSSIBLE" : std::to_string(answer)) << '\n';
}

int main() {
    std::cin >> T;
    for (int i = 1; i <= T; i ++) {
        UnitTest(i);
    }
    return 0;
}
