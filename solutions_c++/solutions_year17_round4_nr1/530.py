#include <bits/stdc++.h>

using namespace std;

int main() {
//    freopen("sample.in", "r", stdin);
//    freopen("A-small-attempt1.in", "r", stdin);
    freopen("A-large.in", "r", stdin);
    freopen("output.txt", "w", stdout);
    int tc;
    cin >> tc;
    int c[4];
    for (int ti = 1; ti <= tc; ++ti) {
        printf("Case #%d: ", ti);
        int n, p;
        cin >> n >> p;            
        for (int i = 0; i < p; ++i) c[i] = 0;
        for (int i = 0; i < n; ++i) {
            int x; cin >> x; ++c[x%p];
        }

        if (p == 2) {
            int g = c[0] + (c[1]+1)/2;
            printf("%d\n", g);
        }
        else if (p == 3) {
            int x = min(c[1], c[2]);
            int y = max(c[1], c[2]);
            int g = c[0] + x + (y-x)/3 + ((y-x)%3 > 0); 
            printf("%d\n", g);
        }
        else {
            int x = min(c[1], c[3]);
            int y = max(c[1], c[3]);
            int g = c[0] + x + (y-x)/4 + c[2]/2; 
            if (c[2]&1) {
                g += ((y-x)%4 + c[2]%2)/3 + (((y-x)%4 + c[2]%2)%3 > 0);
            }
            else {
                g += (y-x)%4 > 0;
            }
            printf("%d\n", g);
        }
    }
    return 0;
}
