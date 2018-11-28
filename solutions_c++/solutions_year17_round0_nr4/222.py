#include <cstdio>
#include <cstdlib>
#include <stack>
#include <algorithm>
#include <cmath>
#include <cstring>
#include <queue>
#define ll long long
#define N 111111
#define md 100000000
#define PI 2*acos(0.0)
using namespace std;

bool u[111][111], a[111][111], b[111][111], r[111][2];

int n, m;
bool p(pair<int, int> u, pair<int, int> v){
    int du = abs(2 * u.first - (n + 1)) + abs(2 * u.second - (n + 1)), dv = abs(2 * v.first - (n + 1)) + abs(2 * v.second - (n + 1));
    return du > dv;
}

void solve(){
    scanf("%d%d\n", &n, &m);
    memset(u, 0, sizeof u);
    memset(a, 0, sizeof a);
    memset(b, 0, sizeof b);
    memset(r, 0, sizeof r);
    for(int i = 0; i < m; i++){
        char c; int p, q;
        scanf("%c%d%d\n", &c, &p, &q);
        if(c == 'o' || c == 'x') a[p][q] = true, r[p][0] = true, r[q][1] = true;
        if(c == 'o' || c == '+') b[p][q] = true;
    }
    int up = 0, sc = 0;
    
    // vertical and horizontal
    for(int i = 1, j = 1; i <= n && j <= n; i++){
        if(r[i][0]) continue;
        while(r[j][1]) j++;
        u[i][j] = true, a[i][j] = true;
        j++;
    }
    // diagonal
    pair<int, int> q[11111];
    for(int i = 1, k = 0; i <= n; i++) for(int j = 1; j <= n; j++, k++) q[k].first = i, q[k].second = j;
    sort(q, q + n*n, p);
    for(int k = 0; k < n * n; k++){
        int i = q[k].first, j = q[k].second;
        if(b[i][j]) continue;
        bool place = true;
        for(int r = 1; i - r >= 1 && j - r >= 1; r++) if(b[i - r][j - r]) place = false;
        for(int r = 1; i - r >= 1 && j + r <= n; r++) if(b[i - r][j + r]) place = false;
        for(int r = 1; i + r <= n && j - r >= 1; r++) if(b[i + r][j - r]) place = false;
        for(int r = 1; i + r <= n && j + r <= n; r++) if(b[i + r][j + r]) place = false;
        if(!place) continue;
        u[i][j] = true, b[i][j] = true;
    }
    
    for(int i = 1; i <= n; i++)
        for(int j = 1; j <= n; j++){
            if(a[i][j]) sc++;
            if(b[i][j]) sc++;
            if(u[i][j]) up++;
        }
    printf("%d %d\n", sc, up);
    for(int i = 1; i <= n; i++)
        for(int j = 1; j <= n; j++)
            if(u[i][j]) printf("%c %d %d\n", a[i][j] ? (b[i][j] ? 'o' : 'x') : (b[i][j] ? '+' : '?'),  i, j);
}

int main(){
    
    int t;
    scanf("%d", &t);
    for(int s = 1; s <= t; s++){
        printf("Case #%d: ", s);
        solve();
    }
    
    return 0;
}
