#include<iostream>
#include<map>
#include<string>
using namespace std;
typedef long long ll;

bool isQual(ll a){
    int last = a-a/10*10;
    a /= 10;
    while (a > 0) {
        if (last >= a-a/10*10) {
            last = a-a/10*10;
            a /= 10;
        }else{
            return false;
        }
    }
    return true;
}

int main(){
    int T;
    cin >> T;
    for(int t = 1; t <= T; t++){
        string s;
        cin >> s;
        string ans;
        bool flag = false;
        for (int i = 1; i < s.size(); i++) {
            if (s[i] < s[i-1]) {
                flag = true;
                int j = i;
                while (j > 0 && (s[j] == '0' || s[j] < s[j-1])) {
                    ans = "9"+ans;
                    s[j-1]--;
                    j--;
                }
                if (j == 0 && s[j] == '0') {
                    
                }else{
                    ans = s.substr(0, j+1) + ans;
                }
                for (int j = i+1; j < s.size(); j++) {
                    ans += "9";
                }
                break;
            }
        }
        if (!flag) {
            ans = s;
        }
        cout << "Case #" << t << ": " << ans << endl;
    }
    return 0;
}