#include <bits/stdc++.h>

using namespace std;

int t;
string s;
int k;
int main()
{
    freopen("in.txt","r",stdin);
    freopen("out.txt","w",stdout);
    cin >> t;
    for (int test = 1; test <= t; test++){
        cin >> s >> k;
        int cnt = 0;
        for (int i = 0; i <= s.length()-k; i++){
            if (s[i]=='-'){
                cnt++;
                for (int j = i; j < i+k; j++){
                    if (s[j]=='+')
                        s[j]='-';
                    else
                        s[j]='+';
                }
            }
        }
        bool b = true;
        for (int i = s.length()-k+1; i < s.length(); i++){
            if (s[i]=='-')
                b=false;
        }
        if (b){
            cout << "Case #" << test << ": " << cnt << "\n";
        }
        else cout << "Case #" << test << ": IMPOSSIBLE\n";
    }
    return 0;
}
