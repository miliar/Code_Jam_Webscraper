#include <iostream>

bool isTidy(unsigned long n) {
    std::string number = std::to_string(n);

    char lastNumber = '0';
    for(char thisNumber : number) {
        if(thisNumber < lastNumber) {
            return false;
        }
        lastNumber = thisNumber;
    }
    return true;
}

int main() {
    unsigned int numTestsCases;
    std::cin >> numTestsCases;

    for(unsigned int i = 1; i <= numTestsCases; i++) {
        unsigned long n;
        std::cin >> n;

        unsigned long maxN = 1;
        for(unsigned long j = 1; j <= n; j++) {
            if(isTidy(j)) {
                maxN = j;
            }
        }

        std::cout << "Case #" << i << ": " << maxN << std::endl;
    }
}