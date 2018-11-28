#include <iostream>

using namespace std;

int main(){
    int T;
    cin >> T;
    for(int t=1;t<=T;t++){
        string s;
        cin >> s;
        int K;
        cin >> K;

        int sol = 0;
        bool possible = true;
        for(int i=0;i<s.size();i++){
            if(s[i] == '-' && s.size() - i < K){
                possible = false;
            } else if(s[i] == '-'){
                sol++;
                for(int j=0;j<K;j++){
                    s[i+j] = s[i+j] == '-' ? '+' : '-';
                }
            }
        }

        cout << "Case #" << t << ": ";
        if(possible){
            cout << sol << endl;
        } else {
            cout << "IMPOSSIBLE" << endl;
        }
    }
}
