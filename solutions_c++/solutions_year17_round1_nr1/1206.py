#include <cstdio>
#include <algorithm>
#include <iostream>
#include <cmath>
#include <vector>
#include <cstring>
#include <map>
#include <set>
#include <unordered_map>
#include <queue>
#include <sstream>
#include <iomanip>
using namespace std;

//#pragma comment(linker, "/STACK:102400000,102400000")

typedef long long ll;
typedef pair<int, int> pii;
typedef pair<int, double> pid;
typedef pair<ll, ll> pll;

int R, C;

char s[30][30];

bool v[30];

void solve() {
    cin >> R >> C;
    for (int i = 0; i < R; ++i)
        scanf("%s", s[i]);
    
    for (int i = 0; i < R; ++i) {
        v[i] = false;
    }
    
    bool preEmpty = false;
    
    int lastNoEmptyRow = -1;
    
    for (int i = 0; i < R; ++i) {
        bool isRowEmpty = true;
        for (int j = 0; j < C; ++j) {
            if (s[i][j] != '?') {
                isRowEmpty = false;
                break;
            }
        }
        v[i] = isRowEmpty;
        if (isRowEmpty) {
            preEmpty = true;
            continue;
        }
        
        lastNoEmptyRow = i;
        
        bool isFirst = true;
        for (int j = 0; j < C; ++j) {
            if (s[i][j] == '?') {
                continue;
            }
            
            if (isFirst) {
                isFirst = false;
                for (int k = j-1; k >= 0; --k) {
                    if (s[i][k] != '?') {
                        break;
                    } else {
                        s[i][k] = s[i][j];
                    }
                }
            }
            
            for (int k = j+1; k < C; ++k) {
                if (s[i][k] != '?') {
                    break;
                } else {
                    s[i][k] = s[i][j];
                }
            }
        }
        
        for (int j = i-1; j >= 0; --j) {
            if (v[j]) {
                for (int k = 0; k < C; ++k) {
                    s[j][k] = s[i][k];
                }
            } else {
                break;
            }
        }
    }
    
    for (int i = lastNoEmptyRow+1; i < R; ++i) {
        for (int j = 0; j < C; ++j) {
            s[i][j] = s[lastNoEmptyRow][j];
        }
    }
    
    for (int i = 0; i < R; ++i) {
        printf("%s\n", s[i]);
    }
}

int main() {
    
    //freopen("/Users/zyeric/Desktop/workspace/workspace/in.txt", "r", stdin);
    
    ios::sync_with_stdio(false);
    cout << fixed << setprecision(16);
    
    int T;
    cin >> T;
    
    for (int kase = 1; kase <= T; ++ kase) {
        cout << "Case #" << kase << ": " << endl;
        solve();
        cerr << "solved " << kase << endl;
    }
    
    return 0;
}
