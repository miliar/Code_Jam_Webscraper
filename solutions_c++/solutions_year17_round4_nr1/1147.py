#include<bits/stdc++.h>

using namespace std;

#define mp(x,y) make_pair(x, y)
#define For(i, n) for (int i = 0; i < (int) n; i++)

typedef long long ll;
typedef vector<int> vi;
typedef pair<int, int> pii;
int p;

int solve(int mod, int r1, int r2, int r3, vector<vector<vector<vector<int> > > >& dynamic) {
    if (dynamic [mod][r1][r2][r3] != -1) return dynamic [mod][r1][r2][r3];
    if (r1 == 0 && r2 == 0 && r3 == 0) return 0;
    int mysol = 0;
    if (r1 > 0) {
        mysol = max(mysol, (mod == 0) + solve((mod + 1)%p, r1 - 1, r2, r3, dynamic));
    }
    if (r2 > 0) {
        mysol = max(mysol, (mod == 0) + solve((mod + 2)%p, r1, r2 - 1, r3, dynamic));
    }
    if (r3 > 0) {
        mysol = max(mysol, (mod == 0) + solve((mod + 3) % p, r1, r2, r3 - 1, dynamic));
    }
    dynamic [mod][r1][r2][r3] = mysol;
    return mysol;
}

int main () {
    int T;
    cin >> T;
    For(cases, T) {
        int n;
        cin >> n >> p;
        vector<int> groups(n);
        vector<int> bymod(4, 0);
        For(i, n) {
            cin >> groups [i];
            groups [i] %= p;
            bymod [groups [i]] ++; 
        }
        int result = bymod [0];
        vector<vector<vector<vector<int> > > > dynamic(p, vector<vector<vector<int> > > (n + 1, vector<vector<int> > (n + 1, vector<int> (n + 1, -1))));
        printf("Case #%d: %d\n", cases + 1, result + solve(0,bymod[1], bymod [2], bymod [3], dynamic));
    }
}
