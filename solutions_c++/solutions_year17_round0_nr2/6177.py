#include <iostream>
#include <cstdio>
#include <cstring>
#include <string>

using namespace std;

int main(){
    int T;
    cin >> T;
    int csT = 1;
    while(T--){
        string s;
        cin >> s;
        int flag = 0;
        int slen = s.length();
        for(int i = slen - 1; i > 0; i--){
            if(flag == 1){
                s[i] = s[i] - flag;
                flag = 0;
            }
            if(s[i] < s[i-1] || s[i] == '0'){
                for(int j = i; j < slen; j++){
                    s[j] = '9';
                }
                flag = 1;
            }
        }
        cout << "Case #"<<csT++<<": ";
        if(flag == 1)
            s[0] = s[0] - 1;
        for(int i = 0; i < slen; i++)
            if(s[i] != '0')
                cout << s[i] ;
        cout << endl;
    }
    return 0;
}
