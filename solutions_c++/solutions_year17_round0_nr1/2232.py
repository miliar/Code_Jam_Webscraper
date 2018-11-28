#include <iostream>
#include <string>
using namespace std;

int main()
{
    int t, k;
    cin >> t;
    string s;
    for(int i = 0; i < t; i++){
        cin >> s >> k;
        int ans = 0;
        for(int i = 0; i + k <= s.length(); i++){
            if(s[i] == '-'){
                ans++;
                for(int j = 0; j < k; j++){
                    if(s[i + j] == '-')
                        s[i + j] = '+';
                    else
                        s[i + j] = '-';
                }
            }
        }
        for(int i = 0; i < s.length(); i++)
            if(s[i] == '-')
                ans = -1;
        cout << "Case #" << i + 1 << ": ";
        if(ans == -1)
            cout << "IMPOSSIBLE" << endl;
        else
            cout << ans << endl;
    }
    return 0;
}

