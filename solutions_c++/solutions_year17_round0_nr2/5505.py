#include <iostream>
#include <cstdio>

using namespace std;

int main () {

    //freopen("B-large.in", "r", stdin);
    //freopen("b.out", "w", stdout);

    int T;

    cin >> T;

    for(int t = 1; t <= T; t++) {

        string s;

        cin >> s;

        long long num;
        sscanf(s.c_str(), "%lld", &num);

        if(num == 10) {
            cout << "Case #" << t << ": 9" << endl;
            continue;
        } else if(num < 10) {
            cout << "Case #" << t << ": " << num << endl;
            continue;
        }

        int len = s.length();

        for(int i = len - 2; i >= 0; i--) {
            if(s[i] > s[i + 1]) {
                s[i + 1] = '9';
                if(s[i] == '0')
                    s[i] = '9';
                else
                    s[i]--;
            }
        }

        int ptr = 0;
        while(s[ptr] == '0')
            ptr++;

        if(ptr > 0)
            for(int i = ptr; i < len; i++)
                s[i] = '9';

        for(int i = 0; i < len - 1; i++)
            if(s[i] > s[i + 1])
                s[i + 1] = '9';

        sscanf(s.c_str(), "%lld", &num);


        cout << "Case #" << t << ": " << num << endl;

    }

    return 0;
}