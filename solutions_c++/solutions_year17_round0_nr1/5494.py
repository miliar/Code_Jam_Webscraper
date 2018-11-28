#include <iostream>
#include <string>

using namespace std;

void flip(string &s, int i){
        if (s[i]=='+'){
                s[i] = '-';
        }
        else{
                s[i] = '+';
        }
}

int main(){
        int t,ca;
        ca = 1;
        cin >> t;
        while (t--){
                string s;
                int k;
                cin >> s >> k;
                int ctr = 0;
                for (int i=0;i<=s.length()-k;i++){
                        if (s[i]=='-'){
                                ctr++;
                                for (int j=0;j<k;j++){
                                        flip(s,i+j);
                                }
                        }
                }
                int flag = 0;
                for (int i=s.length()-k;i<s.length();i++){
                        if (s[i]=='-'){
                                flag = 1;
                        }
                }
                cout << "Case #" << ca <<": ";
                if (flag){
                        cout << "IMPOSSIBLE\n";
                }
                else{
                        cout << ctr << '\n';
                }
                ca++;
        }
        return 0;
}
