#include<iostream>
#include<string>

using namespace std;

int main() {
    int T;
    cin >> T;
    for(int t=1; t<=T; t++) {
        string s; cin >>s;
        int k; cin >> k;
        int r=0;
        for(int i = 0; i<s.size(); i++) {
//            cout << i << ": " << s << "\n";
            if (s[i]=='-') {
                if (i+k > s.size()) {
                    r=-1;
                    break;
                }
                r++;
                for(int j = i; j < i+k; j++) {
                    if(s[j]=='-') {
                        s[j] = '+';
                    }
                    else {
                        s[j] = '-';
                    }
                }
            }
        }
        cout << "Case #" << t << ": ";
        if (r==-1) {
            cout << "IMPOSSIBLE";
        }
        else {
            cout << r;
        }
        cout << "\n";
    }
}
