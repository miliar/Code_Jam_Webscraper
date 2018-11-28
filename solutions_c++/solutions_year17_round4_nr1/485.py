#include <iostream>
#include <cstdio>
#include <algorithm>
#include <string>
#include <vector>
#include <queue>
#include <set>
#include <map>
#include <climits>

using namespace std;

int main() {
    int T; cin >> T;
    for(int cs = 1; cs <= T; cs++) {
        cout << "Case #" << cs << ": ";
        int N, P; cin >> N >> P;
        vector<int> G(P, 0);
        for(int i = 0; i < N; i++) {
            int k; cin >> k;
            G[k % P]++;
        }
        if(P == 2) {
            int res = G[0];
            res += (G[1]+1)/2;
            cout << res << endl;
        }
        if(P == 3) {
            int res = G[0], m;
            m = min(G[1], G[2]);
            res += m;
            G[1] -= m;
            G[2] -= m;
            res += (G[1] + 2)/3;
            res += (G[2] + 2)/3;
            cout << res << endl;
        }
        if(P == 4) {
            int res = G[0];
            res += G[2]/2;
            G[2] -= (G[2]/2)*2;
            int m = min(G[1], G[3]);
            res += m;
            G[1] -= m;
            G[3] -= m;
            int dres = G[1] + G[3];
            if(G[2] >= 1 && dres >= 2) {
                res++;
                G[2]--;
                dres -= 2;
            }
            bool trail = false;
            if(G[2]) {
                res++;
                trail = true;
            }
            if(dres) {
                res += (dres/4);
                dres -= (dres/4)*4;
                if(!trail && dres > 0) {
                    res++;
                }
            }
            cout << res << endl;
        }
    }
    return 0;
}
