#include <bits/stdc++.h>

using namespace std;


int main()
{
    freopen("B-large.in", "r", stdin);
    freopen("output.txt", "w", stdout);
    int tt;
    cin >> tt;
    for(int tn= 1; tn <= tt; tn++){
        string s;
        cin >> s;
        int f = -1;
        int tmp = 0;
        for(int i = 0; i < (int)(s.size())-1; i++){
            if(( (s[i+1]-'0') < (s[i] - '0') ) ){
                if(i >= 1 && s[i] == s[i-1]){
                    f = tmp;
                }else{
                    f = i;
                }
                break;
            }
            if(s[i] != s[i+1]){
                tmp = i+1;
            }
        }
        if(f != -1 && s.size() > 1){
            s[f]--;
            for(int i = f+1; i < s.size(); i++){
                s[i] = '9';
            }
        }
        if(s[0] == '0'){
            cout << "Case #" << tn << ": " << s.substr(1) << endl;
        }else{
            cout << "Case #" << tn << ": " << s << endl;
        }
    }
    return 0;
}
