#include <iostream>
#include <string>

using namespace std;

int main(){

    int n, j;
    char c;
    string s;

    cin >> n;

    for (int i = 1; i <= n; i++){

        cin >> s;

        c = s[s.length()-1];
        for (j = s.length() - 2; j >= 0; j--){
            if (s[j] > c){
                s[j]--;
                for (int k = j+1; k < s.length(); k++){
                    s[k] = '9';
                }
            }
            c = s[j];
        }
        for (j = 0; j < s.length(); j++){
            if (s[j] != '0') break;
        }
        s = s.substr(j);

        cout << "Case #" << i << ": " << s << endl;
    }
}
