#include <cmath>
#include <cassert>
#include <vector>
#include <set>
#include <string>
#include <queue>
#include <map>
#include <cstdio>
#include <cstdlib>
#include <cstring>
#include <algorithm>
#include <iostream>
#include <cassert>
//#include <functional>

using namespace std;
#define MP make_pair
typedef pair<int,int> PII;
typedef vector<int> VI;
typedef vector<VI> VVI;
typedef long long LL;

#define REP (i, s, t) for (int i = (s); i < (t); i++)

struct Act {
    int b, e;
    int i;
    Act(int b,int e,int i): b(b),e(e),i(i) {}
    bool operator<(const Act&other) const {
        return b < other.b;
    }
};
vector<Act> acts;

int dp[201][2001];


int main () {
    int t;
    int INF = 9999999;
    cin >> t;
    for (int i = 1; i <= t; i++) {
        acts = decltype(acts)();
        int ac, cj;
        cin >> ac >> cj;
        int b,e;
        for (int i = 0; i < ac; i++) {
            cin >> b >> e;
            acts.push_back(Act(b,e,0));
        }
        for (int i = 0; i < cj; i++) {
            cin >> b >> e;
            acts.push_back(Act(b,e,1));
        }
        sort(acts.begin(),acts.end());
        acts.push_back(Act(acts[0].b+1440,acts[0].e+1440,acts[0].i));
        for (int i = 0; i < 201; i++) {
            for (int j = 0; j < 2000; j++) {
                dp[i][j]=INF;
            }
        }
        int n = ac+cj;
        dp[n][720] = 0;
        for (int i = n-1; i>= 0; i--) {
            if (acts[i].i == acts[i+1].i) {
                int dt = (acts[i+1].b - acts[i].b);
                dt = acts[i].i==0?dt:-dt;
                int swing = (acts[i+1].b-acts[i].e) - (acts[i].e-acts[i].b);
                swing = (acts[i].i==0?-swing:swing);
                //printf("%d %d\n", dt, swing);
                for (int j = 0; j <= 720*2; j++) {
                    if (dp[i+1][j] < INF) {
                        if (j+dt >= 0 && j+dt <= 1440) {
                            dp[i][j+dt] = min(dp[i][j+dt],dp[i+1][j]);
                            //printf("dp[%d][%d] = %d\n", i,j+dt,dp[i][j+dt]);
                        }
                        for (int dd = max(0,j+min(dt,swing));dd<=min(1440,j+max(dt,swing));dd++) {
                            dp[i][dd] = min(dp[i][dd],dp[i+1][j]+2);
                        }
                    }
                }
            } else {
                int dt = (acts[i+1].b - acts[i].b);
                dt = acts[i].i==0?dt:-dt;
                int swing = (acts[i+1].b-acts[i].e) - (acts[i].e-acts[i].b);
                swing = (acts[i].i==0?-swing:swing); 
                for (int j = 0; j <= 720*2; j++) {
                    if (dp[i+1][j] < INF) {
                        for (int dd = max(0,j+min(dt,swing));dd<=min(1440,j+max(dt,swing));dd++) {
                            dp[i][dd] = min(dp[i][dd],dp[i+1][j]+1);
                        }
                    }
                }
            }
        }
        for (int i = 0; i < n; i++) {
            int ll=1441, rr=0;
            for (int j = 0; j <= 1440; j++) {
                if (dp[i][j]<INF) {
                    ll=min(ll,j);rr=max(rr,j);
                }
            }
            //printf("%d: %d ~ %d\n", i, ll-720, rr-720);
        }
        printf("Case #%d: %d\n", i, dp[0][720]);
    }
}
