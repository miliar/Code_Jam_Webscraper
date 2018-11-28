#include <iostream>  // includes cin to read from stdin and cout to write to stdout
#include <string>

using namespace std;  // since cin and cout are both in namespace std, this saves some text

bool isTidy(long n) {
    int prevDigit = 10;
    while(n != 0) {
        int digit = n % 10;
        // putchar('0' + digit);
        n /= 10;

        if (digit > prevDigit) {
            return false;
        }
        prevDigit = digit;
    }
    return true;
}

int main() {
    int t;
    long num;
    cin >> t;  // read t. cin knows that t is an int, so it reads it as such.
    for (int i = 1; i <= t; ++i) {
        cin >> num;  // read n and then m.
        long n = num;
        while(!isTidy(n)) {
            n--;
        }
        cout << "Case #" << i << ": " << n << endl;
    }
}
