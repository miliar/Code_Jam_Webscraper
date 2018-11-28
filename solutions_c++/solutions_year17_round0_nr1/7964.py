#include <array>
#include <cassert>
#include <cmath>
#include <cstdio>
#include <cstring>
#include <functional>
#include <string>
#include <vector>
#include <queue>
#include <map>
#include <set>
#include <algorithm>
#include <iostream>
#include <sstream>
using namespace std;

#define REP(i, n) for(int i = 0; i < (int)(n); ++ i)
#define FOR(i, b, e) for(auto i = b; i < e; ++ i)
#define all(x) (x).begin(), (x).end()

string S; int K;
int go()
{
    int n = S.length();
    int ret = 0;
    for(int i=0; i<n-K+1; ++i)
    {
        if(S[i] == '-') {
            for(int j=0; j<K; ++j) S[i+j] = '+' + '-' - S[i+j];
            ret ++;
        }
    }
    //cout << S << endl;
    for(int i=0; i<n; ++i) {
        if(S[i] == '-')
            return -1;
    }
    return ret;
}

int main() {
    int T;
    cin >> T;
    for(int kase = 1; kase <= T; ++kase) {
        cin >> S; cin >> K;
        printf("Case #%d: ", kase);
        int t = go();
        if(t == -1)
            printf("IMPOSSIBLE\n");
        else printf("%d\n", t);
    }
    return 0;
}
