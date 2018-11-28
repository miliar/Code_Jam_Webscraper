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

int q[N][N];
int a[N][N];
int b[N][N];
int r[N];

int c[N];

int main() {
    freopen("/Users/mac/Documents/cpp/Code Jam/in", "r", stdin);
    freopen("/Users/mac/Documents/cpp/Code Jam/out", "w", stdout);
    
    int T;
    scanf("%d", &T);
    for (int CT = 1;  CT <= T; CT ++) {
        int n, d;
        scanf("%d%d", &d, &n);
        printf("Case #%d: ", CT);
        
        double res = 0;
        for (int i = 0; i < n; i ++) {
            int k, s;
            scanf("%d%d", &k, &s);
            res = max(res, double(d - k) / s);
        }
        
        printf("%lf\n", d / res);
    }
    
    
    return 0;
}
