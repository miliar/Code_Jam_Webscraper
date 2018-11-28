#include <iostream>
#include <bitset>
#include <sstream>
#include <memory>
#include <limits>
#include <list>
#include <stack>
#include <set>
#include <map>
#include <unordered_map>
#include <unordered_set>
#include <string>
#include <vector>
#include <algorithm>
#include <stdlib.h>
#include <stdio.h>
#include <math.h>

using namespace std;

long long solve() {
    long long n;
    
    cin >> n;
    
    vector<long long> digits;
    while (n) {
        digits.push_back(n%10);
        n/=10;
    }
    
    for (int i = 0; i < (int)digits.size()-1; ++i) {
        if (digits[i] < digits[i+1]) {
            digits[i+1]--;
            for (int j = 0; j <= i; ++j) {
                digits[j] = 9;
            }
        }
    }

    while (digits.back() <= 0) {
        digits.pop_back();
    }

    long long num = 0;
    for (int i = digits.size()-1; i >= 0; --i) {
        num*=10;
        num += digits[i];
    }
    
    return num;    
}

int main() {
    std::cout.precision(15);
    std::ios_base::sync_with_stdio(false);
    
    int t;
    cin >> t;
    for (int i = 1; i <=t ; ++i) {
        cout << "Case #" << i << ": " << solve() << endl;
    }
    
    
    return 0;
}