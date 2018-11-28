#include <iostream>
#include <vector>
#include <map>
#include <string>
#include <cstdint>

std::vector<uint64_t> numbers;
std::vector<std::string> numbers_str;
std::vector<std::string> solution;
int n_testcases = 0;

void read_input() {
    std::cin >> n_testcases;
    numbers.resize(n_testcases);
    numbers_str.resize(n_testcases);
    for(int i=0; i < n_testcases; i++) {
        std::cin >> numbers[i];
        numbers_str[i] = std::to_string(numbers[i]);
    }
    solution.resize(n_testcases, "0");
}

void write_output() {
    for(int i=0; i < n_testcases; i++) {
        std::cout << "Case #" << i+1 << ": ";
        std::cout << solution[i] << std::endl;
    }
}

void solve() {
    for(int i=0; i < n_testcases; i++) {

        std::string str = numbers_str[i];
        uint64_t num = numbers[i];
        // std::cout << "Test " << i << " number " << num << " string " << str << std::endl;

        if (str.size() == 1)
        {
            solution[i] = str;
            continue;
        }

        for(int j = 0; j < str.size() - 1;) {
            if(str[j] <= str[j+1]) {
                j++;
                continue;
            }
            str[j] = (str[j] - 1);
            std::fill(str.begin()+j+1, str.end(), '9');
            // std::cout << "Modified string " << str  << " j " << j << std::endl;
            if(j > 0 && str[j-1] > str[j]) {
                j = 0;
                continue;
            } else {
                break;
            }
        }

        if(str[0] == '0') {
            int k = 0;
            while(k < str.size() && str[k] == '0') k++;
            if (k == str.size()) solution[i] = '0';
            else solution[i] = str.substr(k);
        } else {
            solution[i] = str;
        }
    }
}

int main() {
    read_input();
    solve();
    write_output();
}
