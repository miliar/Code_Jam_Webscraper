#include <bits/stdc++.h>

#define LL long long

using namespace std;

int main() {
    int n;

    cin >> n;
    for(int i = 0; i < n; i++) {
        string str; int k;
        cin >> str >> k;

        LL ans = 0;
        for(int j = 0; j <= str.length() - k; j++) {
            if(str[j] == '-') {
                for(int l = j; l < j + k; l++) {
                    str[l] = (str[l] == '-') ? '+' : '-';
                }

                // cout << str << endl;
                ans++;
            }
        }

        bool impossible = false;
        for(int j = 0; j < str.length(); j++) {
            if(str[j] == '-') {
                impossible = true;
                break;
            }
        }

        if(impossible) printf("Case #%d: IMPOSSIBLE\n", i + 1);
        else printf("Case #%d: %lld\n", i + 1, ans);
    }

    return 0;
}