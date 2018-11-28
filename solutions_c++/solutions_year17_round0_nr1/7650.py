#include <bits/stdc++.h>
using namespace std;

void flip(string& s, int index, int k){
    for (int i=index; k>0; --k,++i){
        if (s[i] == '-'){
            s[i] = '+';
        }
        else{
            s[i] = '-';
        }
    }
}

bool isHappy(const string& s){
    for (int i=0; i<s.length(); ++i){
        if (s[i] == '-'){
            return false;
        }
    }
    return true;
}

int main(){
    int t, k, count;
    string str;
    cin >> t;
    for (int z=1; z<=t; ++z){
        count = 0;
        cin >> str >> k;
        for (int i=0; i<=str.length()-k; ++i){
            if (str[i] == '-'){
                ++count;
                flip(str, i, k);
            }
        }
        cout << "Case #" << z << ": ";
        if (isHappy(str)){
            cout << count;
        }
        else{
            cout << "IMPOSSIBLE";
        }
        cout << "\n";
    }
    return 0;
}
