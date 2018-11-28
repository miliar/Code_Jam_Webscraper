#include<bits/stdc++.h>
using namespace std;

int p[1020], b[1020];
int pos[1020];
int pass[1020];

int main() {
    int T;
    cin >> T;
    for (int i = 0; i < T; i++) {
        memset(pos, 0, sizeof(pos));
        memset(pass, 0, sizeof(pass));
        int n, c, m;
        int mx = 0;
        cin >> n >> c >> m;
        for (int j = 0; j < m; j++) {
            cin >> p[j] >> b[j];
            pos[p[j]] ++;
            pass[b[j]] ++;
            if (pass[b[j]] > mx) 
                mx = pass[b[j]];
        }
        int s = mx;
        while (1) {
            int u = 0;
            int v = 0;
            for (int j = n; j > 0; j--) {
                u += pos[j];
                if (pos[j] > s)
                    v += pos[j] - s;
                u -= s; 
                if (u < 0)
                    u = 0;
            }
            if (u == 0) {
                cout << "Case #" << i+1 << ": " << s << " " << v << endl;
                break;
            }
            s++;
        }
    }
    return 0;
}
