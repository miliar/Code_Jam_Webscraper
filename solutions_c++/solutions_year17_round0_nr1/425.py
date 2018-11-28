#include <iostream>
#include <string>

using namespace std;

int T, k;
string s;
const int failure = -2147483648;

int count(string s) {
    int p = s.find('-');
    //cout <<"found at " <<p <<endl;
    if (p == -1) return 0;
    if (p + k > s.length()) return failure;
    for (int i = p + 1; i < p + k; i++)
        s[i] = (s[i] == '+'? '-' : '+');
    //cout <<s <<endl;
    return 1 + count(s.substr(p + 1));
}

int main() {
    cin >>T;
    for (int i = 0; i < T; i++) {
        cin >>s >>k;
        cout <<"Case #" <<i + 1 <<": ";
        //cout <<s <<' ' <<k <<endl;
        int c = count(s);
        if (c < 0)
            cout <<"IMPOSSIBLE" <<endl;
        else cout <<c <<endl;
    }
    return 0;
}
