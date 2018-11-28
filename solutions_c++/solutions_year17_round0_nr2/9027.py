#include <string>
#include <sstream>
#include <vector>
#include <iterator>
#include <set>
#include <iostream>
#include <functional>
#include <algorithm>

// trim from end
static inline std::string &rtrim(std::string &s) {
    s.erase(std::find_if(s.rbegin(), s.rend(),
            std::not1(std::ptr_fun<int, int>(::isspace))).base(), s.end());
    return s;
}

void printNNines(int n){
    for (int i = 0; i < n; i ++){
        std::cout << '9';
    }
}

int main(){ 
    std::ios_base::sync_with_stdio(false);
    std::cin.tie(nullptr);
    std::string temp;
    std::getline(std::cin, temp);
    const int T = std::stoi(temp);

    for (int i = 1; i <= T; i++){ //Iterate through test cases
        std::cout << "Case #" << i << ": ";
        
        std::getline(std::cin, temp);
        temp = rtrim(temp);
        int len = temp.length();

        int cur = temp[len-1] - '0';
        int last = cur;
        int j = len - 2;
        bool increased = false;
        for(;j >= 0; j--){
            int cur = temp[j] - '0';
            if (cur < last && increased){
                break;
            } else if (cur > last){
                increased = true;
            }
            last = cur;
        }

        if (j >= 0){
            std::cout << temp.substr(0,j+1);
            std::cout << temp[j+1] - '1';
            printNNines(len-j-2);
            std::cout <<"\n";
        } else {
            if (!increased){
                std::cout << temp << "\n";
            } else {
                if (temp[0] != '1'){
                    std::cout << temp[0] - '1';
                }
                printNNines(len-1);
                std::cout << "\n";
            }
        }
    } 
}
