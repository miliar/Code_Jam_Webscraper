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

int main(){

    int testcases;
    ri(testcases);

    char s[1010], t[10000];
    char c[3] = {'Y','B','R'};
    char c2[3] = {'V','O','G'};

    for(int cas=1; cas<=testcases; cas++) {
        printf("Case #%d: ", cas);

        c[0] = 'Y';
        c[1] = 'B';
        c[2] = 'R';

        int n,r,o,y,g,b,v;
        ri(n);
        riii(r,o,y);
        riii(g,b,v);

        /*
        if(y<b) {
            swap(y,b);
            swap(c[0],c[1]);
        }
        if(y<r) {
            swap(y,r);
            swap(c[0],c[2]);
        }
        if(b<r) {
            swap(b,r);
            swap(c[1],c[2]);
        }
        // y >= b >= r

        if(y>r+b) {
            printf("IMPOSSIBLE\n");
            continue;
        }

        memset(s,0,sizeof(s));

        s[0] = c[0];
        y--;
        int i = 1;
        while(y) {
            if(b>r) {
                s[i] = c[1];
                b--;
            } else {
                s[i] = c[2];
                r--;
            }
            i++;
            s[i] = c[0];
            y--;
            i++;
        }
        if(r>b) {
            s[i] = c[2];
            i++; r--;
            while(r>0) {
                s[i] = c[1]; i++;
                b--;
                s[i] = c[2]; i++;
                r--;
            }
        } else {
            s[i] = c[1];
            i++; b--;
            while(b>0) {
                s[i] = c[2]; i++;
                r--;
                s[i] = c[1]; i++;
                b--;
            }
        }

*/


        int yy=y-v,
            bb=b-o,
            rr=r-g;

//        yy=y; bb=b; rr=r;
        if(yy<bb) {
            swap(yy,bb);
            swap(v,o);
            swap(c[0],c[1]);
            swap(c2[0],c2[1]);
        }
        if(yy<rr) {
            swap(yy,rr);
            swap(v,g);
            swap(c[0],c[2]);
            swap(c2[0],c2[2]);
        }
        if(bb<rr) {
            swap(bb,rr);
            swap(o,g);
            swap(c[1],c[2]);
            swap(c2[1],c2[2]);
        }
//        // yy >= bb >= rr
//
//        if(y<=v || b<=o || r<=g
//                || yy>(bb+rr)) {
//            printf("IMPOSSIBLE\n");
//            continue;
//        }

        if(yy>(bb+rr)) {
            printf("IMPOSSIBLE\n");
            continue;
        }
        memset(s,0,sizeof(s));
        memset(t,0,sizeof(t));

        for(int i=0, yc=0; yc<yy; i+=4, yc++) {
            t[i] = c[0];
        }
        int i=2;
        for(int bc=0; bc<bb; i+=4, bc++) {
            t[i] = c[1];
        }
        int rc = 0;
        for(; rc<rr && t[i-2]; i+=4, rc++) {
            t[i] = c[2];
        }

        i=0;
        while(rc<rr) {
            if(t[i]==0) {
                t[i] = c[2];
                rc++;
            }
            i++;
        }

        int j=0, cc=0;
        for(i=0; cc<yy+rr+bb; i++) {
            if(t[i]) {
                s[j] = t[i];
                cc++;
                j++;

//                while(t[i]==c[0] && v) {
//                    s[j]=c2[0]; j++;
//                    s[j]=c[0]; j++;
//                    v--;
//                }
//                while(t[i]==c[1] && o) {
//                    s[j]=c2[1]; j++;
//                    s[j]=c[1]; j++;
//                    o--;
//                }
//                while(t[i]==c[2] && g) {
//                    s[j]=c2[2]; j++;
//                    s[j]=c[2]; j++;
//                    g--;
//                }
            }
        }

        printf("%s\n", s);

    }

    return 0;
}
