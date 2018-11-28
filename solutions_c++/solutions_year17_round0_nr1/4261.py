#include <iostream>
using namespace std;

void handleCase() {
    std::string pancakes;
    int size;
    std::cin >> pancakes >> size;
    
    
    int count = 0;
    for(int i = 0;i < pancakes.size(); i++) {
        if(pancakes[i] == '-') {
            for(int j = i;j < i+size; j++) {
                if(j >= pancakes.size()) {
                    std::cout << "IMPOSSIBLE\n";
                    return;
                }
                
                if(pancakes[j] == '-') pancakes[j] = '+';
                else pancakes[j] = '-';
            }
            count++;
        }
    }
    
    std::cout << count << "\n";
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
