#include <vector>
#include <map>
#include <string>
#include <iostream>
#include <sstream>
#include <fstream>
#include <algorithm>

using namespace std;

const string path = "/Users/mac/Documents/cpp/Code Jam/";

const string IMPOSSIBLE = "IMPOSSIBLE";

const int N = 51;

int main() {
    freopen("/Users/mac/Documents/cpp/Code Jam/in", "r", stdin);
    freopen("/Users/mac/Documents/cpp/Code Jam/out", "w", stdout);
    
    int T;
    scanf("%d", &T);
    for (int CT = 1;  CT <= T; CT ++) {
        int r, y, b, o, v, g, n;
        scanf("%d%d%d%d%d%d%d", &n, &r, &o, &y, &g, &b, &v);
        printf("Case #%d: ", CT);
        
        int f,s,m;
        char F,S,M;
        
        if (y <= r && r <= b) {
            f = y;
            s = r;
            m = b;
            F = 'Y';
            S = 'R';
            M = 'B';
        } else if (r <= y && y <= b) {
            f = r;
            s = y;
            m = b;
            F = 'R';
            S = 'Y';
            M = 'B';
        } else if (y <= b && b <= r) {
            f = y;
            s = b;
            m = r;
            F = 'Y';
            S = 'B';
            M = 'R';
        } else if (b <= y && y <= r) {
            f = b;
            s = y;
            m = r;
            F = 'B';
            S = 'Y';
            M = 'R';
        } else if (b <= r && r <= y) {
            f = b;
            s = r;
            m = y;
            F = 'B';
            S = 'R';
            M = 'Y';
        } else if (r <= b && b <= y) {
            f = r;
            s = b;
            m = y;
            F = 'R';
            S = 'B';
            M = 'Y';
        }
        
        if (n - m < m) {
            printf("%s\n", IMPOSSIBLE.c_str());
            continue;
        }
        
        for (int i = 0; i < m; i ++) {
            printf("%c", M);
            
            if (i < f)
                printf("%c", F);
            
            if (m - 1 - i < s)
                printf("%c", S);
        }
        
        printf("\n");
    }
    
    
    return 0;
}
