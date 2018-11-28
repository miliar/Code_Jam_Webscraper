#include <iostream>
#include <string.h>
using namespace std;
inline int count(string s, int k){

    if(check(s))
        return 0;

    int count = 0;
    for(int i = 0; i < s.size(); i++){
        if(s[i] == '-'){
            for(int j = i; j < i + k || j < s.size(); j++){
                if(s[i] == '-')
                    s[i] = '+';
                else
                    s[i] = '-';
            }
            count++;
        }
        if(check)
            return count;
    }

        return -1;
}

inline bool check(string s){

    for(int i = 0; i < s.size(); i++){
        if(s[i] == '-')
            return false;
    }
    return true;
}

int main(){
    int t, k, ans = -1;
    string s;
    cin >> t;
    int caso = 0;
    while(t--){
        cin >> s >> k;
        ans = count(s, k);

        cout << "Case #" << caso + 1 << ": ";
        if(ans == -1)   cout << "IMPOSSIBLE\n";
        else cout << ans << "\n";
        caso++;
    }
    return 0;
}
