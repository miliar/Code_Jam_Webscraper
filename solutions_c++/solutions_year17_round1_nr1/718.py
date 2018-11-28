#include <bits/stdc++.h>

#define MN 1001000
#define w1 while(1)
#define debug(a) cout << a << endl
#define pb push_back
#define mp make_pair

using namespace std;
typedef long long ll;

int n, empty_[26], fst_r = -1, t, R, C;
char grid[26][26], fst[26];

int main() {
    freopen("A-large__.in", "r", stdin);
    freopen("A-large__.out", "w", stdout);

    scanf("%d",&t);


    for(int T=1; T<=t; T++) {
        memset(empty_, 0, sizeof empty_);
        fst_r = -1;
        scanf("%d %d",&R, &C);

        for(int i=0;i<R;i++) {
            scanf("%s", grid[i]);

            empty_[i] = 1;
            for(int j=0;j<C;j++) {
                if(grid[i][j] != '?' && empty_[i] == 1) {
                    empty_[i] = 0;
                    fst[i] = grid[i][j];
                }
            }
        }

        for(int i=0;i<R;i++) {
            if(empty_[i] == 1) continue;
            if(fst_r == -1) fst_r = i;

            char last = fst[i];
            for(int j=0;j<C;j++) {

                if(grid[i][j] == '?') {
                    grid[i][j] = last;
                }
                else {
                    last = grid[i][j];
                }
            }
        }

        assert(fst_r != -1);
        int last = fst_r;
        for(int i=0;i<R;i++) {
            if(empty_[i] == 0) {
                last = i;
                continue;
            }

            for(int j=0;j<C;j++) {
                grid[i][j] = grid[last][j];
            }
        }

        printf("Case #%d:\n", T);
        for(int i=0;i<R;i++) {
            printf("%s\n", grid[i]);
        }
    }
    return 0;
}

/*
A*
**
*B


*/
