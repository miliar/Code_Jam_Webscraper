#include <bits/stdc++.h>
using namespace std;

bool func(string num){
    int len=num.size();
    for(int i=0;i<len - 1; i++){
        if(num[i+1] < num[i])
            return false;
    }
    return true;
}

int main(){
    //freopen("input.txt", "r", stdin);
    //freopen("output.txt", "w", stdout);
    string s;
    int T, q=0, len;
    cin >> T;
    while(T--){
        q++;
        cin >> s;
        len = s.size();
        while(!func(s)){
            for(int i = 1; i < len; i++){
                if(s[i-1] > s[i]){
                    if(s[i-1] == '0')
                        s[i-1] = '9';
                    else
                        s[i-1]-=1;

                    for(int j=i;j<len;j++)
                        s[j] = '9';
                }
            }
        }

        for(int i = 0; s[i]=='0'; i++)
            s = s.substr(1, s.size());

        cout << "Case #" << q << ": " << s << endl;
    }
    return 0;
}

