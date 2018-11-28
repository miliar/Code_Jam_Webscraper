#include <bits/stdc++.h>
using namespace  std;

#define bits(a)     __builtin_popcount(a)

#define PB          push_back
#define SIZE(x)     (int)x.size()
#define MP(x,y)     make_pair(x,y)
#define All(t)      (t).begin(),(t).end()
#define CLR(x,y)    memset(x,y,sizeof(x))
#define FOR(i,n,m)  for (int i = n; i <= m; i++)
#define ROF(i,n,m)  for (int i = n; i >= m; i--)

#define RI(x)       scanf ("%d", &(x))
#define RII(x,y)    RI(x),RI(y)
#define RIII(x,y,z) RI(x),RI(y),RI(z)

typedef long long ll;
typedef unsigned int ui;
typedef unsigned long long ull;

/***********************END OF DEFINE******************************/

const int mx = 28;

int t, r, c;
char s[mx][mx];

void solve() {
    for(int i = 0; i < r; i++) {
        for(int j = 0; j < c; j++) {
            if(s[i][j] != '?') {
                for(int k = j + 1; k < c; k++) {
                    if(s[i][k] == '?') s[i][k] = s[i][j];
                    else break;
                }
                for(int k = j - 1; k >= 0; k--) {
                    if(s[i][k] == '?') s[i][k] = s[i][j];
                    else break;
                }
            }
        }
    }
    for(int i = 0; i < r; i++) {
        if(s[i][0] != '?'){
            for(int k = i - 1; k >= 0; k--) {
                if(s[k][0] == '?'){
                    for(int j = 0; j < c; j++)
                        s[k][j] = s[i][j];
                }
                else break;
            }
            for(int k = i + 1; k < r; k++) {
                 if(s[k][0] == '?'){
                    for(int j = 0; j < c; j++)
                        s[k][j] = s[i][j];
                }
                else break;
            }
        }
    }
}

int main(){
    freopen("A-large.in", "r", stdin);
    freopen("out", "w", stdout);

    cin >> t;
    for (int cs = 1; cs <= t; cs ++){
        cin >> r >> c;
        for(int i = 0; i < r; i++) scanf("%s", s[i]);
        solve();
        printf("Case #%d:\n", cs);
        for(int i = 0; i < r; i++) printf("%s\n", s[i]);
    }
    return 0;
}
