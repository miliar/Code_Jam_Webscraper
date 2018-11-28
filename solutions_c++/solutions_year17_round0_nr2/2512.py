#include<iostream>
#include<string>
using namespace std;

string compute(string &s) {
    int n, i, digit;
    n = s.length();
    if (n == 1) return s;
        
    i = 1;
    while (s[i] >= s[i-1] && i < n) i++;
    if (i == n) return s;

    if (s[i] == '0' && s[i-1] == '1') {
        string ans;
        for (int j = 0; j < n-1; j++) ans += '9';
        return ans;
    }
    //cout << i << endl;
    i--;
    digit = s[i];
    
    while (i > 0 && s[i-1] == digit) i--;
    //cout << i << endl;
    string ans;
    for (int j = 0; j <= i-1; j++) ans += s[j];
    
    ans += (s[i] - 1);
    if (i == 0) {
        for (int j = 1; j < n; j++) ans += '9';
        return ans;
    }
    
    for (int j = 0; j < n-i-1; j++) ans += '9';
    return ans;
    
}

int main() {

    int t, i, n;
    string s;
    
    cin >> t;
    for (int k = 0; k < t; k++) {
        cin >> s;
        
        cout << "Case #" << k + 1 << ": ";
        cout << compute(s) << endl;
    }
    
    return 0;
}            
            
        
