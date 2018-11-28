#include <iostream>
#include <algorithm>
#include <cmath>
#include <cstdio>
#include <cstring>
#include <fstream>

using namespace std;

fstream input("input.in");
ofstream output("output.out");

int isTidy(unsigned long long  n) {
    string number = to_string(n);
    for (int i = 1; i < number.length(); i++) {
        if (number[i] < number[i-1]) {
            return (int) number.length() - i - 1;
        }
    }
    return -1;
}

void solve(int index) {
    unsigned long long  number;
    input >> number;
    int indexValue = isTidy(number);
    while (indexValue != -1) {
        unsigned long long power = pow(10, indexValue);
        unsigned long long rest = power - 1;
        number /= power;
        number *= power;
        number -= power;
        number += rest;
        indexValue = isTidy(number);
    }
    
    output << "Case #" << index << ": ";
    output << number << "\n";
}

int main()
{
    int T;
    input >> T;
    for (int i = 1; i <= T; i++) {
        solve(i);
    }
    return 0;
}
