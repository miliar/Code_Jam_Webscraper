#include<iostream>
#include<string>


using namespace std;


int main(void) {
    int T; cin >> T;
    int ca = 0;
    while(T--) {
        string s; cin >> s;
        int k; cin >> k;
        int flips = 0;
        for(int i=0; i<=s.size()-k; i++) {
            if(s[i] == '-') {
                for(int j=0; j<k; j++) {
                    if(s[i+j]=='-') {
                        s[i+j] = '+';
                    } else {
                        s[i+j] = '-';
                    }
                }
                flips++;
            }
        }
        bool ok = true;
        for(char c: s) {
            if(c=='-') {
                ok = false;
                break;
            }
        }
        cout << "Case #" << ++ca << ": ";
        if(ok) cout << flips << endl;
        else cout << "IMPOSSIBLE" << endl;
    }
    return 0;
}