#include <bits/stdc++.h>
#define MAX_S 100
using namespace std;

bool sorted(string s) {
    for (int i = 0; i < s.size() - 1; i++) {
        if (s[i] > s[i+1]) {
            return false;
        }
    }
    return true;
}

void print(int q, string s) {
    printf("Case #%d: ", q);
    int i = 0;
    while(s[i] == '0') {i++;}
    for (i = i ;i < s.size(); ++i) {
        cout << s[i];
    }
    cout << endl;
}

int main() {
    int t, i;
    int q = 1;
    string s;
    cin >> t;

    while(t--) {
        cin >> s;

        i = s.size() - 1;
        while (!sorted(s) && i >= 0) {
            s[i] = '9';
            s[i-1] = s[i-1] - 1;
            i--;
        }
        print(q++, s);
    }

    return 0;
}
