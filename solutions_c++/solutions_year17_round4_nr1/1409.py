#pragma comment (linker, "/STACK:128000000")
#include <iostream>
#include <cstdio>
#include <fstream>
#include <functional>
#include <set>
#include <map>
#include <vector>
#include <queue>
#include <stack>
#include <cmath>
#include <algorithm>
#include <cstring>
#include <bitset>
#include <ctime>
#include <sstream>
#include <stack>
#include <cassert>
#include <list>
#include <deque>

using namespace std;

#define mp make_pair
#define pb push_back
#define all(a) a.begin(), a.end()

typedef long long li;
typedef long long i64;
typedef pair <int, int> pi;
typedef vector <int> vi;
typedef double ld;
typedef vector<int> vi;
typedef pair <int, int> pi;

void solve();

//int timer = 0;
#define FILENAME ""

int main() {
    string s = FILENAME;
#ifdef YA
    //assert(!s.empty());
    freopen("input.txt", "r", stdin);
    freopen("output.txt", "w", stdout);
    //cerr<<FILENAME<<endl;
    //assert (s != "change me please");
    clock_t start = clock();
#else
    //freopen("input.txt", "r", stdin);
    //freopen("output.txt", "w", stdout);
    //freopen(FILENAME ".in", "r", stdin);
    //freopen(FILENAME ".out", "w", stdout);
    cin.tie(0);
#endif
    cout.sync_with_stdio(0);
    cout.precision(10);
    cout << fixed;
    int t = 1;
    
    cin >> t;
    for (int i = 1; i <= t; ++i) {
        //++timer;
        cout << "Case #" << i << ": ";
        solve();
    }
#ifdef YA
    cerr << "\n\n\n" << (clock() - start) / 1.0 / CLOCKS_PER_SEC << "\n\n\n";
#endif
    return 0;
}

int dp[101][101][101][101][4];

void solve() {
    int n, p;
    cin >> n >> p;
    vector <int> numbers(n);
    
    vector <int> g(4);
    
    for (int i = 0; i < n; ++i) {
        cin >> numbers[i];
        numbers[i] %= p;
        g[numbers[i]]++;
    }
    
    for (int i0 = 0; i0 <= g[0]; ++i0) {
        for (int i1 = 0; i1 <= g[1]; ++i1) {
            for (int i2 = 0; i2 <= g[2]; ++i2) {
                for (int i3 = 0; i3 <= g[3]; ++i3) {
                    for (int rest = 0; rest < p; ++rest) {
                        dp[i0][i1][i2][i3][rest] = -1;
                    }
                }
            }
        }
    }
    for (int i = 0; i < 4; ++i) {
        cerr << g[i] << " ";
    }
    cerr << endl;
    
    dp[g[0]][g[1]][g[2]][g[3]][0] = 0;
    
    int ans = 0;
    
    vector <int> new_i(4);
    for (int sum_all = n; sum_all >= 1; --sum_all) {
        for (int rest = 0; rest < p; ++rest) {
            vector <int> i(4);
            for (i[1] = 0; i[1] <= min(g[1], sum_all); ++i[1]) {
                for (i[2] = 0; i[2] <= min(g[2], sum_all - i[1]); ++i[2]) {
                    for (i[3] = 0; i[3] <= min(g[3], sum_all - i[1] - i[2]); ++i[3]) {
                        i[0] = sum_all - i[1] - i[2] - i[3];
                        if (i[0] < 0 || i[0] > g[0]) {
                            continue;
                        }
                        if (dp[i[0]][i[1]][i[2]][i[3]][rest] == -1) {
                            continue;
                        }
                        for (int j = 0; j < 4; ++j) {
                            if (i[j] == 0) {
                                continue;
                            }
                            for (int t = 0;t < 4; ++t) {
                                new_i[t] = i[t];
                            }
                            new_i[j]--;
                            int new_val =dp[i[0]][i[1]][i[2]][i[3]][rest] + int(rest == 0);
                            int new_rest = ((rest - j) + p) % p;
                            int to_upd = dp[new_i[0]][new_i[1]][new_i[2]][new_i[3]][new_rest];
                            if (to_upd == -1 || to_upd < new_val) {
                                dp[new_i[0]][new_i[1]][new_i[2]][new_i[3]][new_rest] = new_val;
                                ans = max(ans, new_val);
                            }
                        }
                    }
                }
            }
        }
    }
    
    cout << ans << "\n";
}
