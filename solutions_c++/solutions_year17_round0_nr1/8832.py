#include <bits/stdc++.h>
using namespace std;
void O_o() {
    ios_base::sync_with_stdio(0); cin.tie(0); cout.tie(0);
 }
int main()
{
    O_o();
    freopen ("A-small-practice.in","r",stdin);
    int t, ans, k;
    string s;
    cin >> t;
    for(int i = 1; i <= t; i++){
        ans = 0;
        cin >> s >> k;
        char str2[s.size()], *loc;
        strcpy(str2, s.c_str());
         for(int i = 0; i <= s.size() - k; i++) {
            if(str2[i] != '-')
                continue;
            for(int j = i; j < i + k; j++) {
                if(str2[j] == '-')
                    str2[j] = '+';
                else
                   str2[j] = '-';
            }
             ans++;
        }
    freopen ("A-small-practice.out","a",stdout);
    if (loc = strstr(str2, "-"))
        printf("Case #%d: IMPOSSIBLE\n", i);
    else
        printf("Case #%d: %d\n", i, ans);

}
    return 0;

}

