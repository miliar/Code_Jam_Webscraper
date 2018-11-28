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

std::string execute(std::string N) {
    uint32_t i = 0;
    while(i < N.size()-1) {
        if (N[i] <= N[i+1]) { // Ok
            i++;
        }
        else {
            N[i]--;
            for (uint32_t j = i+1; j < N.size(); ++j) {
                N[j] = '9';
            }
            i--;
        }
    }

    // Cleaning
    while(N[0] == '0') {
        N.erase(N.begin());
    }
    
    return N;
}

std::string parseAndExecute(std::istream& in) {
    std::string N;
    in >> N;

    return execute(N);
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
