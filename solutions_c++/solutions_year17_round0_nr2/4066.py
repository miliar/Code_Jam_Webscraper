#include <bits/stdc++.h>

#define LL long long

using namespace std;

string str;

int main() {
    int n;
    cin >> n;

    for(int i = 1; i <= n; i++) {
        cin >> str;
        
        for(int j = 1; j < str.length(); j++) {
            if(str[j - 1] > str[j]) {
                int l = j;
                while(str[l - 1] > str[l]) {
                    str[l - 1]--;
                    for(int k = l; k < str.length(); k++) {
                        str[k] = '9';
                    }
                    l--;
                }

                break;
            }
        }

        while(str[0] == '0') {
            str = str.substr(1);
        }

        printf("Case #%d: ", i);
        cout << str << endl;
    }

}