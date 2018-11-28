#include <cstdio>
#include <iostream>
#include <string>

using namespace std;

typedef long long int64;



string calc(int64 N) {        
    string s = to_string(N);
    string r;
    int L = s.size();
    int pos = -1;
    for (int i = 0; i + 1 < L; i++) {
        if (s[i + 1] < s[i]) {            
            pos = i;
            break;
        }
    }
    if (pos == -1)
        return s;
    while (pos > 0 && s[pos] == s[pos - 1]) pos--;
    if (s[pos] == '1') {
        for (int i = 0; i < L - 1; i++) {
            r += '9';
        }
    }
    else {
        for (int i = 0; i < pos; i++) {
            r += s[i];
        }
        r += s[pos] - 1;
        for (int i = pos + 1; i < L; i++) {
            r += '9';
        }
    }
    return r;
}

int main() {    
    int T;
    scanf("%d", &T);
    for (int test = 0; test < T; test++) {
        int64 N;
        scanf("%lld", &N);
        printf("Case #%d: %s\n", test + 1, calc(N).c_str());
    }    
    return 0;
};
