#include <iostream>
#include <map>
#include <vector>
#include <algorithm>
#include <string>

// c library headers
#include <cstdint>
#include <cstdio>
#include <ctype.h>
#include <cmath>

using namespace std;

bool recurse_check(uint64_t n, int dig){
    if(n<10 && dig >= n) return 1;
    return (dig >= n%10) & recurse_check(n/10, n%10);
}

int main(){
    int n, i;
    uint64_t number, j;
    cin >> n;
    vector<uint64_t> num;
    for(i=0; i<n; ++i){
        cin >> number;
        num.push_back(number);
    }
    i = 0;
    while(i < n){
        number = 0;
        for(j = num[i]; j>0; --j)
            if(recurse_check(j/10, j%10)) break;
        printf("Case #%d: %llu\n", i+1, j);
        ++i;
    }
    return 0;
}
