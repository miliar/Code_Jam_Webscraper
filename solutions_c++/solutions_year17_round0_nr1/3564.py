#include <bits/stdc++.h>
using namespace std;
string s;
int k,c,t;
bool flag;
int main(){
    scanf("%d", &t);
    for (int i = 1; i <= t; i++){
        cin >> s;
        printf("Case #%d: ", i);
        scanf("%d", &k); flag = true;
        c = 0;
        for (int j = 0; j <= s.size()-k; j++){
            if (s[j] == '-'){
                for (int m = j; m < j+k; m++){
                    if (s[m] == '-') s[m] = '+';
                    else s[m] = '-';
                }
                c++;
            }
        }
        for (int j = 0; j < s.size(); j++){
            if (s[j] == '-') flag = false;
        }
        if (!flag) printf("IMPOSSIBLE\n");
        else printf("%d\n", c);
    }
}
