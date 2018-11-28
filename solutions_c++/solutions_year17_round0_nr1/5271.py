#include <iostream>
#include <vector>
using namespace std;

void flip(string& s, int pos, int k) {
    for(int i = pos; i < pos+k; i++) {
        if(s[i] == '+')
            s[i] = '-';
        else
            s[i] = '+';
    }
}

int main() {
    int t, k;
    string s;
    cin >> t;
    for(int z = 1; z <= t; z++) {
        cin >> s >> k;
        int p = 0, n = s.length();
        int count = 0;
        for(int i = 0; i <= n-k; i++) {
            if(s[i] == '-') {
                flip(s, i, k);
                ++count;
            }            
        }
        bool flag = true;
        for(int i = 0; i < n; i++) {
            if(s[i] == '-') {
                flag = false;
                break;
            }
        }
        cout << "Case #" << z << ": ";
        if(flag)
            cout << count << endl;
        else
            cout << "IMPOSSIBLE" << endl;
    }
}
