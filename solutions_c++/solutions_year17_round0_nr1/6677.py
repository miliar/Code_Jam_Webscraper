#include <bits/stdc++.h>
using namespace std;

int main() {
    int n, t, i, j, c, l, k, m;
    char s[1001];

    cin >> m;

    for(t = 1; t <= m; t++){
        cin >> s >> k;
        l = strlen(s) - k;
        i = c = 0;

        while(s[i] && i <= l){
            while(s[i] && s[i] == '+')
                i++;

            if(s[i] && i <= l){
                j = 0; c++;

                while(j < k){
                    if(s[i + j] == '+')
                        s[i + j] = '-';
                    else
                        s[i + j] = '+';
                    j++;
                }
                i++;
            }
        }

        l += k;

        while(i < l && c != -1)
            if(s[i++] == '-')
                c = -1;

        if(c == -1)
            cout << "Case #" << t << ": IMPOSSIBLE" << endl;
        else
            cout << "Case #" << t << ": " << c << endl;
    }
    return 0;
}
