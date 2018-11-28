#include <bits/stdc++.h>
#define ff first
#define ss second
#define mp make_pair
#define var(x) cerr << #x << " = " << x << endl;

using namespace std;

typedef long long ll;
typedef pair<int,int> pii;

int v[1111][1111], k[1111];

// case c == 2
int main() {
    int N;
    cin >> N;
    for(int t=1;t<=N;t++) {
        int n, m, c, p, b;
        cin >> n >> c >> m;
        memset(v,0,sizeof(v));
        memset(k,0,sizeof(k));
        for(int i=0;i<m;i++) {
            cin >> p >> b;
            v[b][p]++;
            k[b]++;
        }
        int y = max(k[1],k[2]);
        int z = 0;
        if(v[1][1]+v[2][1] > y) {
            y = v[1][1]+v[2][1];
        } else {
            for(int i=1;i<=n;i++) {
                if(v[1][i] + v[2][i] > y) {
                    z += (v[1][i] + v[2][i] - y);
                }
            }
        }
        printf("Case #%d: %d %d", t, y, z);
        cout << endl;
    }
    return 0;
}

