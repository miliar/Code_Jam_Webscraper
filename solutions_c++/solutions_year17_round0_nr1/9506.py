#include <iostream>
#include <vector>
#include <string>
using namespace std;

bool allplus(string& s) {
    for(int i=0; i<s.size(); ++i)
        if(s[i] == '-')
            return false;
    return true;
}

void flip(string& s, int lo, int hi) {
    for(int i=lo; i<hi; ++i) {
        if(s[i] == '+')
            s[i] = '-';
        else if(s[i] == '-')
            s[i] = '+';
    }
}

int main() {
    int T;
    cin >> T;
    for(int n=1; n<=T; ++n) {
        string s;
        int k;
        cin >> s >> k;
        //cout << "DEBUG: " << s << endl;
        //cout << "DEBUG: " << k << endl;
        int N = s.size();
        int ans = 0;
        for(int i=0; i<N-k+1; ++i) {
            //cout << "DEBUG: i = " << i << endl;
            if(s[i] == '+') continue;
            flip(s, i, i+k);
            //cout << "DEBUG: " << s << endl;
            ans++;
        }
        if(allplus(s))
            cout << "Case #" << n << ": " << ans << endl;
        else
            cout << "Case #" << n << ": IMPOSSIBLE"<< endl;
    }
}