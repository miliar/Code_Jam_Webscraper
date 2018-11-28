#include <bits/stdc++.h>

using namespace std;

int main()
{
    int t;
    cin >> t;
    int tc = 1;

    while (t--) {
        string s;
        cin >> s;

        int i;
        for (i = 0; i+1 < s.size(); i++) {
            if (s[i] > s[i+1]) break;
        }

        if (i+1 < s.size()) {
            int j = 0;
            while (s[j] != s[i]) j++;

            s[j++]--;
            while (j < s.size()) s[j++] = '9';
        }

        i = 0;
        while (s[i] == '0') i++;
        printf("Case #%d: ", tc++);
        while (i < s.size()) printf("%c", s[i++]);
        printf("\n");
    }

    return 0;
}
