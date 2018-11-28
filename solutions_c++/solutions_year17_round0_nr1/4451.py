#include <bits/stdc++.h>
using namespace std;

#define SZ(x) ((int)(x).size())
#define LE(x) ((int)(x).length())

void solve() {
    string str;
    int K;
    cin >> str >> K;
    int cnt = 0;
    for (int i=0; i<LE(str)-K+1; i++) {
        if (str[i] == '-'){
            cnt++;
            for (int j=i; j-i<K; j++){
                str[j] = (str[j] == '+' ? '-' : '+');
            }
        }
    }
    for (int i=0; i<LE(str); i++){
        if (str[i] == '-') {
            cout << "IMPOSSIBLE" << endl;
            return;
        }
    }
    cout << cnt << endl;
}
    

int main() {
    int T;
    cin >> T;
    for (int i=0; i<T; i++){
        cout << "Case #" << i+1 <<": ";
        solve();
    }
}
