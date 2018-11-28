#include <bits/stdc++.h>

using namespace std;

int main(int argc, const char * argv[]) {
    freopen("/Inputs/GC2017/in.txt", "r", stdin);
    freopen("/Inputs/GC2017/out.txt", "w", stdout);
    
    int n;
    cin >> n;
    
    for (int c = 1; c <= n; c++) {
        string p;
        int k, swaps = 0;
        cin >> p >> k;
        for (int i = 0; i <= p.size() - k; i++) {
            if (p[i] == '-') {
                swaps++;
                for (int j = 0; j < k; j++) {
                    if (p[i+j] == '-') {
                        p[i+j] = '+';
                    } else {
                        p[i+j] = '-';
                    }
                }
            }
        }
        bool is = true;
        for (char a : p) {
            if (a == '-') {
                is = false;
            }
        }
        if (is) {
            printf("Case #%d: %d\n", c, swaps);
        } else {
            printf("Case #%d: IMPOSSIBLE\n", c);
        }
    }
    
    return 0;
}
