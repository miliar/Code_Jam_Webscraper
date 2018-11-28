#include <iostream>
#include <cstdio>
#include <algorithm> 
#include <cstring>

using namespace std;


int main() {
    freopen("input_b_1.txt", "r", stdin);
    freopen("output_b_1.txt", "w", stdout);
    int testCases;
    cin >> testCases;
    for (int testCase = 1; testCase <= testCases; testCase++) {
        cout << "Case #" << testCase << ": ";
                
        string s;
        cin >> s;        
        long long num = 0;
        for (int i = 0; i < s.size(); i++) {            
            if (i > 0) {
                num = num * 10 + 9;
            }
        }

        int prev = 0;
        for (int i = 0; i < s.size(); i++) {
            if (s[i] - '0' >= prev) {
                long long temp = 0;
                for (int j = 0; j < i; j++) {
                    temp = temp * 10 + s[j] - '0';
                }
                if (i + 1 == s.size()) {
                    temp = temp * 10 + s[i] - '0';
                    num = max(num, temp);
                } else {
                    if (prev < s[i] - '0') {
                        temp = temp * 10 + s[i] - '0' - 1;
                        for (int j = i + 1; j < s.size(); j++) {
                            temp = temp * 10 + 9;
                        }
                        num = max(num, temp);
                    }
                }
                prev = s[i] - '0';
            } else {                
                break;
            }
        }
        cout << num << endl;
    } 
    return 0;
}