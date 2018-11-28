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

double dp[1001][1001];

int main() {
    const double pi = 3.14159265358979323846;
    int T;
    cin >> T;
    for (int test = 0; test < T; test++) {
        int N, K;
        cin >> N >> K;
        vector<pair<double,double> > P;
        for (int i = 0; i < N; i++) {
            double r, h;
            cin >> r >> h;
            P.push_back(mp(r, h));
        }
        sort(all(P), [](pair<double,double> a, pair<double,double> b){return a.first > b.first;});


        for (int i = 0; i < 1001; i++) {
            for (int j = 0; j < 1001; j++) {
                dp[i][j] = 0;
            }
        }

        for (int i = 0; i < N; i++) {
            for (int k = 0; k <= K; k++) {
                double temp = 0;
                if (k == 0) temp = P[i].first * P[i].first * pi;

                if (k != K) dp[i + 1][k + 1] = max(dp[i + 1][k + 1], dp[i][k] + pi * 2 * P[i].first * P[i].second + temp);
                dp[i + 1][k] = max(dp[i + 1][k], dp[i][k]);
            }
        }

        printf("Case #%d: %20.19f\n", test + 1, dp[N][K]);


    }
    return 0;
}