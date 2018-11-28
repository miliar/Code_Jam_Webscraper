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

const int N = 101;

int n, p;
int a[N];

int count(int m) {
    int r = 0;
    for (int i = 0; i < n; i ++)
        if (a[i] % p == m)
            r ++;
    return r;
}

int main() {
    freopen("/Users/mac/Documents/cpp/Code Jam/in", "r", stdin);
    freopen("/Users/mac/Documents/cpp/Code Jam/out", "w", stdout);
    
    int T;
    scanf("%d", &T);
    for (int CT = 1;  CT <= T; CT ++) {
//        int n, p;
        scanf("%d%d", &n, &p);
        printf("Case #%d: ", CT);
        
        for (int i = 0; i < n; i ++)
            scanf("%d", &a[i]);
        
        int res = 0;
        if (p == 2) {
            res = count(0) + (count(1) + 1) / 2;
        } else if (p == 3) {
            int pairs = min(count(1), count(2));
            int triples = count(1) + count(2) - 2 * pairs;
            
            res = count(0) + pairs + (triples + 2) / 3;
        } else {
            int c1 = count(1);
            int c2 = count(2);
            int c3 = count(3);
            
            if (c1 > c3) {
                swap(c1, c3);
            }
            
            res = count(0) + c1 + c2 / 2 + (c3 - c1 + 2 * (c2 % 2) + 3) / 4;
        }
        
        
        printf("%d\n", res);
    }
    
    
    return 0;
}
