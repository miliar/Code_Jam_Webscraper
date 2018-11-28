#include <iostream>
using namespace std;

char flip(char c){
    if(c == '+') return '-';
    else return '+';
}

int main(){
    int r; cin >> r; for(int t = 1; t <= r; t++){
        string s; int k;
        cin >> s >> k;
        int counter = 0;
        for(int i = 0; i <= s.length() - k; i++){
            if(s[i] == '-'){
                counter++;
                for(int j = 0; j < k; j++){
                    s[i+j] = flip(s[i+j]);
                }
            }
        }
        bool f = true;
        for(int i = s.length() - k; i < s.length(); i++){
            if(s[i] == '-') f = false;
        }
        if(f) cout << "Case #" << t << ": " << counter << endl;
        else cout << "Case #" << t << ": " << "IMPOSSIBLE" << endl;
    }
    return 0;
}

