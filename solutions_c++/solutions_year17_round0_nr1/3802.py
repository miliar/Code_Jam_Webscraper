#include <iostream>
#include <algorithm>
#include <string>

using namespace std;

int main()
{

    freopen("A-large.in", "r", stdin);
    freopen("A-large.txt", "w", stdout);

    int t, n;
    string s;

    cin >> t;
    for(int i=1;i<=t;i++){
        cin >> s >> n;

        int ans = 0;
        for(int j=0;j<s.size()-n+1;j++){
            if(s[j] == '-'){
                ans++;
                s[j] = '+';
                for(int k=1;k<n;k++){
                    if(s[j+k] == '-') s[j+k] = '+';
                    else s[j+k] = '-';
                }
            }
        }
        bool f = true;
        for(int j=0;j<s.size();j++){
            if(s[j] == '-'){
                cout << "Case #"<< i << ": " << "IMPOSSIBLE" <<'\n';
                f = false;
                break;
            }
        }
        if(f)
            cout << "Case #"<< i << ": " << ans <<'\n';
    }

    return 0;
}
