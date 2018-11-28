#include <cmath>
#include <cstdio>
#include <vector>
#include <iostream>
#include <string>
#include <algorithm>
using namespace std;


int main() {
    int tcase;
    cin >> tcase;
    for (int t = 0; t < tcase; t++) {
        string s;
        cin >> s;
        int n = s.length();
        int num[50];
        for (int i = 0; i < n; i++) {
            num[i] = s[i] - '0';
        }
        for (int i = n-1; i >= 1; i--) {
            if (num[i] < num[i-1]) {
                for (int j = i; j < n; j++) {
                    num[j] = 9;
                }
                num[i-1]--;
            }
        }
        cout << "Case #" << t+1 << ": ";
        bool leadingZero = true;
        for (int i = 0; i < n; i++) {
            if (leadingZero && num[i] == 0) {
                continue;
            } else {
                leadingZero = false;
                cout << num[i];
            }
        }
        cout << endl;
    }
    return 0;
}