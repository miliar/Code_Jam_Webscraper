#include <iostream>
#include <string>
#include <algorithm>
#include <cstdio>
#include <vector>
#include <stack>
#include <unordered_map>
#include <queue>
#include <cmath>
#include <unistd.h>

using namespace::std;

int max = 18;

bool isTidy(long long int number) {
    int last_max_seen = number % 10;
    while (number > 0) {
        int lastDigit = number % 10;
        if (lastDigit > last_max_seen) {
            return false;
        }
        last_max_seen = lastDigit;
        number = number/10;
    }
    return true;
}

long long int getLastTidyNumber(long long int number) {
    long long int temp_number = number;
    for (int i=0; i<=18; i++) {
        if (isTidy(temp_number)) {
            return temp_number;
        } else {
            long long int p = pow(10, i);
            long long int num_to_substract = i > 0 ? (number % p) : 0;
            temp_number = number - num_to_substract - 1;
        }
    }
    return temp_number;
}

int main() {
    freopen("/Users/udit/Downloads/input.in", "r", stdin);
    freopen("/Users/udit/Downloads/output.out", "w", stdout);
    
    int test_cases;
    cin>>test_cases;
    
    for (int i=1; i<=test_cases; i++) {
        long long int number;
        cin>>number;
        cout<<"Case #"<<i<<": "<<getLastTidyNumber(number)<<endl;
    }
    
    return 0;
}
