#include<bits/stdc++.h>
using namespace std;
int main()
{
    freopen("input.txt", "r", stdin);
    freopen("out.txt", "w", stdout);
    int t;
    cin >> t;
    int test = 1;
    while(test <= t) {
        string s;
        int p_len;
        cin >> s >> p_len;
        int ans = 0;
        for(int i=0;i<s.length()-p_len+1;i++) {
            if(s[i] == '-') {
                ans++;
                for(int j=i;j<i+p_len;j++) {
                    if(s[j] == '-')
                        s[j] = '+';
                    else
                        s[j] = '-';
                }
            }
        }
        int check = 0;
        for(int i=0;i<s.length();i++) {
            if(s[i] == '-') {
                check = 1;
                break;
            }
        }
        if(check == 1)
           cout << "Case #" << test << ": " << "IMPOSSIBLE"  << endl;
        else
           cout << "Case #" << test << ": " << ans  << endl;
        test++;
    }
    fclose(stdin);
    fclose(stdout);
    return 0;
}

