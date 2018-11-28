#include<iostream>
#include<string>
using namespace std;
int main(){
    int T;
    cin >> T;
    for(int i = 0; i < T; i++){
        string s;
        cin >> s;
        int k;
        cin >> k;
        int flip = 0;
        bool flag = true;
        for(int j = 0; j < s.size(); j++){
            if (s[j] == '+') continue;
            if (j + k > s.size()) {
                flag = false;
                break;
            }
            for(int cur = j; cur < j + k; cur++){
                s[cur] = (s[cur] == '+') ? '-' : '+';    
            }
            flip++;
        }
        if (flag) {
            cout << "Case #" << i + 1 << ": " << flip << endl;
        } else {
            cout << "Case #" << i + 1  <<  ": IMPOSSIBLE" << endl;
        }
    }
    return 0;
}
