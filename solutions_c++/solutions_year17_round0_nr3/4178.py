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

void getLevelNum(long long int num, long long int k) {
    
    int power = 0;
    while (pow(2, power) <= k) {
        power++;
    }
    power--;
    
    long long int high_count = 1, low_count = 0;
    
    for (int i = 0; i < power; i++) {
        if (num % 2 == 0) {
            low_count = 2 * low_count + high_count;
        } else {
            high_count = 2 * high_count + low_count;
        }
        num = num/2;
    }
    
    long long int diff_positon = k - pow(2, power) + 1;
    long long int num_taken;
    if (diff_positon > high_count) {
        num_taken = num - 1;
    } else {
        num_taken = num;
    }
    
    if (num_taken % 2 ==0) {
        cout<<num_taken/2<<" "<<(num_taken/2-1)<<endl;
    } else {
        cout<<num_taken/2<<" "<<num_taken/2<<endl;
    }
}

int main() {
    freopen("/Users/udit/Downloads/input.in", "r", stdin);
    freopen("/Users/udit/Downloads/output.out", "w", stdout);
    
    int test_cases;
    cin>>test_cases;
    
    for (int i=1; i<=test_cases; i++) {
        long long int num, k;
        cin>>num>>k;
        
        cout<<"Case #"<<i<<": ";
        getLevelNum(num, k);
    }
    
    return 0;
}
