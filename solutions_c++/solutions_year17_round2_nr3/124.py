#define STRINGIZE(x) #x
#define STRINGIZE2(x) STRINGIZE(x)
#define FP STRINGIZE2(FILEPATH)

#include <iostream>
#include <cstdio>
#include <cassert>
#include <string>
#include <vector>
#include <queue>
using namespace std;

const long long INF64 = 1e18;

const int N = 1000 + 3;

int n, q;
int e[N], s[N];
long long d[N][N];
int start[N], finish[N];

bool read() {
    if (scanf("%d%d", &n, &q) != 2) {
        return false;
    }
    for (int i = 0; i < n; i++) {
        assert(scanf("%d%d", &e[i], &s[i]) == 2);
    }
    for (int i = 0; i < n; i++) {
        for (int j = 0; j < n; j++) {
            int x;
            assert(scanf("%d", &x) == 1);
            if (x < 0) {
                d[i][j] = INF64;
            } else {
                d[i][j] = x;
            }
        }
        
        d[i][i] = 0;
    }
    for (int i = 0; i < q; i++) {
        assert(scanf("%d%d", &start[i], &finish[i]) == 2);
        start[i]--;
        finish[i]--;
    }
    return true;
}

double dist[N];
bool used[N];

void solve(int test) {
    printf("Case #%d:", test + 1);
    
    for (int k = 0; k < n; k++) {
        for (int i = 0; i < n; i++) {
            for (int j = 0; j < n; j++) {
                d[i][j] = min(d[i][j], d[i][k] + d[k][j]);
            }
        }
    }
    
    for (int Q = 0; Q < q; Q++) {
        for (int i = 0; i < n; i++) {
            dist[i] = 1e20;
            used[i] = false;
        }
        
        dist[start[Q]] = 0;
        
        while (true) {
            int idx = -1;
            for (int i = 0; i < n; i++) {
                if (!used[i] && (idx == -1 || dist[i] < dist[idx])) {
                    idx = i;
                }
            }
            
            if (idx == -1 || dist[idx] > 5e19) {
                break;
            }
            used[idx] = true;
            
            for (int i = 0; i < n; i++) {
                long long pathDist = d[idx][i];
                if (pathDist > e[idx]) {
                    continue;
                }
                double time = pathDist / double(s[idx]);
                if (dist[i] > dist[idx] + time) {
                    dist[i] = dist[idx] + time;
                }
            }
        }
        
        if (dist[finish[Q]] > 5e19) {
            throw;
        }
        printf(" %.10lf", dist[finish[Q]]);
    }
    puts("");
}

int main() {
    freopen(FP "input.txt", "rt", stdin);
    freopen(FP "output.txt", "wt", stdout);
    
    int testCount;
    cin >> testCount;
    
    for (int test = 0; test < testCount; test++) {
        assert(read());
        solve(test);
    }
    
    return 0;
}
