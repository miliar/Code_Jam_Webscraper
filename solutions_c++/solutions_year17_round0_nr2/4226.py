#include <iostream>
using namespace std;


void handleCase() {
    std::string number;
    std::cin >> number;
    
    // find last tidy digit
    int i;
    for(i = 1;i < number.size(); i++) {
        if(number[i-1] > number[i]) break;
    }
    if(i == number.size()) {
        std::cout << number << "\n";
        return;
    } else {
        i--;
    }
    
    
    number[i] = number[i] - 1;
    for(int j = i+1;j < number.size(); j++) number[j] = '9';
    
    for(int j = i-1; j >= 0; j--) {
        if(number[j] > number[j+1]) {
            number[j]--;
            number[j+1] = '9';
        } else {
            break;
        }
    }
    
    if(number[0] == '0') {
        // find last set of zeros if starts with zero
        i = 0;
        for(;i < number.size(); i++) {
            if(number[i] != '0') break;
        }
        std::cout << number.substr(i) << "\n";
    } else {
        std::cout << number << "\n";
    }
}

int main() {
    int N;
    std::cin >> N;
    
    for(int i = 1;i <= N; i++) {
        std::cout << "Case #" << i << ": ";
        handleCase();
    }
    return 0;
}