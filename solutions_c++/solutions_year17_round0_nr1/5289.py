#include <iostream>
#include <vector>
#include <map>
#include <memory>

const std::string impossible = "IMPOSSIBLE";
std::vector<std::pair<int, std::string>> tc;
int n_testcases;
std::vector<bool> possible;
std::vector<int> solution;

void read_input() {
    std::cin >> n_testcases;
    tc.reserve(n_testcases);
    for(int i=0; i < n_testcases; i++) {
        std::pair<int, std::string> test;
        std::cin >> test.second >> test.first;
        tc.push_back(test);
    }
    possible.resize(n_testcases, false);
    solution.resize(n_testcases, 0);
}

void write_output() {
    for(int i=0; i < n_testcases; i++) {
        std::cout << "Case #" << i+1 << ": ";
        if(possible[i])std::cout << solution[i] << std::endl;
        else std::cout << impossible << std::endl;
    }
}

void solve() {
    for(int i=0; i < n_testcases; i++) {
        int K = tc[i].first;
        std::string& S = tc[i].second;
        int flips = 0;
        // std::cout << "Test " << i << " K " << K << " S " << S << std::endl;
        for(int j = 0; j < S.size();) {
            if(S[j] == '-') {
                int offset = K;
                ++flips;
                if((S.size()-1)-j < K) {
                    j = S.size() - K;
                    for(int a=0; a < K; a++) {
                        S[j] = (S[j] == '-') ? '+' : '-';
                        j++;
                    }
                    break;
                }
                for(int k=j; k < j+K; k++) {
                    if(S[k] == '-') {
                        S[k] = '+';
                    } else {
                        S[k] = '-';
                        if(offset == K) offset = k-j;
                    }
                }
                j += offset;
                // std::cout << "Flip S " << S << " j " << j << std::endl;
            } else {
                j++;
            }
        }
        if (S.find('-') == std::string::npos) {
            possible[i] = true;
            solution[i] = flips;
        }
    }
}

int main() {
    read_input();
    solve();
    write_output();
}
