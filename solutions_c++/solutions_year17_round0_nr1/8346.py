#include <cstdio>
#include <queue>
#include <string>
#include <cstring>
#include <cmath>
#include <set>
#include <vector>
#include <algorithm>
#include <iostream>

using namespace std;

typedef long long ll;
typedef pair<int, int> P;

//int dir[] = { 0, -1, 0, 1, 0 };

int T = 0, K = 0;
string curr;

void turn(string &curr, int start) {
    for (int i = start; i < start + K; i++) {
        if (curr[i] == '-') curr[i] = '+';
        else                curr[i] = '-';
    }
}

int getMinNum() {
    int len = (int) curr.length();
    int flip = 0;
    for (int i = 0; i <= len - K; i++) {
        if (curr[i] != '+') {
            turn(curr, i);
            flip++;
        }
    }
    
    for (int i = len - K + 1; i < len; i++) {
        if (curr[i] != '+') {
            return -1;
        }
    }
    
    return flip;
}
int main() {
    freopen("1A_small.in", "r", stdin);
    
    scanf("%d\n", &T);
    for (int t = 1; t <= T; t++) {
        cin >> curr >> K;
        
        int res = getMinNum();
        if (res >= 0) printf("Case #%d: %d\n", t, res);
        else          printf("Case #%d: IMPOSSIBLE\n", t);
    }
    return 0;
}
