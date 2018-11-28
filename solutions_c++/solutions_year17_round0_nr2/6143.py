#include<bits/stdc++.h>
using namespace std;

#define inst freopen("in.txt", "r", stdin)
#define oust freopen("out.txt", "w", stdout)

int main() {
    inst;oust;
    int t, cs = 1, n;
    string str;
    cin >> t;
    while(t--) {
        cin >> str;
        int len = str.size();
        int last_inc = 0, last_nd = 0;
        for(int i = 1; i < len; i++) {
            if(str[i] > str[i - 1]) last_inc = last_nd = i;
            else if(str[i] == str[i - 1]) last_nd = i;
            else break;
        }
        printf("Case #%d: ", cs++);
        if(last_nd == len - 1) cout << str << endl;
        else {
            if(str[last_nd] == '1') {
                for(int i = 1; i < len; i++) cout << '9';
                cout << endl;
            } else {
                str[last_inc]--;
                for(int i = last_inc + 1; i < len; i++) str[i] = '9';
                cout << str << endl;
            }
        }
    }
    return 0;
}
