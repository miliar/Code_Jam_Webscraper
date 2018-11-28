#include <bits/stdc++.h>
using namespace std;

#define len(x)  (int((x).size()))
#define append push_back
#define pp make_pair
#define ff(a, b)    for (int a = 0; a < int(b); ++a)
#define kk(n)    ff(k, n)
#define xx(n)    ff(x, n)
#define yy(n)    ff(y, n)
#define ii(n)    ff(i, n)
#define fff(a, b, c) for (int a = int(b); a < int(c); ++a)
#define kkk(a, b) fff(k, a, b)
#define xxx(a, b) fff(x, a, b)
#define yyy(a, b) fff(y, a, b)
#define iii(a, b) fff(i, a, b)
#define bb begin()
#define ee end()
#define uu first
#define vv second
#define all(x)  (x).bb, (x).ee
#define ite(v)   decltype((v).bb)
#define fe(i, v) for(ite(v) i = (v).bb; i != (v).ee; ++i)
#define err(...)    { fprintf(stderr, __VA_ARGS__); fflush(stderr); }
#define zz(array, byte)   memset(array, byte, sizeof(array));

using LL = long long;
using DD = long double;
using pii = pair<int, int>;


const LL  INFLL  = 0x7f7f7f7f7f7f7f7fLL;
const int INFint = 0x7f7f7f7f;  //Works with memset(..).
   




int main() {
    //ios_base::sync_with_stdio(false);     cin.tie(NULL);
    //cout << '\n';     //Avoid flushing with endl.
    cout.precision(16);


    int ncases;
    cin >> ncases;

    fff (icase, 1, ncases+1) {
        int N, Q;
        cin >> N >> Q;
        vector<LL> limits(N);
        vector<int> speeds(N);
        vector<vector<double> > dists(N, vector<double>(N, -1));
        
        ii (N)
            cin >> limits[i] >> speeds[i];
        ii (N)
            kk (N) {
                cin >> dists[i][k];
                if (dists[i][k] < 0)
                    dists[i][k] = 1e100;
            }

        kk (N)
        xx (N)
        yy (N)
            dists[x][y] = min(dists[x][y], dists[x][k] + dists[k][y]);

        xx (N)
        yy (N) {
            if (dists[x][y] > limits[x]) {
                dists[x][y] = 1e100;
                continue;
            }
            dists[x][y] = double(dists[x][y]) / speeds[x];
        }
        
        kk (N)
        xx (N)
        yy (N)
            dists[x][y] = min(dists[x][y], dists[x][k] + dists[k][y]);

        printf("Case #%d:", icase);
        ff (iq, Q) {
            int u, v;
            cin >> u >> v;
            printf(" %.15g", dists[u-1][v-1]);
        }
        printf("\n");
    }
    

    return 0;
}


