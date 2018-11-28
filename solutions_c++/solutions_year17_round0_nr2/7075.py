#include <bits/stdc++.h>
//#include <unordered_map>
#define _USE_MATH_DEFINES//M_PI
using namespace std;
typedef unsigned long long ll;

void tidy(string &k) {
    for(int i = 1; i < k.size(); i++) {
        if(k[i] < k[i-1]) {
            k[i-1]--;
            for(int j = i; j < k.size(); j++) {
                k[j] = '9';
            }
            return;
        }
    }
}

int main() {
    int n, counter = 1;
    cin >> n;
    while(n--) {
        string k;
        cin >> k;
        for(int i = 0; i < 50; i++) {
            tidy(k);
        }
        while(k[0] == '0') {
            k = k.substr(1);
        }
        cout << "Case #" << counter++ << ": " << k << endl;
    }
    return 0;
}
