#include <cstdio>
#include <vector>
using namespace std;

int N, M, C;

bool solve(int mid, vector< pair<int, int> > &edges, int &cost) {
    bool can = true;
    vector<int> ds(C);
    for(int i = 0; i < edges.size(); i++) {
        ds[edges[i].second] ++;
    }
    for(int i = 0; i < C; i++) 
        if (ds[i] > mid) 
            return false;
    vector<int> g(N);
    for(int i = 0; i < edges.size(); i++) {
        g[edges[i].first] += 1;
    }
    int leftover = 0; cost = 0;
    for(int i = N - 1; i >= 0; i--) {
        int cnt = g[i];        
        if (cnt < mid) {
            int left = min(mid - cnt, leftover);
            cost += left;
            leftover -= left;

        } else {
            leftover += cnt - mid;
        }
    }
    if (leftover > 0) return false;
    return true;
}

int main() {
    int T; scanf("%d", &T); int test_id = 0;
    while(test_id < T) { test_id ++;
        printf("Case #%d: ", test_id);
        vector< pair<int, int> > edges;
        scanf("%d %d %d", &N, &C, &M);
        for(int i = 0; i < M; i++) {
            int a, b;
            scanf("%d %d", &a, &b);
            a--, b--;
            edges.push_back(make_pair(a, b));
        }

        int l = 0, r = M;
        while(r - l > 1) {
            int mid = (l + r) >> 1;
            int cost = 0;
            if (solve(mid, edges, cost)) r = mid;
            else l = mid;
        }
        
        int cost = 0;
        solve(r, edges, cost);

        printf("%d %d\n", r, cost);
    }
}
