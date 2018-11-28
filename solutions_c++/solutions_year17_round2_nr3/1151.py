#include <iostream>
#include <iomanip>
#include <algorithm>
#include <vector>
#include <queue>
using namespace std;

typedef pair<long long, long long> pi;
int T;
long long N, Q;
long long E[105], S[105];
long long adjMat[105][105];
long long U, V;
long double DP[105];
long long P[105], D[105];

int main() {
    ios::sync_with_stdio(0);
    cin.tie(0);
    cin >> T;
    for (int TC = 1; TC <= T; ++TC) {
        cin >> N >> Q;
        for (int a = 1; a <= N; ++a)
            cin >> E[a] >> S[a];
        for (int a = 1; a <= N; ++a)
            for (int b = 1; b <= N; ++b)
                cin >> adjMat[a][b];
        cout << "Case #" << TC << ": ";
        for (int QQ = 0; QQ < Q; ++QQ) {
            cin >> U >> V;
            // Dijkstra
            priority_queue<pi, vector<pi>, greater<pi>> pq; // Cost, Node
            for (int a = 1; a <= N; ++a) D[a] = -1;
            D[U] = 0;
            P[U] = -1;
            pq.emplace(0, U);
            while (!pq.empty()) {
                pi top = pq.top();
                pq.pop();
                if (top.second == V) break;
                if (D[top.second] != top.first) continue;
                for (int a = 1; a <= N; ++a) {
                    if (adjMat[top.second][a] == -1) continue;
                    int ND = top.first + adjMat[top.second][a];
                    if (D[a] == -1 || D[a] > ND) {
                        D[a] = ND;
                        P[a] = top.second;
                        pq.emplace(ND, a);
                    }
                }
            }
            // Retrieve the path
            vector<int> path;
            int X = V;
            for (; ~ X; X = P[X]) {
                path.push_back(X);
            }
            reverse(path.begin(), path.end());
            long long PSUM[105] = {0};
            for (int a = 1; a < (int)path.size(); ++a) {
                PSUM[a] = PSUM[a - 1] + adjMat[path[a - 1]][path[a]];
            }
            // Construct jumps
            vector<long long> JMP[105];
            for (int a = 0; a < (int)path.size(); ++a) {
                for (int b = a + 1; b < (int)path.size(); ++b) {
                    // Calculate this distance...
                    long long DST = PSUM[b] - PSUM[a];
                    if (DST > E[path[a]]) break; // Too far
                    JMP[b].push_back(a); // Can jump to here
                }
            }
            // Reset DP array
            for (int a = 0; a < (int)path.size(); ++a)
                DP[a] = -1;
            DP[0] = 0;
            for (int a = 1; a < (int)path.size(); ++a) {
                for (auto B: JMP[a]) {
                    long long dist = PSUM[a] - PSUM[B];
                    long double NC = DP[B] + (long double)dist / (long double)S[B + 1];
                    if (DP[a] < 0) DP[a] = NC;
                    else DP[a] = min(DP[a], NC);
                }
            }
            if (QQ) cout << " ";
            cout << fixed << setprecision(9) << DP[path.size() - 1] << "\n";
        }
    }
    return 0;
}
