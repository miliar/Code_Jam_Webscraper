#include <bits/stdc++.h>
using namespace std;

int main()
{
    int T;
    cin >> T;
    for(int t = 1; t <= T; ++t) {
        cout << "Case #" << t << ": ";
        string str;
        cin >> str;
        int len = str.size();
        int up = 0, down = -1;
        for(int i = 0; i < len-1; ++i) {
            if(str[i] < str[i+1]) up = i+1;
            if(str[i] > str[i+1]) {
                down = i;
                break;
            }
        }
        if(down == -1) {
            cout << str << endl;
            continue;
        }
        bool touchUp = false;
        for(int i = 0; i < len; ++i) {
            if(touchUp) cout << "9";
            else if(i == up) {
                char c = str[i]-1;
                if(c != '0') cout << c;
                touchUp = true;
            }
            else cout << str[i];
        }
        cout << endl;
    }
    return 0;
}
