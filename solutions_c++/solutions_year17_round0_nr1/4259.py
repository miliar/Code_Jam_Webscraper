#include <bits/stdc++.h>

using namespace std;

typedef long long ll;

int main() {
#define TASK "A-large"
    freopen(TASK".in", "r", stdin), freopen(TASK".out", "w", stdout);
	int t;
    scanf("%d", &t);
    for(int cs = 1; cs <= t; ++cs){
        bool s[1123];
        int i = 0;
        char c;
        scanf("%c", &c);
        while(c != ' '){
            scanf("%c", &c);
            s[i++] = c == '+';
        }
        --i;
        int k;
        scanf("%d", &k);
        int ans = 0;
        for(int j = 0; j < i - k + 1; ++j){
            if(!s[j]){
                ++ans;
                for(int r = 1; r < k; ++r) s[j + r] = !s[j + r];
            }
        }
        bool can = true;
        for(int j = i - k + 1; j < i; ++j){
            if(!s[j]){
                printf("Case #%d: IMPOSSIBLE\n", cs);
                can = false;
                break;
            }
        }
        if(can) printf("Case #%d: %d\n", cs, ans);
    }
	return 0;
}
