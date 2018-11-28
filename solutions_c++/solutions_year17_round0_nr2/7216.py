#include <iostream>
#include <string>

using namespace std;

int main() {
    int T;
    cin >> T;
    for (int t = 1; t <= T; ++t) {
        string s;
        cin >> s;
        int len = s.size();
        bool isfree = false;
        for (int i = 0; i < len; ++i)
            if (isfree) 
                s[i] = '9';
            else {
                if (i != len-1 && s[i] > s[i+1]) {
                    s[i] = s[i] - 1;
                    isfree = true;
                    if (i && s[i] < s[i-1]) {
                        for (int j = i; j >= 1; --j)
                            s[j] = '9';
                        s[0] = s[0] - 1;
                    }
                } 
            }
        int i = 0;
        while (s[i] == '0' && i != len-1)
            ++i;
        cout << "Case #" << t << ": ";
        while (i < len)
            cout << s[i++];
        cout << endl;
    }
    return 0;
}


