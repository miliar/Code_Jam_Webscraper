#include <iostream>
#include <vector>
#include <string>
#include <cmath>

using namespace std;

long power(int base, int exp) {
    return pow(base, exp);
}

int highestPower(long n) {
    return (int) log10(n);
}

int tidy(long n) {
    int lastDigit = n / power(10, highestPower(n)) % 10;
    for (int i = highestPower(n) - 1; i >= 0; i--) {
        if (n / power(10, i) % 10 >= lastDigit) {
            lastDigit = n / power(10, i) % 10;
        } else {
            return i;
        }
    }
    return -1;
}

int main(int argc, const char * argv[]) {
    freopen("/Users/danielsong/Downloads/B-large.in", "r", stdin);
    freopen("/Users/danielsong/Downloads/B-large.out", "w", stdout);
    
    int T;
    cin >> T;
    for (int t = 1; t <= T; t++) {
        long input;
        cin >> input;
        long temp = input;
        while (tidy(input) >= 0) {
            int isTidy = tidy(input);
            input += (9 - ((input % power(10, isTidy + 1)) / power(10, isTidy))) * power(10, isTidy);
            if (input > temp) {
                input -= (long) power(10, isTidy + 1);
            }
        }
        cout << "Case #" << t << ": " << input << endl;
    }
    
    return 0;
}
