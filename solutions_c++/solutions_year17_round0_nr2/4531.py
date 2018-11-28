
// Kasimir Tanner 2017
#include <iostream>
#include <vector>
#include <string>

using namespace std;

typedef long long int llint;
typedef unsigned long long int ullint;

string tidy(string s, ullint pos){
    s[pos]--;
    for(ullint i = pos+1;i<s.size();i++){
        s[i] = '9';
    }
    return s;
}

ullint check(string s){
    for(ullint i = 1;i<s.size();i++){
        if(s[i] < s[i-1])return i-1;
    }
    return -1;
}

string clarify(string s){
    if(s[0] == '0')return s.substr(1);
    return s;
}

int main(){
    ios_base::sync_with_stdio(false);
    cin.tie(0);

    ullint T;
    cin >> T;
    
    for(ullint t = 0;t< T;t++){
        string s;
        cin >> s;

        ullint r = check(s);

        while(r != -1){
            s = tidy(s,r);
            r = check(s);
        }

        cout << "Case #" << t+1 << ": " << clarify(s) << "\n";

    }
    return 0;
}