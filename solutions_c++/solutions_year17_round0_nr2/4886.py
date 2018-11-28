#include <algorithm>
#include <iostream>
#include <vector>

using namespace std;

long last_tidy_number(long n);

int main() {
    int t;
    long n;
    cin >> t;
    for (int x = 1; x <= t; ++x) {
        cin >> n;
        cout << "Case #" << x << ": " << last_tidy_number(n) << endl;
    }
    return 0;
}

long last_tidy_number(long n) {
    // Number is already tidy if it has only one digit
    if (n < 10)
        return n;
    
    // Extract out the digits of the number
    vector<int> digits;
    while (n != 0) {
        digits.push_back(n % 10);
        n /= 10;
    }
            
    // Determine the digits of the last tidy number
    auto right = digits.begin();
    auto left = ++digits.begin();
    
    while (left != digits.end()) {  
        
        if (*left > *right) {
            *left -= 1;
            *right = 9;
            while (right != digits.begin()) {
                --right;
                if (*right == 9)
                    break;
                *right = 9;
            }
        }
        
        right = left;
        ++left;
    }
    
    // Recombine the modified digits into the tidy number    
    long order = 1;
    long tidy = 0;
    for (int i = 0; i < digits.size(); ++i) {
        tidy += digits[i] * order;
        order *= 10;
    }
    
    return tidy;
}

