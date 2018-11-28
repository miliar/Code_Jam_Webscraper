#include <iostream>
#include <string>
#include <sstream>
#include <vector>
#include <algorithm>
#include <map>
#include <cstdlib>
#include <cstdio>
#include <complex>
#include <queue>
#include <stack>
using namespace std;
typedef long long unsigned int ll;

#define REP(i,n) for(int i=0; i<(int)n; i++)
#define rep(n) REP(i,n)
#define EPS (1e-7)
#define INF 1e9
#define PI (acos(-1))

const int MAXN = 108;
char G[MAXN][MAXN];
char G_ori[MAXN][MAXN];
int N;

int res;
int res_m;
vector<char> res_type;
vector<int> res_ii;
vector<int> res_jj;

bool check_G() {
    int cnt;
    // row
    for(int i = 0; i < N; ++i) {
        cnt = 0;
        for(int j = 0; j < N; ++j) {
            if(G[i][j] == 'x' || G[i][j] == 'o') ++cnt;
            if(cnt > 1) return false;
        }
    }
    // col
    for(int j = 0; j < N; ++j) {
        cnt = 0;
        for(int i = 0; i < N; ++i) {
            if(G[i][j] == 'x' || G[i][j] == 'o') ++cnt;
            if(cnt > 1) return false;
        }
    }
    // diag
    for(int k = 0; k < N; ++k) {
        cnt = 0;
        for(int i = 0, j = k; i < N && j < N; ++i, ++j) {
            if(G[i][j] == '+' || G[i][j] == 'o') ++cnt;
            if(cnt > 1) return false;
        }
        cnt = 0;
        for(int i = k, j = 0; i < N && j < N; ++i, ++j) {
            if(G[i][j] == '+' || G[i][j] == 'o') ++cnt;
            if(cnt > 1) return false;
        }
    }
    // diag
    for(int k = 0; k < N; ++k) {
        cnt = 0;
        for(int i = 0, j = k; i < N && j >= 0; ++i, --j) {
            if(G[i][j] == '+' || G[i][j] == 'o') ++cnt;
            if(cnt > 1) return false;
        }
        cnt = 0;
        for(int i = k, j = N-1; i < N && j >= 0; ++i, --j) {
            if(G[i][j] == '+' || G[i][j] == 'o') ++cnt;
            if(cnt > 1) return false;
        }
    }
    return true;
}

int main() {
    int T,tt = 0;
    cin>>T;
    while(tt++ < T) {
        // initialize
        res = res_m = 0; res_type.clear(); res_ii.clear(); res_jj.clear();
        fill((char *)G, (char *)(G+MAXN), '.');
        fill((char *)G_ori, (char *)(G_ori+MAXN), '.');
        int M; cin>>N>>M;
        for(int i = 0; i < M; ++i) {
            char type;
            int ii,jj;
            cin>>type>>ii>>jj; --ii; --jj;
            G[ii][jj] = type;
            G_ori[ii][jj] = type;
        }

        // fill '+'
        for(int i = 0, icnt = 0; icnt < N; i = N-i, ++icnt) {
            if(i>(N-1)/2) --i;
            // cout << "! " << i << endl;
            for(int j = 0, jcnt = 0; jcnt < N; j = N-j, ++jcnt) {
                if(j>(N-1)/2) --j;
                // cout << "! " << j << endl;
                if(G[i][j] != '.') {
                    continue;
                }
                else {
                    G[i][j] = '+';
                    if(!check_G()) {
                        G[i][j] = '.';
                    }
                }
            }
        }

        // fill 'x'
        int is_xo = -1;
        for(int j = 0; j < N; ++j) {
            if(G[0][j] == 'x' || G[0][j] == 'o') {
                is_xo = j;
            }
        }
        if(is_xo >= 0) {
            int j = is_xo;
            if(G[0][j] == 'x') {
                G[0][j] = 'o'; // replace
            }
            for(int i = 1; i < N; ++i) {
                j = (j + 1) % N;
                G[i][j] = 'x';
                if(i == N-1) {
                    G[i][j] = 'o';
                    if(!check_G()) {
                        G[i][j] = 'x';
                    }
                }
            }
        }
        else {
            // int i = N-2;
            int i = N-1;
            for(int j = 0; j < N; ++j) {
                if(G[i][j] == '+') {
                    G[i][j] = 'o'; // replace ?
                }
                else if(G[i][j] == '.') {
                    G[i][j] = 'x';
                    // debug
                    if(!check_G()) {
                        cout << "!!!!! something is wrong" << endl;
                    }
                    // end debug
                }
                i = (i + 1) % N;
            }
        }

        // debug
        // cout << "/////////" << endl;
        // for(int i = 0; i < N; ++i) {
        //     for(int j = 0; j < N; ++j) {
        //         cout << G[i][j] << " ";
        //     }
        //     cout << endl;
        // }
        // cout << "/////////" << endl;
        // end debug

        // evaluation
        for(int i = 0; i < N; ++i) {
            for(int j = 0; j < N; ++j) {
                if(G[i][j] == 'o') res += 2;
                else if(G[i][j] == 'x' || G[i][j] == '+') res += 1;
            }
        }

        // diff
        for(int i = 0; i < N; ++i) {
            for(int j = 0; j < N; ++j) {
                if(G[i][j] != G_ori[i][j]) {
                    res_type.push_back(G[i][j]);
                    res_ii.push_back(i);
                    res_jj.push_back(j);
                    ++res_m;
                }
            }
        }

        // print result
        cout << "Case #" << tt << ": " << res << " " << res_m << endl;
        for(int i = 0; i < res_m; ++i) {
            cout << res_type[i] << " " << (res_ii[i] + 1) << " " << (res_jj[i] + 1) << endl;
        }
    }
    return 0;
}
