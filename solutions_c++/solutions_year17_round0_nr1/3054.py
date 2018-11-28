#include <iostream>

using namespace std;

int main(){

    string s;
    int j, n, k, l, t, tam;

    cin >> n;

    for (int i = 1; i <= n; i++){
        cin >> s >> l;

        t = 0;
        tam = s.length() - l + 1;
        for (j = 0; j < tam; j++){
            if (s[j] == '-'){
                t++;
                s[j] = '+';
                for (int k = j+1; k < (j+l); k++)
                    (s[k] == '-') ? s[k] = '+' : s[k] = '-';
            }
        }

        for ( ; j < s.length(); j++){
            if (s[j] == '-'){
                break;
            }
        }
        if (j == s.length()){
            cout << "Case #" << i << ": " << t << endl;
        }else{
            cout << "Case #" << i << ": IMPOSSIBLE\n";
        }
    }
}
