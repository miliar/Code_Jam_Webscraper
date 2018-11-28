#include<iostream>
#include<string>
using namespace std;


string s;
int len;

void read() {
    cin >> s >> len;
}


void work(int cases) {
    int ans = 0;
    for (int i = 0; i + len <= s.size(); ++i) {
        if (s[i] == '-') {
            for (int j = i; j < i + len; ++j) {
                s[j] = s[j] == '-' ? '+' : '-';
            }
            ++ans;
        }
    }
    
    cout << "Case #" << cases << ": ";
    
    if (s.find('-') == string::npos) {
        cout << ans << endl;
    } else {
        cout << "IMPOSSIBLE" << endl;
    }
}


int main() {
    int cases;
    cin >> cases;
    
    for (int i = 0; i < cases; ++i) {
        read();
        work(i + 1);
    }
    return 0;
}
