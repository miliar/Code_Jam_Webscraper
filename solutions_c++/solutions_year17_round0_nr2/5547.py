#include <bits/stdc++.h>

using namespace std;

int main()
{
    ifstream cin("in (2).in");
    ofstream cout("out.txt");
    ios_base::sync_with_stdio(0);

    int T;
    cin >> T;
    //T = 1;
    for (int t = 1; t <= T; t++){
        string s;
        cin >> s;
        bool fl = 0;
        for (int i = 0; i < (int)s.size() - 1; i++)
            if (s[i] > s[i + 1])
                fl = 1;

        cout << "Case #" << t << ": ";

        if (!fl){
            cout << s << '\n';
            continue;
        }

        for (int i = (int)s.size() - 1; i >= 0; i--){
            if (i == 0){
                if (s[i] == '1'){
                    for (int it = 0; it < (int)s.size() - 1; it++)
                        cout << '9';
                    cout << '\n';
                }
                else{
                    cout << (char)(s[i] - 1);
                    for (int it = 0; it < (int)s.size() - 1; it++)
                        cout << '9';
                    cout << '\n';
                }
            }
            else{
                bool f = 0;
                for (int it = 0; it < i; it++)
                    if (s[it] > s[it + 1])
                        f = 1;
                if (f || s[i] <= s[i - 1])
                        continue;
                for (int it = 0; it < i; it++)
                    cout << s[it];
                cout << (char)(s[i] - 1);
                for (int it = i + 1; it < (int)s.size(); it++)
                    cout << '9';
                cout << '\n';
                break;
            }
        }
    }
    return 0;
}
