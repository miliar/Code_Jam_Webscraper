#include <iostream>
#include <string>
#include <cstdio>
using namespace std;

int main() {
    int T;
    cin >> T;
    for (int II = 1; II <= T; II++) {
        string s;
        cin >> s;
        int marking = s.size();
        for (int i = s.size() - 1; i > 0; i--) {
            if (s[i] < s[i-1]) {
                marking = i;
                s[i-1]--;
            }
        }
        for (int i = marking; i < s.size(); i++) s[i] = '9';
        const char *ptr = s.c_str();
        while (*ptr == '0') ptr++;
        printf("Case #%d: %s\n", II, ptr);
    }
    return 0;
}
