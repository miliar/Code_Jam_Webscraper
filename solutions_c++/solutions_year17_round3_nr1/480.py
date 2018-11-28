#include <bits/stdc++.h>

using namespace std;

# define M_PI 3.14159265358979323846

typedef pair<double, double> pd;

struct pancake {
    int r;
    int h;
    double surface_area;
    double lateral_area;

    bool operator<(const struct pancake &b) const {
        return tie(r, h) > tie(b.r, b.h);
    }
};

double calc_lateral(double r, double h) {
    return 2 * M_PI * r * h;
}

double calc_surface(double r) {
    return M_PI * r * r;
}

int main() {
    int T;
    cin >> T;
    for (int t = 1; t <= T; t++) {
        int K, N;
        cin >> N >> K;
        vector<struct pancake> pancakes;
        for (int i = 0; i < N; i++) {
            int r, h;
            cin >> r >> h;
            pancakes.push_back({r, h, calc_surface(r), calc_lateral(r, h)});
        }
        sort(pancakes.begin(), pancakes.end());
        double ans = -1;
        for (int i = 0; i <= N - K; i++) {
            double curr = pancakes[i].surface_area + pancakes[i].lateral_area;
            priority_queue<double> laterals;
            for (int j = i + 1; j < N; j++) {
                laterals.push(pancakes[j].lateral_area);
            }
            for (int l = 0; l < K - 1; l++) {
                curr += laterals.top();
                laterals.pop();
            }
            if (ans == -1)
                ans = curr;
            else
                ans = max(ans, curr);
        }
        printf("Case #%d: %.8lf\n", t, ans);
    }
    return 0;
}
