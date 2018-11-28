#include <vector>
#include <list>
#include <map>
#include <set>
#include <deque>
#include <stack>
#include <bitset>
#include <algorithm>
#include <functional>
#include <numeric>
#include <utility>
#include <sstream>
#include <iostream>
#include <iomanip>
#include <cstdio>
#include <cmath>
#include <cstdlib>
#include <ctime>
#include <cstring>
#include <queue>
#include <cassert>
#include <unordered_map>
#include <fstream>
#define ll long long
#define F first
#define S second
#define MOD 1000000007
#define MAX 200001
#define BUGGY 0
using namespace std;
string grid[101];
bool orig[101][101];
int n, m;
void solve() {
    memset(orig, true, sizeof orig);
    for (int i = 1;i <= n; ++i) {
        for (int j = 0;j < m; ++j) {
            if (grid[i][j] != '?' && orig[i][j]) {
                int le = j, r = j;
                for (int k = j + 1;k < m; ++k)
                    if (grid[i][k] == '?') grid[i][k] = grid[i][j], r = k, orig[i][k] = false;
                    else break;
                for (int k = j - 1;k >= 0; --k)
                    if (grid[i][k] == '?') grid[i][k] = grid[i][j], le = k, orig[i][k] = false;
                    else break;
                //if (grid[i][j] == 'C') cout << le << " " << r << "..\n";
                for (int k = i - 1;k >= 1; --k) {
                    bool tr = true;
                    for (int l = le;l <= r && true; ++l) {
                        tr &= (grid[k][l] == '?');
                    }
                    if (tr) {
                        for (int l = le;l <= r && true; ++l) grid[k][l] = grid[i][j], orig[k][l] = false;
                    } else break;
                }
                for (int k = i + 1;k <= n; ++k) {
                    bool tr = true;
                    for (int l = le;l <= r && true; ++l) {
                        tr &= (grid[k][l] == '?');
                    }
                    if (tr) {
                        for (int l = le;l <= r && true; ++l) grid[k][l] = grid[i][j], orig[k][l] = false;
                    } else break;
                }
            }
        }
    }
    
//    for (int i = 1;i <= n; ++i)
//        for (int j = 0;j < m; ++i) assert(grid[i][j] != '?');
}
int main(){
    ifstream cin("/Users/shikhar.s/Downloads/A-large.in");
    //ifstream cin("/Users/shikhar.s/Desktop/Competitive/Competitive/a.txt");
    ofstream cout("/Users/shikhar.s/Desktop/Competitive/Competitive/b.txt");
    int t;
    cin >> t;
    int T = 1;
    while (t--) {
        cin >> n >> m;
        for (int i = 1;i <= n; ++i) cin >> grid[i];
        cout << "Case #" << T++ << ":\n";
        solve();
        for (int i = 1;i <= n; ++i) cout << grid[i] << "\n";
    }
    printf("Done!");
    return 0;
}

