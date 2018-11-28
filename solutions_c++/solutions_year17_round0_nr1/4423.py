#include <bits/stdc++.h>

using namespace std;

int calc(string s, int t) {
    int res = 0;
    for(int i=0;i<=s.size()-t;i++) {
        if(s[i] == '-') {
            res++;
            for(int j=0;j<t;j++) {
                if(s[i+j] == '-') {
                    s[i+j] = '+';
                } else {
                    s[i+j] = '-';
                }
            }
        }
    }
    if(count(s.begin(),s.end(),'-') == 0) {
        return res;
    }
    return -1;
}

int main() {
    int casos;
    cin >> casos;
    for(int i=1;i<=casos;i++) {
        string s;
        int t;
        cin >> s >> t;
        cout << "Case #" << i <<": ";
        t = calc(s,t);
        if(t == -1) cout <<"IMPOSSIBLE\n";
        else cout << t << endl;
    }
}