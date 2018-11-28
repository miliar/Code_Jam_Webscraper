#include<iostream>
#include<string>

using namespace std;

int main(){
    int t;
    cin >> t;
    for(int i = 1; i <= t; i++){
        string s;
        int k, ans;
        cin >> s >> k;
        ans = 0;
        for(auto j = s.begin(); j < s.end() - k + 1; j++){
            if(*j == '-'){
                for(int l = 0; l < k; l++){
                    if(*(j + l) == '+')*(j + l) = '-';
                    else *(j + l) = '+';
                }
                ans++;
            }
        }
        int cnt = 0;
        for(auto j = s.begin() - k + 1; j < s.end(); j++){
            if(*j == '-'){
                cnt++;
                break;
            }
        }
        cout << "Case #" << i << ": ";
        if(cnt)cout << "IMPOSSIBLE" << '\n';
        else cout << ans << '\n';
    }

    return 0;
}
