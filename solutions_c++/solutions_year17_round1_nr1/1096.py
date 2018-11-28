#include <iostream>
#include <fstream>
#include <algorithm>
#include <vector>
#include <unordered_map>
#include <stack>
#include <queue>
#include <set>
#include <cstdio>
#include <cstring>
#include <cmath>
#include <climits>
#include <cfloat>
#include <cstdlib>

using namespace std;

#define pb push_back
#define mp make_pair
#define fs first
#define sc second

#define ri(X) scanf("%d", &(X))
#define rii(X, Y) scanf("%d%d", &(X), &(Y))
#define riii(X, Y, Z) scanf("%d%d%d", &(X), &(Y), &(Z))
#define all(a) (a).begin(),(a).end()

#define INF 0x3f3f3f3f
#define INFL 0x3f3f3f3f3f3f3f3fLL

typedef pair<int,int> pii;
typedef vector<int> vi;
typedef long long ll;

int mod1 = int(1e9) + 7;

char b[30][30];

int main(){

    int t;
    ri(t);

    for(int cas=1; cas<=t; cas++) {

        int r,c;
        rii(r,c);

        for(int i=0; i<r; i++) 
            scanf("%s", b[i]);

        int lr = -1;
        for(int rr=0; rr<r; rr++) {
            int lc = -1;
            for(int cc=0; cc<c; cc++) {
                if(b[rr][cc]!='?') {
                    for(int r2=rr; r2>lr; r2--)
                        for(int c2=cc; c2>lc; c2--)
                            b[r2][c2] = b[rr][cc];
                    lc = cc;
                }
            }
            if(lc>=0) lr = rr;
        }

        for(int rr=0; rr<r; rr++) 
            for(int cc=1; cc<c; cc++) 
                if(b[rr][cc]=='?')
                    b[rr][cc] = b[rr][cc-1];

        for(int cc=0; cc<c; cc++) 
            for(int rr=1; rr<r; rr++) 
                if(b[rr][cc]=='?')
                    b[rr][cc] = b[rr-1][cc];

        printf("Case #%d: \n", cas);
        for(int rr=0; rr<r; rr++) 
            printf("%s\n", b[rr]);
    }

    return 0;
}
