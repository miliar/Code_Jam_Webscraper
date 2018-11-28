#include <bits/stdc++.h>

using namespace std;

int main()
{
    freopen("input.txt", "r", stdin);
    freopen("output.txt", "w", stdout);
    int t;
    cin >> t;
    for (int cnt = 0; cnt < t; cnt++){
        string s;
        cin >> s;
        vector<int> vt;
        int ct = 1;
        for (int i = 1; i < s.size(); i++){
            if (s[i] < s[i - 1]){
                ct = 0;
                break;
            }
            else if (s[i] == s[i - 1]){
                ct++;
            }
            else{
                vt.push_back(ct);
                ct = 1;
            }
        }
        if (ct != 0){
            vt.push_back(ct);
        }
        cout << "Case #" << cnt + 1 << ": ";
        if (vt.empty() && s[0] == '1'){
            for (int i = 1; i < s.size(); i++){
                cout << "9";
            }
        }
        else{
            ct = 0;
            for (auto v: vt){
                ct += v;
            }
            for (int i = 0; i < ct; i++){
                cout << s[i];
            }
            if (ct != s.size()){
                cout << (char)(s[ct] - 1);
                for (int i = ct + 1; i < s.size(); i++){
                    cout << "9";
                }
            }
        }
        cout << "\n";
    }
    return 0;
}
