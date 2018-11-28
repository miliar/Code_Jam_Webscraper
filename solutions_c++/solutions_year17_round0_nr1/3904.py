#include <iostream>
#include <cstring>
using namespace std;

void flip(char& c) {
    if(c=='+')
        c = '-';
    else
        c = '+';
}

int solve(char* string, int k) {
    int n = strlen(string);
    int flips = 0;
    
    for(int i=0;i<n-k+1; ++i) {
        if(string[i] != '+') { // flip
            ++flips;
            for(int j=0;j<k;++j) {
                flip(string[i+j]);
            }
        }
    }
    
    // check the last k-1
    for(int i=n-k+1; i<n; ++i)
        if(string[i] != '+')
            return -1;
    return flips;
}

int main() {
    int t, k;
    char string[1001];
    
    cin >> t;
    for(int i=0;i<t;++i) {
        cin >> string >> k;
        
        int res = solve(string, k);
        cout << "Case #" << (i+1) << ": ";
        if(res == -1)
            cout << "IMPOSSIBLE";
        else
            cout << res;
        cout << endl;
    }
}
