#include <iostream>
using namespace std;

bool isTidy(string s) {
    for(int i = 0 ; i < s.length() - 1 ; i++) {
        if( s[i] > s[i-1] ) return false;
    }

    return true;
}

string makeTidy(string s) {
    if( s.length() == 1 ) return s;

    string sub = makeTidy(s.substr(1));
    string ret = "";

    if( sub[0] < s[0] ) {
        ret += (char)((int)s[0]-1);

        for(int i = 0 ; i < sub.length() ; i++) ret += '9';

        return ret;
    }

    return s[0] + sub;
}

int main() {
    int t;

    freopen("B-large.in", "r", stdin);
    freopen("large.out", "w", stdout);

    cin >> t;

    for(int ts = 1 ; ts <= t ; ts++) {
        string k;
        cin >> k;

        string answer = makeTidy(k);

        //int answer = 0;

        while( answer[0] == '0' ) {
            answer = answer.substr(1);
        }

        cout << "Case #" << ts << ": " << answer << endl;
    }
}