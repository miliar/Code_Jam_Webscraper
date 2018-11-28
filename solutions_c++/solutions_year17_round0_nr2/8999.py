#include <bits/stdc++.h>

using namespace std;

int main()
{
    int t, j;
    string s;
    bool f;
    freopen("B-small-attempt0.in", "r", stdin);
    freopen("output.out", "w", stdout);
    cin >> t;
    for (int i = 0; i < t; i++){
        cin >> s;
        printf("Case #%d: ", i+1);
        if (s.length() == 1)cout << s << endl;
        else{
            for (int l = 0; l < 18; l++){
                f = 0;
                for (int k = 0; k < s.length()-1; k++){
                    if (s[k] > s[k+1]){
                            if (!f){
                                s[k] --;
                                f = 1;
                            }
                            s[k+1] = '9';
                    }

                }
            }
            for (int k = 0; k < s.length(); k++){
                if (s[k] == '0')continue;
                cout << s[k];
            }
            cout << "\n";
        }
    }
    return 0;
}
