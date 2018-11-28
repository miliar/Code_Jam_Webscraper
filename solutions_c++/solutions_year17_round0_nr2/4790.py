//
// Created by Taewoo Kim on 4/8/2017.
//

#include <iostream>

using namespace std;

string maxTidy(string&& s){
    int i = s.length() - 1;
    while (i > 0){
        if (s[i] < s[i-1]){
            s[i-1]--;
            for (int j = i; j < s.length() && s[j] != '9'; j++){
                s[j] = '9';
            }
        }
        i--;
    }
    if (s[0] == '0') s = s.substr(1);
    return s;
}

int main() {
    int t;
    cin >> t;

    for (int i = 1; i <= t; i++){
        string n;
        cin >> n;
        cout << "Case #" << i << ": " << maxTidy(move(n)) << endl;
    }
    return 0;
}