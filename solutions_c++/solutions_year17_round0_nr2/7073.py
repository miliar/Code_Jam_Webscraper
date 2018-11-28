#include <iostream>
#include <cmath>

int lastTidy (int n);


int main() {


    int t, n;
    std::cin >> t;

    for (int i = 1; i <= t; ++i) {
        std::cin >> n;
        std::cout << "Case #" << i << ": " << lastTidy(n) << std::endl;
    }

    return 0;
}


int lastTidy (int n){
    int prev = 0;
    int cur = 0;
    int prevCounter = std::pow(10, std::floor(std::log10(n) + 1));
    int counter = prevCounter / 10;
    while (counter >= 1) {
        cur = (n % prevCounter) / counter;
        if (cur < prev) {
            while ((n % (prevCounter * 10)) / prevCounter ==
                    (n % (prevCounter * 100)) / (prevCounter * 10)) {
                prevCounter *= 10;
            }
            return (n / prevCounter) * prevCounter - 1;
        }
        prev = cur;
        prevCounter = counter;
        counter /= 10;
    }
    return n;
}