#include <iostream>
#include <cstdio>
#include <vector>

using namespace std;

int main()
{
    freopen("input.txt", "r", stdin);
    freopen("output.txt", "w", stdout);

    ios::sync_with_stdio(false);
    cin.tie(NULL);
    int T;
    cin >> T;

    for(int qqq = 0; qqq < T; qqq++){
        string s;
        cin >> s;
        int n = s.length();
        bool f = false;
        cout << "Case #" << qqq + 1 << ": ";
        for(int i = n-1; i > 0; i--){
            if(s[i] < s[i-1]){
                int pos = -1;
                for(int j = i-1; j >= 0; j--){
                    if(s[j] != '0'){
                        pos = j;
                        break;
                    }
                }
                if(pos == 0 && s[pos] == '1'){
                    f = true;
                    break;
                }
                s[pos] = s[pos] - 1;
                for(int j = pos + 1; j < n; j++){
                    s[j] = '9';
                }
            }
        }
        if(f){
            for(int i = 0; i < n-1; i++){
                cout << '9';
            }
        } else {
            cout << s;
        }
        cout << endl;
    }
    return 0;
}
