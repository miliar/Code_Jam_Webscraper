#include <cstdio>
#include <queue>
#include <string>
#include <cstring>
#include <cmath>
#include <set>
#include <vector>
#include <iostream>
#include <map>
#include <algorithm>

using namespace std;

typedef long long ll;
typedef pair<int, int> P;

int T, N;
int num[6] = {};
char unicorn[] = "ROYGBV";

string solve() {
    string res(N, 'a');
    
    int head = -1;
    int prev = -1;
    for (int i = 0; i < N; i++) {
        int currMax = -1;
        for (int u = 0; u < 6; u++) {
            int ci = u;
            if (i > 0) {
                ci = head + u;
                if (ci >= 6) ci -= 6;
            }
            if (ci != prev && num[ci] > 0 && (currMax == -1 || num[ci] > num[currMax])) {
                currMax = ci;
            }
        }
        if (currMax == -1) {
            return "IMPOSSIBLE";
        }
        if (i == 0) {
            head = currMax;
        }
        num[currMax]--;
        prev = currMax;
        res[i] = unicorn[currMax];
    }
    
    if (res[N-1] == res[0]) return "IMPOSSIBLE";

    return res;
}


int main() {
    freopen("1b.in", "r", stdin);
    
    scanf("%d\n", &T);
    
    for (int t = 1; t <= T; t++) {
        scanf("%d", &N);
        
        for (int i = 0; i < 6; i++) {
            scanf("%d", &num[i]);
        }
        
        printf("Case #%d: ", t);
        cout << solve() << endl;
    }
    
    return 0;
}
