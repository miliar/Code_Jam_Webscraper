#include <iostream>
#include <cstring>

using namespace std;

void fill9s(char* number, int i, int n) {
    for(;i < n; ++i)
        number[i] = '9';
}


void solve(char* number) {
    int n = strlen(number);
    for(int i=n-1; i > 0; --i) {
        if(number[i-1] > number[i]) {
            --number[i-1];
            fill9s(number, i, n);
        }
    }
}

int main(int argc, char** argv) {
    int t;
    char number[19];
    
    cin >> t;
    
    for(int i=0;i<t;++i) {
        cin >> number;
        solve(number);
        char* begin = number;
        while(*begin == '0')
            ++begin;
        cout << "Case #" << (i+1) << ": " << begin << endl;
    }
    
    return 0;
}

