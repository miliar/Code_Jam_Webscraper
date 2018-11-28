#include <bits/stdc++.h>

#define FOR(i, p, n) for(int i = (int)(p); i < (int)(n); ++i)
#define FORD(i, p, n) for(int i = (int)(p); i >= (int)(n); --i)
#define UMAP unordered_map

using namespace std;

typedef long long LL;
typedef pair <int, int> PII;

const int N = 1e3 + 5;
const double INF = 1e9;

pair <double, double> horse[N];
int n;
double d;

double find_min() {
    double t = 1e9;
    FOR(i, 0, n - 1) {
        double x1 = horse[i].first, v1 = horse[i].second;
        double x2 = horse[i + 1].first, v2 = horse[i + 1].second;
        if (x1 > d) break;
        if (x2 > d) t = min(t, (d - x1) / v1);
        else if (v1 <= v2) t = min(t, (d - x1) / v1);
        else {
            if (x1 + v1 * ((x2 - x1) / (v1 - v2)) > d) t = min(t, (d - x1) / v1);
            else t = min(t, (x2 - x1) / (v1 - v2));
        }
    }
    if (horse[n - 1].first < d) t = min(t, (d - horse[n - 1].first) / horse[n - 1].second);
    return t;
}

void move_on(double t) {
    FOR(i, 0, n) horse[i].first += horse[i].second * t;
}

void update_speeds() {
    map <double, double> mapper;
    FOR(i, 0, n) if (!mapper.count(horse[i].first)) mapper[horse[i].first] = horse[i].second;
    else mapper[horse[i].first] = min(mapper[horse[i].first], horse[i].second);
    FOR(i, 0, n) horse[i].second = mapper[horse[i].first];
}

bool solve() {
    scanf("%lf %d", &d, &n);
    FOR(i, 0, n) scanf("%lf %lf", &horse[i].first, &horse[i].second);
    sort(horse, horse + n);
    if (n == 1) {
        printf("%.10lf\n", d / ((d - horse[0].first) / horse[0].second));
    } else {
        double cur_time = 0;
        while (horse[0].first < d) {
            double t = find_min();
            move_on(t);
            update_speeds();
            cur_time += t;
        }
        printf("%.10lf\n", d / cur_time);
    }

    return 0;
}

int main() {
    freopen("input", "r", stdin);
    freopen("output", "w", stdout);
    int t;
    cin >> t;
    FOR(i, 1, t + 1) {
        printf("Case #%d: ", i);
        solve();
    }

    return 0;
}
