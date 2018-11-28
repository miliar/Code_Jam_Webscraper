#include<iostream>
#include<stdio.h>
#include<string>
using namespace std;

#define N 1001

int main() {

    string s;
    int t, k, a[N], i, n, flips;
    bool isPossible;
    cin >> t;

    for (int x = 0; x < t; x++) {
        
        i = 0;
        flips = 0;
        isPossible = true;
        
        cin >> s;
        n = s.length();
        cin >> k;
        
        for (i = 0; i <= n-k; i++) {
            if (s[i] == '+') continue;
            flips++;
            for (int j = i+1; j < i+k; j++) {
                s[j] = (s[j] == '+' ? '-' : '+');
            }
        }
        
        
        for (i = n-k+1; i < n; i++) {
            if (s[i] == '-') {
                isPossible = false;
                break;
            }
        }
        
        cout << "Case #" << x + 1 << ": ";
        if (!isPossible) cout << "IMPOSSIBLE" << endl;
        else cout << flips << endl;
    }
    
    return 0;
}                  



