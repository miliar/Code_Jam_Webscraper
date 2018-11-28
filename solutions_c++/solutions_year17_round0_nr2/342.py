#include <iostream>
#include <string>
using namespace std;
string ans (string s){
    string r = s;
    if (r.size() == 1) return r;
    bool flag = false;
    int i;
    for (i = 0 ; i < s.size()-1; i++) {
        if ( flag = (s[i]>s[i+1]) ) break;
    }
    if (!flag) return r;
    while (i>0) {
        if (s[i-1] != s[i]) break;
        i--;
    }
    if (i == 0 && s[0] == '1') {
        return string(s.size()-1,'9');
    } 
    s[i]--;
    i++;
    while (i<s.size()) {s[i] = '9'; i++;}
    return s;
}
int main() {
    int nn;
    cin >> nn;
    for (int i = 1 ; i <= nn; i++) {
        printf("Case #%d: ",i);
        string s;
        int k;
        cin >> s;
        cout << ans(s) << endl;
    }
}
