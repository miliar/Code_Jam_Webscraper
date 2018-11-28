#include <iostream>
#include <string>

using namespace std;

int main() {
    int TC; cin >> TC; ++TC;
    string s; int cap;
    for(int tc = 1; tc < TC; ++tc) {
        cin >> s >> cap; cin.get();
        // cout << s << " " << cap;
        int ans = 0;
        for(unsigned int i = 0; i < s.size(); ++i) {
            if (s[i] == '-') {
                if (i + cap > s.size()) {ans = -1; break;}
                ++ans;
                for(int j = 0; j < cap; ++j) {
                    s[i+j] = (s[i+j] == '+' ? '-' : '+');
                }
            }
        }
        if (ans != -1)
            printf("Case #%d: %d\n", tc, ans);
        else
            printf("Case #%d: IMPOSSIBLE\n", tc);
    }
    return 0;
}
