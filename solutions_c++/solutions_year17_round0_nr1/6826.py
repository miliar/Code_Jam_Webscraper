#include <bits/stdc++.h>

using namespace std;

int t, k;
string s;

void action(int ind)
{
    int ans = 0;
    cin >> s >> k;
    for(int i = 0; i < s.size()-k+1; i++){
        if(s[i] == '-'){
            for(int j = 0; j < k; j++){
                if(s[i+j] == '-')
                    s[i+j] = '+';
                else
                    s[i+j] = '-';
            }
            ans++;
        }
    }
    cout << "Case #" << ind << ": ";
    for(int i = s.size()-k+1; i < s.size(); i++){
        if(s[i] == '-'){
            cout << "IMPOSSIBLE" << endl;
            return;
        }
    }
    cout << ans << endl;
}

int main()
{
    freopen("input.in", "r", stdin);
    freopen("output.txt", "w", stdout);
    cin >> t;
    for(int i = 0; i < t; i++)
        action(i+1);
    return 0;
}
