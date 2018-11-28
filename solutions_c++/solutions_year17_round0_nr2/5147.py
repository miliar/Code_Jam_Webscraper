#define B
#ifdef B

#include <bits/stdc++.h>
using namespace std;

int main(){
    ios::sync_with_stdio(0);
    int T;cin >> T;

    for (int i = 1; i <= T; ++i) {
        string str;
        cin >> str;
        for (int j = 0; j < str.size()-1; ++j) {
            if(str[j] <= str[j+1] ) continue;
            else{
                if(str[j] == 0) {
                    for (int k = j; k < str.size(); ++k) {
                        str[k] = '9';
                    }
                 }
                else{
                    str[j] -= 1;

                    for (int k = j+1; k < str.size(); ++k) {
                        str[k] = '9';
                    }
                    j -= 2;
                    while(str[0] == '0') str = str.substr(1,str.size()-1);
                }
            }
        }
        cout << "Case #" << i << ": " << str << endl;
    }

    return 0;
}

#endif