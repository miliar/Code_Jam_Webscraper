#include<iostream>
#include<string>
using namespace std;
string isTinyNumbers(string& s){
    int j = 1;
    bool flag = true;
    for(j = 1; j < s.size(); j++){
        if (s[j] < s[j - 1]){
            s[j - 1] -= 1;
            flag = false;
            break;
        }
    }
    if (flag) return s;
    for(; j < s.size(); j++){
        s[j] = '9';
    }
    isTinyNumbers(s);
    return s;
}
int main(){
    int T;
    cin >> T;
    for(int i = 0; i < T; i++){
        string s;
        cin >> s;
        isTinyNumbers(s);
        int j = 0;
        for(; j < s.size()-1; j++){
            if (s[j] != '0') break;
        }
        cout << "Case #" << i + 1 << ": "  <<  s.substr(j) << endl;
    }
    return 0;
}
