#include <bits/stdc++.h>

using namespace std;

int main()
{
    //freopen("B-large.in", "r", stdin);
    //freopen("out.txt", "w", stdout);
    int cases, caseno = 0;
    scanf("%d", &cases);
    while(cases--){
        string str;
        cin >> str;
        if(str.length() == 1) cout << "Case #" << ++caseno << ": " << str << endl;
        else {
            int imperfect = -1;
            for(int i=1; i<str.length(); i++){
                int v = str[i] - '0';
                int u = str[i-1] - '0';
                if(v < u){
                    imperfect = i;
                    break;
                }
            }
            if(imperfect == -1) cout << "Case #" << ++caseno << ": " << str << endl;
            else {
                int flag = 0;
                for(int i=imperfect-1; i>=0; i--){
                    if(str[i] != '1') flag = 1;
                }
                if(flag == 0){
                    string ans = "";
                    for(int i=0; i<str.length()-1; i++) ans += '9';
                    cout << "Case #" << ++caseno << ": " << ans << endl;
                }
                else {
                    int temp;
                    char x = str[imperfect - 1];
                    for(int i=0; i<imperfect; i++){
                        if(str[i] == x){
                            str[i] = char((int) x - 1);
                            temp = i+1;
                            break;
                        }
                    }
                    for(int i=temp; i<str.length(); i++){
                        str[i] = '9';
                    }
                    cout << "Case #" << ++caseno << ": " << str << endl;
                }
            }
        }
    }
}
