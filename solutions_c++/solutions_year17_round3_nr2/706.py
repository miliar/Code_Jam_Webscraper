#include <map>
#include <set>
#include <list>
#include <cmath>
#include <queue>
#include <stack>
#include <cstdio>
#include <string>
#include <vector>
#include <complex>
#include <cstdlib>
#include <cstring>
#include <numeric>
#include <sstream>
#include <iostream>
#include <algorithm>
#include <functional>
  
#define mp       make_pair
#define pb       push_back
#define all(x)   (x).begin(),(x).end()
#define rep(i,n) for(int i=0;i<(n);i++)


using namespace std;
  
typedef    long long          ll;
typedef    unsigned long long ull;
typedef    vector<bool>       vb;
typedef    vector<int>        vi;
typedef    vector<vb>         vvb;
typedef    vector<vi>         vvi;
typedef    pair<int,int>      pii;
  
const int INF=1<<29;
const double EPS=1e-9;
  
const int dx[]={1,0,-1,0,1,1,-1,-1},dy[]={0,-1,0,1,1,-1,-1,1};

int dp1[60 * 24 + 1][30 * 24 + 1][2];
int dp2[60 * 24 + 1][30 * 24 + 1][2];
int fc[60 * 24 + 1];
int fj[60 * 24 + 1];

int main() {
    int T;
    cin >> T;
    for (int test = 0; test < T; test++) {
        int A_c, A_j;
        cin >> A_c >> A_j;

        for (int i = 0; i < 60 * 24 + 1; i++) {
            fc[i] = 0;
            fj[i] = 0;
            for (int j = 0; j < 30 * 24 + 1; j++) {
                dp1[i][j][0] = dp1[i][j][1] = INF;
                dp2[i][j][0] = dp2[i][j][1] = INF;
            }
        }

        for (int i = 0; i < A_c; i++) {
            int l, r;
            cin >> l >> r;
            for(int j = l; j < r; j++) {
                fc[j] = 1;
            }
        }
        for (int i = 0; i < A_j; i++) {
            int l, r;
            cin >> l >> r;
            for(int j = l; j < r; j++) {
                fj[j] = 1;
            }
        }
        int ans = INF;
        if (fc[0] == 0) {
            dp1[0][0][0] = 0;
            for (int i = 0; i < 60 * 24; i++) {
                for (int j = 0; j <= 30 * 24; j++) {
                    if (fc[i + 1] == 0) {
                        if (j != 30 * 24) dp1[i + 1][j + 1][0] = min(dp1[i + 1][j + 1][0], dp1[i][j][0]);
                        dp1[i + 1][j][0] = min(dp1[i + 1][j][0], dp1[i][j][1] + 1);
                    }
                    if (fj[i + 1] == 0) {
                        dp1[i + 1][j][1] = min(dp1[i + 1][j][1], dp1[i][j][1]);
                        if (j != 30 * 24) dp1[i + 1][j + 1][1] = min(dp1[i + 1][j + 1][1], dp1[i][j][0] + 1);
                    }
                }
            }
            ans = min(ans, min(dp1[60 * 24][30 * 24][0], dp1[60 * 24][30 * 24][1] + 1));
        }
        if (fj[0] == 0) {
            dp2[0][0][1] = 0;
            for (int i = 0; i < 60 * 24; i++) {
                for (int j = 0; j <= 30 * 24; j++) {
                    if (fc[i + 1] == 0) {
                        if (j != 30 * 24) dp2[i + 1][j + 1][0] = min(dp2[i + 1][j + 1][0], dp2[i][j][0]);
                        dp2[i + 1][j][0] = min(dp2[i + 1][j][0], dp2[i][j][1] + 1);
                    }
                    if (fj[i + 1] == 0) {
                        dp2[i + 1][j][1] = min(dp2[i + 1][j][1], dp2[i][j][1]);
                        if (j != 30 * 24) dp2[i + 1][j + 1][1] = min(dp2[i + 1][j + 1][1], dp2[i][j][0] + 1);
                    }
                }
            }
            ans = min(ans, min(dp2[60 * 24][30 * 24][1], dp2[60 * 24][30 * 24][0] + 1));
        }
        printf("Case #%d: %d\n", test + 1, ans);
        

    }
    return 0;
}