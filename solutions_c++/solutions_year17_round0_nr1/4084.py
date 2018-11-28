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

int getMinFlips(string str, int k) {

    int minFilps = 0;
    for (int i=0; i<str.length(); i++) {
        if (str[i] == '-') {
            for (int j=0; j<k; j++) {
                if (i+j >= str.length()) {
                    return -1;
                }
                str[i+j] = (str[i+j] == '+') ? '-' : '+';
            }
            minFilps++;
        }
    }
    
    return minFilps;
}

int main() {
    freopen("/Users/udit/Downloads/A-small-attempt0.in", "r", stdin);
    freopen("/Users/udit/Downloads/output.out", "w", stdout);
    
    int test_cases;
    cin>>test_cases;
    
    for (int i=1; i<=test_cases; i++) {
        string str;
        int k;
        cin>>str>>k;
        cout<<"Case #"<<i<<": ";
        int minFlips = getMinFlips(str, k);
        if (minFlips == -1) {
            cout<<"IMPOSSIBLE"<<endl;
        } else {
            cout<<minFlips<<endl;
        }
        
    }
    
    return 0;
}
