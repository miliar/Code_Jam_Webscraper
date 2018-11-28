#include <cstdio>
#include <iostream>
#include <algorithm>
#include <cstring>
using namespace std;
char input[2000];
int main() {
    int i, j, T, cnt, k, ans;
    bool imp;
    cnt = 0;
    cin>> T;
    while(T--) {
        cin >> input >> k;
        ans = 0;
        imp = false;
        int len = strlen(input);
        for (i = 0; i < len; i++) {
            if ( input[i] == '+') {
                ;
            } else {
                ans++;
                if (len-i < k) {
                    imp = true;
                    break;
                }
                for (j = i; j < k+i; j++) {
                    if (input[j] == '+' ) {
                        input[j] = '-';
                    } else {
                        input[j] = '+';
                    }
                }
            }
        }
        cout <<"Case #"<<++cnt<< ": ";

        if (imp) {
            cout <<"IMPOSSIBLE"<<endl;
        } else {
            cout <<ans<<endl;
        }
    }
    return 0;
}
