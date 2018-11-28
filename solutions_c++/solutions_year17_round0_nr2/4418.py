#include <bits/stdc++.h>
using namespace std;

#define SZ(x) ((int)(x).size())
#define LE(x) ((int)(x).length())

void solve() {
    string str;
    cin >> str;
    reverse(str.begin(), str.end());
    char minimum = '9';
    
    for (int i=0; i<LE(str); i++){
        if (str[i] > minimum) {
            for (int j=0; j<i; j++){
                str[j] = '9';
            }
            str[i]--;
        }
        minimum = str[i];
    }
    
    reverse(str.begin(), str.end());
    int index = 0;
    while (str[index] == '0'){
        index++;
    }
    while (index < LE(str)){
        cout << str[index++];
    }
    cout << endl;
}
    

int main() {
    int T;
    cin >> T;
    for (int i=0; i<T; i++){
        cout << "Case #" << i+1 <<": ";
        solve();
    }
}
