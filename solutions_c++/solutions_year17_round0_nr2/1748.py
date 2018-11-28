#include <iostream>
#include <string>
#include <vector>
#include <algorithm>
#include <stdio.h>
#include <cstring>
#include <stdlib.h>
#include <cmath>
#include <map>
using namespace std;

int T;
typedef long long ll;
string str;
int main() {
    int C = 1;
    freopen("in.txt","r",stdin);
    freopen("out.txt","w",stdout);
    cin >> T;
    while (T --) {
        cin >> str;
        int len = str.size();

        for (int i = 0;i < len;i ++) {
            if (i + 1 < len && str[i] > str[i + 1]) {
                str[i] = (str[i] - '0' - 1) + '0';
                for (int j = i + 1;j < len;j ++) {
                    str[j] = '9';
                }
                i -= 2;
            }
        }
        printf("Case #%d: ",C ++);
        string ans = "";
        bool beg = false;
        for (int i = 0,sz = str.size();i < sz;i ++) {
            if (!beg) {
                if (str[i] != '0') {
                    beg = true;
                }
            }
            if (beg) {
                ans += str[i];
            }
        }
        cout << ans << endl;
    }
 }















