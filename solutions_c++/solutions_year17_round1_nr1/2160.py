/**********************************************
            Author : smiley007  
***********************************************/

//Data Structure Includes
#include <vector>
#include <queue>
#include <deque>
#include <bitset>
#include <stack>
#include <list>
#include <set>          
#include <map>
#include <unordered_set>

//Other Includes
#include <cstdio>
#include <string>
#include <cstring>
#include <cstdlib>
#include <iostream>
#include <cmath>
#include <cctype>
#include <cassert>
#include <numeric>
#include <algorithm>
#include <ctime>
#include <sstream>
#include <climits>
#include <iomanip>

using namespace std ;
typedef long long ll;
typedef pair<int,int> pii;
typedef pair<ll,ll> pll;
typedef vector<int> vi;
typedef vector<ll> vll;
typedef vector<vll> vvll;
typedef vector<vvll> vvvll;
typedef vector<pii> vpii;
typedef vector<vpii> vvpii;
typedef vector<vpii> vvpii;
typedef vector<pll> vpll;
typedef vector<vpll> vvpll;
typedef vector<vvpll> vvvpll;
typedef vector<vi> vvi;
typedef vector<string> vs;
typedef vector<vs> vvs;

#ifdef LocalHost
    #define eprintf(...) fprintf(stderr,__VA_ARGS__)
#endif

//Code Begins Here ------ >>>
const int N = 30;
char mat[N][N];
vi g[N];
int r, c;
int t, tt = 1;


void solve() {
    cin >> r >> c;
    for (int i = 0; i < N; i++) g[i].clear();
    for (int i = 0; i < r; i++) {
        for (int j = 0; j < c; j++) {
            cin >> mat[i][j];
            if (mat[i][j] != '?') {
                g[j].push_back(i);
            }
        }
    }
    int end = 0;
    for (int i = c - 1; i >= 0; i--)    if (!g[i].empty()) {
        end = i;
        break;
    }
    int idx = 0, lst = 0;
    while (lst < c) {
        while (lst < c && g[lst].empty())  lst++;
        if (lst < c) {
            int sz = g[lst].size();
            int st = 0;
            char cr;
            int en = lst;
            if (lst == end) en = c - 1;
            for (int j = 0; j < sz; j++) {
                for (int a = st; a <= g[lst][j]; a++) {
                    for (int b = idx; b <= en; b++) {
                        mat[a][b] = mat[g[lst][j]][lst];
                    }
                }
                st = g[lst][j] + 1;
            }
            cr = mat[g[lst][sz - 1]][lst];
            for (int a = st; a < r; a++) {
                for (int b = idx; b <= en; b++) {
                    mat[a][b] = cr;
                }
            }
            idx = lst + 1;
            lst++;
            if (en == c - 1)    break;
        }
    }
    for (int i = 0; i < r; i++) {
        for (int j = 0; j < c; j++) {
            cout << mat[i][j];
        }
        cout << "\n";
    }
}

int main(){
    #ifdef LocalHost
        freopen("input.txt","r",stdin);
        freopen("output.txt","w",stdout);
    #endif

    
    scanf("%d", &t);
    while (tt <= t) {
        cout << "Case #" << tt << ": \n" ;
        solve();
        tt++;
    }





    

    return 0;
}