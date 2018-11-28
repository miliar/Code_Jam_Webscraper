#include <iostream>
#include <string>


using namespace std;

int flip(string s, int k){
    int flips = 0;
    for(int i = 0; i < s.size(); ++i){
        if((s.size()-i) < k && s[i] != '+') {flips = -1; break;}
        if(s[i] == '-'){
            string sub = s.substr(i,k);
            for(int j = 0; j < sub.size(); j++){
                sub[j] = (sub[j] == '+') ? sub[j] = '-' : sub[j] = '+';
            }
             s.replace(i,k,sub);
            flips++;
        }
    }
    return flips;
}

int main(){
    int cases;
    cin >> cases;
    for(int i = 0; i < cases; i++){
        string s;
        int k;
        cin >> s >> k;
        if(s.find('-') == -1){ cout << "Case #" << (i+1) << ": " << 0 << endl; continue;}
        int out = flip(s,k);
        if(out == -1) cout << "Case #" << i+1 << ": " << "IMPOSSIBLE" << endl;
        else cout << "Case #" << (i+1) << ": " << out << endl;
    }
    return 0;
}