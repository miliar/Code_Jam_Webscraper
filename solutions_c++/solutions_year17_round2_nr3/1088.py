#include <iostream>
#include <vector>
#include <utility>
#include <algorithm>

using namespace std;

struct horse {
    int idx;
    int k;
    int s;
};

bool comp(const horse &lhs, const horse &rhs) {
    if(lhs.s == rhs.s) {
        if(lhs.k == rhs.k) {
            return lhs.idx < rhs.s;
        }

        return lhs.k > rhs.k;
    }

    return lhs.s > rhs.s;
}

int main() {
    int T;
    cin >> T;
    for(int cs=1; cs<=T; cs++) {
        int N,Q;
        cin >> N >> Q;

        vector<horse> v(N);
        for(int i=0;i<N;i++) {
            v[i].idx = i;
            cin >> v[i].k >> v[i].s;
        }

        int dist[105] = {0,};
        int aaa;
        for(int i=0;i<N;i++) {
            for(int j=0;j<N;j++) {
                cin >> aaa;
                if(i+1 == j) {
                    dist[i]=aaa;
                }
            }
        }

        for(int i=0;i<Q;i++) {
            cin >> aaa >> aaa;
        }

        double dd[1000] = {0,};
        for(int i=1;i<=N;i++) {
            double ans = 1.E15;
            for(int j=i-1;j>=0;j--) {
                double dist_sum = 0;
                for(int k=j;k<i;k++) dist_sum += dist[k];
                if(dist_sum > v[j].k) continue;

                ans = min(ans, dd[j] + dist_sum*1. / v[j].s);
            }

            dd[i] = ans;
        }

        printf("Case #%d: %.7f\n", cs, dd[N]);
    }

    return 0;
}
