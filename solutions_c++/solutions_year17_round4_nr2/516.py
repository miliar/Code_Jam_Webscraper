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

const int N = 1002;

int a[N][N];

int main() {
    freopen("/Users/mac/Documents/cpp/Code Jam/in", "r", stdin);
    freopen("/Users/mac/Documents/cpp/Code Jam/out", "w", stdout);
    
    int T;
    scanf("%d", &T);
    for (int CT = 1;  CT <= T; CT ++) {
        int n, c, m;
        scanf("%d%d%d", &n, &c, &m);
        printf("Case #%d: ", CT);
        
        memset(a, 0, sizeof(a));
        
        for (int i = 0; i < m; i ++) {
            int pi, bi;
            scanf("%d%d", &pi, &bi);
            a[pi][bi] ++;
//            cout << pi << " c " << bi << endl;
        }
        
//        cout << a[1][2] << endl;
    
        int r = 0;
        
        for (int j = 1; j <= c; j ++) {
            int s = 0;
            for (int i = 1; i <= n; i ++)
                s += a[i][j];
            r = max(r, s);
        }
    
        int s = 0;
        for (int i = 1; i <= n; i ++) {
            for (int j = 1; j <= c; j ++)
                s += a[i][j];
//            cout << 'a' << s << endl;
            r = max(r, (s + i - 1) / i);
        }
        
        int res = r;
        
        int p = 0;
        for (int i = 1; i <= n; i ++) {
            int s = 0;
            for (int j = 1; j <= c; j ++)
                s += a[i][j];
            if (s > r)
                p += s - r;
        }
    
        printf("%d %d\n", res, p);
    }
    
    
    return 0;
}
