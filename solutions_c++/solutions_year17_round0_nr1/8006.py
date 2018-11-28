#include <bits/stdc++.h>
using namespace std;

int t, k, ans, j, i;
string s;

void rep(int i){
    for(int a = i ; a < i+k ; a++) s[a] = (s[a] == '-' ? '+' : '-');
}
int main()
{
    freopen("A-large.in" , "r" , stdin);
    freopen("o.txt" , "w" , stdout);
    cin >> t;
    while(t-- && cin >> s >> k){
        ans = i = 0;
        cout << "Case #" << ++j << ": ";
        for(; i < s.size() ; i++){
            if(s[i] == '-' && s.size()-i < k){cout << "IMPOSSIBLE\n"; break;}
            if(s[i] == '-') ans++, rep(i);
        }
        if(i == s.size()) cout << ans << endl;
    }
    fclose (stdout);
    return 0;
}
