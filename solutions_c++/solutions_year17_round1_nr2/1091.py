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

int r[60], q[60][60];
double mmin[60], mmax[60];
int it[60];

int main(){

    int t;
    ri(t);

    for(int cas=1; cas<=t; cas++) {

        int n,p;
        rii(n,p);

        for(int i=1; i<=n; i++)
            ri(r[i]);
        for(int i=1; i<=n; i++) {
            for(int j=1; j<=p; j++) 
                ri(q[i][j]);
            sort(&q[i][1], &q[i][1]+p);
        }
        for(int i=1; i<=n; i++) {
            it[i] = 1;
            mmin[i] = (double)q[i][1] / ((double)r[i] * 1.1);
            mmax[i] = (double)q[i][1] / ((double)r[i] * 0.9);
        }

        int ans = 0;
        while(true) {
            double imin = 0, imax=100000000;
            double minmax = 100000000;
            int minmaxi = 0;
            int cul = 0;
            for(int i=1; i<=n; i++) {
//                cout << "imin,imax: " << imin << " " << imax << endl;
//                cout << "mmin[i], mmax[i]: " << mmin[i] << " " << mmax[i] << endl;
                if(ceil(mmin[i]) > floor(mmax[i])
                        || floor(mmax[i])<imin){
                    cul = i;
//                    cout << "break" << endl;
                    break;
                }
                if(ceil(mmin[i])>imax){
                    cul = minmaxi;
                    break;
                }
                
                if(floor(mmax[i])<minmax) {
                    minmax = floor(mmax[i]);
                    minmaxi = i;
                }
                imin = max(imin, ceil(mmin[i]));
                imax = min(imax, floor(mmax[i]));
            }
            if(cul) {
//                cout << "cul: " << cul << " it[cul]: " << it[cul] << ", p: " << p << endl;
                if(it[cul]==p)
                    break;
                it[cul]++;
                //mmin[cul] = 0.9 * (double)q[cul][it[cul]] / (double)r[cul];
                //mmax[cul] = 1.1 * (double)q[cul][it[cul]] / (double)r[cul];
                mmin[cul] = (double)q[cul][it[cul]] / ((double)r[cul] * 1.1);
                mmax[cul] = (double)q[cul][it[cul]] / ((double)r[cul] * 0.9);
//                cout << "new mmin,mmax: " << mmin[cul] << " " << mmax[cul] << endl;
            } else {
                ans++;
                int ok = 1;
                for(int i=1; i<=n; i++) {
                    if(it[i]==p) {
                        ok = 0;
                        break;
                    }
                    it[i]++;
                    mmin[i] = (double)q[i][it[i]] / ((double)r[i] * 1.1);
                    mmax[i] = (double)q[i][it[i]] / ((double)r[i] * 0.9);
                    //mmin[i] = 0.9 * (double)q[i][it[i]] / (double)r[i];
                    //mmax[i] = 1.1 * (double)q[i][it[i]] / (double)r[i];
                }
                if(!ok) break;
            }
        }

        printf("Case #%d: %d\n", cas, ans);
    }

    return 0;
}
