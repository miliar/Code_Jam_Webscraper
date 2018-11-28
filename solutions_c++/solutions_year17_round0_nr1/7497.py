#include <iostream>
#include <string>
#include <vector>
#include <sstream>
#include <algorithm>
#include <iterator>

#ifndef max
#define max(a,b) (a<b?b:a)
#endif

#ifndef min
#define min(a,b) (a>b?b:a)
#endif

std::string execute(std::string S, int K) {
    std::ostringstream os;

    int out = 0;

    for (unsigned i = 0; i < S.size()-K + 1; ++i) {
        if (S[i] == '-') {
            out++;
            for (int j = 0; j < K; ++j) {
                S[i+j] = (S[i+j] == '-' ? '+' : '-');
            }
        }
    }

    for (int i = 0; i < K; ++i) {
        if (S[S.size()-i-1] == '-') {
            return "IMPOSSIBLE";
        }
    }

    os << out;

    return os.str();
}

std::string parseAndExecute(std::istream& in) {
    std::string S;
    int K;
    in >> S >> K;

    return execute(S,K);
}

int main(int argc, char const *argv[]) {
    int T;
    std::cin >> T; // Number of cases
    for (int i = 1; i <= T; ++i) {

        std::cout << "Case #" << i << ": " 
                  << parseAndExecute(std::cin)
                  << std::endl;
    }
}
