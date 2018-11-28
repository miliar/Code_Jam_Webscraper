/* Paras Narang 
 *
 */
#include <iostream>
#include <string>

using namespace std;

bool isTidy(string s) {
    for(int i = 0; i+1 < s.length(); i++) {
        if (s[i] > s[i+1]) {
            return false;
        }
    }
    return true;
}

string tidify(string s) {
    int index = -1;
    for(int i = 0; i+1 < s.length(); i++) {
        if(s[i] > s[i+1]){
            s[i] = s[i] - 1;
            index = i;
            break;
        }
    }
    for(int i = index - 1; i >= 0; i--) {
        if(s[i] <= s[i+1]) {
            break;
        }
        s[i] = s[i] - 1;
        index = i;
    }
    if(index != -1) {
        for(int i = index+1; i < s.length(); i++) {
            s[i] = '9';
        }
    }
    return s;
}

int main() {
    int t, ti;
    cin >> t;

    for(ti = 0; ti < t; ti++) {
        string res;
        cin >> res;
        while(!isTidy(res)) {
            res = tidify(res);
        }
        printf("Case #%d: %lld\n", ti+1, stoll(res));
    }
    return 0;
}
