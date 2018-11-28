#include <iostream>
#include <cstdio>

#define For(i, n) for(int i = 0; i < (n); i++)

using namespace std;

int main () {
    int t;
    scanf("%d", &t);

    For (i, t) {
        char c[1020];
        scanf("%s", c);
        string s(c);
        
        int k;
        scanf("%d", &k);
        int cnt = 0;
        bool can = true;

        For (j, (int)s.size()) {
            if (s[j] == '-')
            {
                if ((int)s.size() - j < k) {
                    can = false;
                    break;
                }

                cnt++;
                For (l, k)
                    s[j + l] = (s[j + l] == '-' ? '+' : '-');
            }
        }

        For (j, (int)s.size()) {
            if (s[i] == '-') {
                can = false;
                break;
            }
        }

        if (can)
            printf("Case #%d: %d\n", i + 1, cnt);
        else
            printf("Case #%d: IMPOSSIBLE\n", i + 1);
    }
}