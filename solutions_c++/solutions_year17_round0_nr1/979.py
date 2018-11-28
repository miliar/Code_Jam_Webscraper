#include <iostream>
#include <string>
using namespace std;

int main() {
    int T, kase = 0; scanf("%d",&T);
    while (T--) {
        string s; int k; cin >> s >> k;
        int cnt = 0;
        for (int i = 0; i + k - 1 < s.size(); i ++) {
            if (s[i] == '-') {
                for (int j = 0; j < k; j ++) {
                    s[i+j] = (s[i+j] == '+' ? '-' : '+');
                }
                cnt ++;
            }
        }
        bool flag = 1;
        for (int i = 0; i < s.size(); i ++) {
            if (s[i] == '-') {
                flag = 0;
                break;
            }
        }
        printf("Case #%d: ",++kase);
        if (flag) printf("%d\n",cnt);
        else printf("IMPOSSIBLE\n");
    }
    return 0;
}
