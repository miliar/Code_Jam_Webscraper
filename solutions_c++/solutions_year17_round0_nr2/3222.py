#include <cstdlib>
#include <iostream>
#include <vector>

using namespace std;

int split_to_digits(int *digits, int size, unsigned long long N) {
    int i = size;
    while(N > 0) {
        digits[--i] = (N % 10);
        N /= 10;
    }
    
    return i;
}

unsigned long long solve(unsigned long long N) {
    int MAX_DIGITS = 19;
    int digits[MAX_DIGITS];
    for(long i = 0; i < MAX_DIGITS; ++i) {
        digits[i] = -1;
    }
    
    if(N < 10) {
        return N;
    }
    
    int start = split_to_digits(digits, MAX_DIGITS, N);
    int i = start;
    while(i < MAX_DIGITS - 1) {
        if(digits[i] > digits[i + 1]) {
            break;
        }
        ++i;
    }
    
    if(i < MAX_DIGITS - 1) {
        while(digits[i] > digits[i + 1]) {
            --digits[i];
            --i;
        }
        
        i += 2;
        while(i < MAX_DIGITS) {
            digits[i] = 9;
            ++i;
        }
        
        N = digits[start];
        for(i = start + 1; i < MAX_DIGITS; ++i) {
            N *= 10;
            N += digits[i];
        }
        
        return N;
    }
    else {
        // N is tidy
        return N;
    }
    
    return N;
}

int main(int argc, char** argv) {
    int T;
    unsigned long long N;
    
    cin >> T;
    for(int i = 1; i <= T; ++i) {
        cin >> N;
        cout << "Case #" << i << ": " << solve(N) << "\n";
    }
    
    return 0;
}
