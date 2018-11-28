#include <bits/stdc++.h>

using namespace std;

int main(int argc, const char * argv[]) {
    freopen("/Inputs/GC2017/in.txt", "r", stdin);
    freopen("/Inputs/GC2017/out.txt", "w", stdout);
    
    int t;
    scanf("%d\n", &t);
    for (int c = 1; c < t+1; c++) {
        string n;
        cin >> n;
        long long v = strtol(n.c_str(), nullptr, 10);
        long long r=0;
        for (int i = 0; i < n.length(); i++) {
            int d = n[i] - '0';
            long long nv = r;
            for (int j = i; j < n.length(); j++) {
                nv *= 10;
                nv += d;
            }
            if (nv > v) {
                r *= 10;
                r += d-1;
                for (int j = i + 1; j < n.length(); j++) {
                    r *= 10;
                    r += 9;
                }
                break;
            }
            r *= 10;
            r += d;
        }
        printf("Case #%d: %lld\n", c, r);
    }
    return 0;
}
