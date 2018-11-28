#include <stdio.h>
#include <iostream>
#include <string>
#include <vector>
#include <algorithm>
#include <queue>
using namespace std;

int N;
int Q;
double HD[100];
double HS[100];
double matrix[100][100];
bool used[100][100];
struct State {
    int horse;
    double dist;
    int city;
    operator < (const State& s) const { return s.dist < dist; }
};
priority_queue<std::pair<double, State>> q;

void reset() { 
    while (!q.empty()) q.pop();
    for (int i = 0; i < N; i++) {
        for (int j = 0; j < N; j++) {
            used[i][j] = false;
        }
    }
}

double find(int end) {
    while (!q.empty()) {
        double d = -q.top().first;
        State s = q.top().second;
        q.pop();
        if (used[s.city][s.horse]) continue;
        if (HD[s.horse] < s.dist) continue;
        if (s.city == end) return d;
        used[s.city][s.horse] = true;
//        printf("%lf -> %d %lf %d\n", d, s.horse, s.dist, s.city);
        for (int j = 0; j < N; j++) {
            if (matrix[s.city][j] > -0.5) {
                double dist = matrix[s.city][j];
                q.push({-d - dist / HS[s.horse], {s.horse, s.dist + dist, j}});
                q.push({-d - dist / HS[s.city], {s.city, dist, j}});
            }
        }
    }
    return -1.0;
}

void solve() {
    scanf("%d %d", &N, &Q);
    for (int i = 0; i < N; i++) {
        scanf("%lf %lf", &HD[i], &HS[i]);
    }
    for (int i = 0; i < N; i++) {
        for (int j = 0; j < N; j++) {
            scanf("%lf", &matrix[i][j]);
            used[i][j] = false;
        }
    }
    for (int i = 0; i < Q; i++) {
        int s, e;
        scanf("%d %d", &s, &e);s--; e--;
        reset();
        q.push({0.0, {s, 0, s}});
        printf(" %lf", find(e));
    }
}

int main() {
  int T;
  scanf("%d", &T);
  for (int t = 1; t <= T; t++) {
    cout << "Case #" << t << ": ";
    solve();
    cout << "\n";
  }
  return 0;
}
