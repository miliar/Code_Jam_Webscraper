#include <iostream>
#include <cstdio>
#include <vector>

using namespace std;

int main()
{
    //freopen("input.txt", "r", stdin);
    //freopen("output.txt", "w", stdout);

    ios::sync_with_stdio(false);
    cin.tie(NULL);
    int T;
    cin >> T;

    for(int qqq = 0; qqq < T; qqq++){
        string s;
        cin >> s;
        int k;
        cin >> k;
        cout << "Case #" << qqq + 1 << ": ";
        int n = s.length();
        int res = 0;
        for(int l = 0; l < n - k + 1; l++){
            if(s[l] == '+'){
                continue;
            }
            res ++;
            for(int i = l; i < l + k; i++){
                if(s[i] == '-'){
                    s[i] = '+';
                } else {
                    s[i] = '-';
                }
            }
        }
        bool f = false;
        for(int i = 0; i < n; i++){
            if (s[i] != '+'){
                cout << "IMPOSSIBLE";
                cout << endl;
                f = true;
                break;
            }
        }
        if(!f){
            cout << res;
            cout << endl;
        }
    }
    return 0;
}
