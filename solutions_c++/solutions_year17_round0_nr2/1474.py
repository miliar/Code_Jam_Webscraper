#include <cstdio>
#include <algorithm>
#include <string>
#include <iostream>
using namespace std;
int T;
string str;
int main() {
    freopen("B-large.in", "r", stdin);
    freopen("output.txt", "w", stdout);
    cin >> T;
    for(int test = 1; test <= T; ++test) {
        cin >> str;
        int idx = -1, beg;
        for(int i = 1; i < str.size(); ++i) {
            if(str[i - 1] > str[i]) {
                idx = i - 1;
                break;
            }
        }

        if(idx == -1) {
            printf("Case #%d: ", test);
            cout << str << "\n";
            continue;
        }

        for(beg = idx; beg >= 0; --beg) {
            if(str[beg] != str[idx]) {
                beg++;
                break;
            }
        }
        if(beg == -1)
            beg = 0;

        if(beg == idx) {
            for(int i = idx + 1; i < str.size(); ++i)
                str[i] = '9';
            str[idx]--;
        }
        else {
            for(int i = beg + 1; i < str.size(); ++i)
                str[i] = '9';
            str[beg]--;
        }

        printf("Case #%d: ", test);
        for(int i = 0; i < str.size(); ++i)
            if(str[i] != '0')
                cout << str[i];
        cout << "\n";
    }
    return 0;
}