
#include <bits/stdc++.h>

using namespace std;

int T, K;
string str;

int main(){
    freopen("A-large.in", "r", stdin);
    freopen("pancake_2.txt", "w", stdout);

    cin >> T;
    for (int c = 1; c <= T; c++){
        cin >> str >> K;
        int cnt = 0;
        for (int i = 0; i + K <= str.size(); i++){
            //printf("%s\n", str.c_str());
            if (str[i] == '-'){
                cnt++;
                for (int j = i; j < i + K; j++){
                    str[j] = (str[j] == '-' ? '+' : '-');
                }
            }
        }
        bool flag = true;
        for (int i = 0; i < str.size(); i++){
            if (str[i] == '-'){
                flag = false;
                break;
            }
        }

        if (flag)
            printf("Case #%d: %d\n", c, cnt);
        else
            printf("Case #%d: IMPOSSIBLE\n", c);
    }
}
