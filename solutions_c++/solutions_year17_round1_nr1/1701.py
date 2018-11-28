#include <cassert>
#include <iostream>
#include <vector>
#include <map>
#include <set>
#include <bitset>
#include <list>
#include <stack>
#include <queue>
#include <deque>
#include <string>
#include <sstream>
#include <algorithm>
#include <cstdio>
#include <cstring>

#define ff first
#define ss second
#define pb push_back
#define sz size

#define ms(x,v) memset((x), (v), sizeof(x))

using namespace std;

typedef long long L;
typedef unsigned long long UL;
typedef double D;
typedef pair<L,L> PL;
typedef vector<L> VL;
typedef vector<VL> VVL;
typedef vector<PL> VPL;
typedef vector<VPL>VVPL;

#define _NO_USE_LOG
#ifdef _USE_LOG
#define ASSERT(x) assert(x)
#define LOG(x) cout << x;
#else
#define ASSERT(x)
#define LOG(x)
#endif

const int MAXN = 30;

int r, c;
char mat[MAXN][MAXN];

void fill_l() {
    char curr;
    for(int i = 0; i < r; ++i) {
        curr = '?';
        for(int j = 0; j < c; ++j) {
            if(mat[i][j] == '?') mat[i][j] = curr;
            else curr = mat[i][j];
        }
    }
}

void fill_r() {
    char curr;
    for(int i = 0; i < r; ++i) {
        curr = '?';
        for(int j = c - 1; j >= 0; --j) {
            if(mat[i][j] == '?') mat[i][j] = curr;
            else curr = mat[i][j];
        }
    }
}

void fill_b() {
    int b, e;
    char curr;
    bool bork;
    for(int i = 1; i < r; ++i) {
        b = e = 0;
        while(b < c) {
            curr = mat[i - 1][b];
            bork = false;
            for(e = b; e < c && mat[i-1][e] == curr; ++e) {
                if(mat[i][e] != '?') {
                    bork = true;
                }
            }
            if(!bork) for(int j = b; j < e; ++j) mat[i][j] = curr;

            b = e;
        }
    }
}

void fill_u() {

    int b, e;
    char curr;
    bool bork;
    for(int i = r - 2; i >= 0; --i) {
        b = e = 0;
        while(b < c) {
            curr = mat[i + 1][b];
            bork = false;
            for(e = b; e < c && mat[i + 1][e] == curr; ++e) {
                if(mat[i][e] != '?') {
                    bork = true;
                }
            }
            if(!bork) for(int j = b; j < e; ++j) mat[i][j] = curr;

            b = e;
        }
    }
}

int main() {
    ios_base::sync_with_stdio(0);
    cin.tie(0);

    int t;
    cin >> t;
    for(int i = 1; i <= t; ++i) {
        cout << "Case #" << i << ":\n";
        cin >> r >> c;
        for (int i = 0; i < r; ++i)
            for(int j = 0; j < c; ++j)
                cin >> mat[i][j];
        fill_l();fill_r();
        fill_b(); fill_u();
        for (int i = 0; i < r; ++i) {
            for(int j = 0; j < c; ++j){
                ASSERT(mat[i][j] != '?');
                cout << mat[i][j];
            }
            cout << '\n';
        }
    }
}
