#include <iostream>
#include <string>

void flip(std::string &state, int k, int start)
{
    auto end = start + k;
    for (int i = start; i < end; i++) {
        if (state[i] == '-') {
            state[i] = '+';
        } else {
            state[i] = '-';
        }
    }
}

int solve(std::string state, int k)
{
    const int l = state.length();
    const auto last = l-k;
    int count = 0;
    for (int i = 0; i <= last; ++i) {
       if (state[i] == '-') {
           flip(state, k, i);
           ++count;
       }
    }
    for (int i = last+1; i < l; ++i) {
        if (state[i] == '-') {
            return -1;
        }
    }
    return count;
}

int main()
{
    int T;
    std::cin >> T;
    for (int i = 1; i <= T; ++i) {
        std::string S;
        std::cin >> S;
        int K;
        std::cin >> K;
        int r = solve(S, K);
        std::cout << "Case #" << i << ": ";
        if (r >= 0) {
            std::cout << r << '\n';
        } else {
            std::cout << "IMPOSSIBLE\n";
        }
    }
    return 0;
}
