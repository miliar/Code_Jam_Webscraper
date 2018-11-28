#include <iostream>
#include <cstring>
#include <cmath>
#include <string>
#include <queue>

using namespace std;

int T, K, bit, arr[2000], len;
string str;
typedef pair<int, int> ii;

void dfs(int x) {
    for (int i = 0; i <= len - K; i++) {
        int b = x;
        for (int j = i; j < i+K; j++) {
            b ^= (1 << j);
        }
        if (arr[b] == 0) {
            arr[b] = 1;
            dfs(b);
        }
    }
}



int bfs(int x, int y) {
    queue<ii> q;
    if (x == y) return 0;
    q.push(ii(x, 0));
    while(!q.empty()) {
        ii mm = q.front();
        q.pop();
        for (int i = 0; i <= len - K; i++) {
            int b = mm.first;
            for (int j = i; j < i+K; j++) {
                b ^= (1 << j);
            }
            if (b == y) return mm.second+1;
            q.push(ii(b, mm.second+1));
        }
    }
    return -1;
}




int main() {
    cin >> T;
    cout << T << endl;
    for (int ca = 1; ca <= T; ca++) {
        memset(arr, 0, sizeof(arr));
        cin >> str;
        cin >> K;
        bit = 0;
        len = str.length();
        int r = pow(2, len) - 1;
        for (int i = 0; i < len; i++) {
            if (str.at(i) == '+') {
                bit |= (1 << i);
            }
        }
        dfs(bit);
        if (arr[r] == 0) {
            cout << "Case #" << ca << ": " << "IMPOSSIBLE" << endl; 
            continue;
        }
        int res = bfs(bit, r);
        cout << "Case #" << ca << ": " << res << endl; 

    }
}