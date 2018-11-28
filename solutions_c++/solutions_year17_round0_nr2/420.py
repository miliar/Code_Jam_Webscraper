#include <iostream>
#include <string>

using namespace std;

int T;
string N;

bool adjust(string &s) {
    bool mod = false;
    for (int i = s.length() - 1; i > 0; i--) {
        if (s[i] < s[i - 1]) {
            s[i] = '9';
            s[i - 1]--;
            mod = true;
        } else return mod;
    }
    return mod;
}

long long trail(string &s) {
    long long rst = 0;
    for (int i = 0; i < s.length(); i++)
        rst = rst * 10 + s[i] - '0';
    return rst;
}

int main() {
    cin >>T;
    for (int i = 1; i <= T; i++) {
        cin >>N;
        string s;
        for (int j = 0; j < N.length(); j++) {
            s += N[j];
            if (adjust(s)) break;
        }
        //cout <<s <<endl;
        while (s.length() != N.length())
            s += '9';
        cout <<"Case #" <<i <<": " <<trail(s) <<endl;
    }
    return 0;
}
