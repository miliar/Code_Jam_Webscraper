#include <iostream>
#include <iomanip>
#include <fstream>
#include <algorithm>
#include <queue>
#include <set>
#include <vector>
#include <map>
#include <cmath>
#include <valarray>

using namespace std;

typedef long long ll;
typedef unsigned long long ull;
typedef long double ld;
typedef pair<int, int> ii;
typedef pair<ii, int> iii;
typedef pair<ii, ii> pp;

const int CMAX = 1005;
const int INF = 2e9 + 5;

int a[CMAX][2];

int main() {
    
    freopen("/Users/Lukas/Desktop/in.txt", "r", stdin);
    freopen("/Users/Lukas/Desktop/out.txt", "w", stdout);
    
    int T;
    cin >> T;
    for (int t = 1; t <= T; t++) {
        cout << "Case #" << t << ": ";
        int n, c, m;
        cin >> n >> c >> m;
        for (int i = 0; i <= n; i++) { a[i][0] = 0; a[i][1] = 0; }
        for (int i = 0; i < m; i++) {
            int p, b;
            cin >> p >> b;
            a[p-1][b-1]++;
        }
        
        int res = 0;
        int promotions = 0;
        
        for (int i = 0; i < n; i++) {
            if (a[i][0] == 0 || a[i][1] == 0) continue;
            
            if (a[i][0] < a[i][1]) {
                for (int j = 0; j < n && a[i][0] > 0; j++) {
                    if (i == j || a[j][0] == 0 || a[j][1] == 0) continue;
                    int pp = min(a[i][0], a[j][1]);
                    a[i][0] -= pp;
                    a[j][1] -= pp;
                    res += pp;
                }
                
                for (int j = 0; j < n && a[i][0] > 0; j++) {
                    if (i == j || a[j][1] == 0) continue;
                    int pp = min(a[i][0], a[j][1]);
                    a[i][0] -= pp;
                    a[j][1] -= pp;
                    res += pp;
                }
            } else {
                for (int j = 0; j < n && a[i][1] > 0; j++) {
                    if (i == j || a[j][0] == 0 || a[j][1] == 0) continue;
                    int pp = min(a[i][1], a[j][0]);
                    a[i][1] -= pp;
                    a[j][0] -= pp;
                    res += pp;
                }
                
                for (int j = 0; j < n && a[i][1] > 0; j++) {
                    if (i == j || a[j][0] == 0) continue;
                    int pp = min(a[i][1], a[j][0]);
                    a[i][1] -= pp;
                    a[j][0] -= pp;
                    res += pp;
                }
            }
        }
        
        for (int i = 0; i < n; i++) {
            if (a[i][0] == 0 && a[i][1] == 0) continue;
            
            if (a[i][0] > 0 && a[i][1] > 0) {
                if (a[i][0] >= a[i][1]) {
                    for (int j = 0; j < n && a[i][0] > 0; j++) {
                        if (i == j || a[j][1] == 0) continue;
                        int pp = min(a[i][0], a[j][1]);
                        a[i][0] -= pp;
                        a[j][1] -= pp;
                        res += pp;
                    }
                } else {
                    for (int j = 0; j < n && a[i][1] > 0; j++) {
                        if (i == j || a[j][0] == 0) continue;
                        int pp = min(a[i][1], a[j][0]);
                        a[i][1] -= pp;
                        a[j][0] -= pp;
                        res += pp;
                    }
                }
            }
        }
        
        for (int i = 0; i < n; i++) {
            if (a[i][0] == 0 && a[i][1] == 0) continue;
            
            if (a[i][0] > 0) {
                for (int j = 0; j < n && a[i][0] > 0; j++) {
                    if (i == j || a[j][1] == 0) continue;
                    int pp = min(a[i][0], a[j][1]);
                    a[i][0] -= pp;
                    a[j][1] -= pp;
                    res += pp;
                }
            } else {
                for (int j = 0; j < n && a[i][1] > 0; j++) {
                    if (i == j || a[j][0] == 0) continue;
                    int pp = min(a[i][1], a[j][0]);
                    a[i][1] -= pp;
                    a[j][0] -= pp;
                    res += pp;
                }
            }
        }
        
        for (int i = 0; i < n; i++) {
            if (a[i][0] == 0 && a[i][1] == 0) continue;
            if (a[i][0] > 0 && a[i][1] > 0) {
                if (i == 0) {
                    res += a[i][0] + a[i][1];
                    a[i][0] = 0;
                    a[i][1] = 0;
                } else {
                    res += max(a[i][0], a[i][1]);
                    promotions += min(a[i][0], a[i][1]);
                    a[i][0] = 0;
                    a[i][1] = 0;
                }
            } else {
                res += max(a[i][0], a[i][1]);
                a[i][0] = 0;
                a[i][1] = 0;
            }
        }
        
        cout << res << " " << promotions << endl;
    }
    
    return 0;
}
