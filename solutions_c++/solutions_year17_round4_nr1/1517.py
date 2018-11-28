#define _ijps 01
#define _CRT_SECURE_NO_DEPRECATE
//#pragma comment(linker, "/STACK:667772160")
#include <iostream>
#include <cmath>
#include <vector>
#include <time.h>
#include <map>
#include <set>
#include <deque>
#include <cstdio>
#include <cstdlib>
#include <unordered_map>
#include <unordered_set>
#include <bitset>
#include <algorithm>
#include <string>
#include <fstream>
#include <assert.h> 
#include <list>
#include <cstring>
#include <queue>
using namespace std;

#define name ""

typedef long long ll;

struct __isoff {
    __isoff() {
        if(_ijps)
            freopen("input.txt", "r", stdin), freopen("output.txt", "w", stdout);//, freopen("test.txt", "w", stderr);
        //else freopen(name".in", "r", stdin), freopen(name".out", "w", stdout);
        //ios_bsume::sync_with_stdio(0);
        //srand(time(0));
        srand('C' + 'T' + 'A' + 'C' + 'Y' + 'M' + 'B' + 'A');
    }
    ~__isoff() {
        //if(_ijps) cout<<times<<'\n';
    }
} __osafwf;

map<vector<int>, int> dp[10];
void operator delete(void *) {

}
int n, p;
int dfs(vector<int> W, int x = 0) {
    W.push_back(x);
    if(dp[p].count(W)) {
        return dp[p][W];
    }
    W.pop_back();
    int d = x == 0;
    int res = 0;
    for(int i = 0; i < W.size(); i++) {
        if(W[i] > 0) {
            W[i]--;
            res = max(res, dfs(W, (x + i) % p) + d);
            W[i]++;
        }
    }
    W.push_back(x);
    return dp[p][W] = res;
}

int main() {
    int tt;
    cin >> tt;
    for(int ii = 1; ii <= tt; ii++) {
        cerr << ii << '\n';
        cin >> n >> p;
        vector<int> W(p);
        for(int i = 0; i < n; i++) {
            int t;
            cin >> t;
            W[t % p]++;
        }
        printf("Case #%d: %d\n", ii, dfs(W));
    }
}