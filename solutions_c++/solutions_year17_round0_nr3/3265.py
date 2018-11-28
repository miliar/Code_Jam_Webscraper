#include <iostream>
#include <string>
#include <sstream>
#include <vector>
#include <algorithm>
#include <map>
#include <cstdlib>
#include <cstdio>
#include <complex>
#include <queue>
#include <stack>
using namespace std;
typedef long long unsigned int ll;

#define REP(i,n) for(int i=0; i<(int)n; i++)
#define rep(n) REP(i,n)
#define EPS (1e-7)
#define INF 1e9
#define PI (acos(-1))

int main() {
    int T,tt = 0;
    cin>>T;
    while(tt++ < T) {
        ll N,K; cin>>N>>K;
        priority_queue<ll> q; // 99,98,97,... (push(), top(), pop(), empty())
        q.push(N);
        ll res_max = 0;
        ll res_min = 0;
        while(K--) {
            ll len = q.top(); q.pop();
            ll left,right;
            if(len % 2 == 0) { // even
                left = len / 2 - 1;
                right = len / 2;
            }
            else { // odd
                left = right = (len - 1) / 2;
            }

            res_max = max(left, right);
            res_min = min(left, right);

            if(left > 0) q.push(left);
            if(right > 0) q.push(right);
        }
        cout << "Case #" << tt << ": " << res_max << " " << res_min << endl;
    }
    return 0;
}
