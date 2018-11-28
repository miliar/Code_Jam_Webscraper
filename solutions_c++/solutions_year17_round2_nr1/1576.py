#include <bits/stdc++.h>

using namespace std;

const int maxn = 2000;

struct point {
    int speed;
    long double position;
    long double pos2;
    long double tim;

    point() {}

    point(int s, long double p1, long double p2) {
        speed = s;
        position = p1;
        pos2 = p2;
        tim = (p2 - p1) / s;
    }

};

long double crashspeed(long double p1, long double p2, int v2, long double d) {
    return v2 * (p2 - p1) / (d - p2) + v2;
}

int k[maxn], s[maxn];
pair<int, int> pairs[maxn];

int main() {
    freopen("A-small-attempt0.in", "r", stdin);
    freopen("A-small-attempt0.out", "w", stdout);

    ios_base::sync_with_stdio(false);
    cin.tie(0);

    int t;
    cin >> t;
    cout.precision(20);
    for (int z = 0; z < t; ++z) {
        int d, n;
        cin >> d >> n;
        for (int i = 0; i < n; ++i) {
            cin >> pairs[i].first >> pairs[i].second;
        }
        sort(pairs, pairs + n);
        for (int i = 0; i < n; ++i) {
            k[i] = pairs[i].first;
            s[i] = pairs[i].second;
        }
        vector<point> v;
        v.push_back(point(s[n - 1], k[n - 1], d));
        for (int i = n - 2; i >= 0; --i) {
            long double cur = k[i];
            while (v.size() && s[i] <= v.back().speed) {
                cur += v.back().tim * s[i];
                v.pop_back();
            }

            while (true) {
                if (v.size() == 0) {
                    v.push_back(point(s[i], k[i], d));
                    break;
                }
                long double t = (v.back().position - cur) / (s[i] - v.back().speed);
                if (t <= v.back().tim) {
                    v.back().tim -= t;
                    v.back().position += t * v.back().speed;
                    v.push_back(point(s[i], k[i], v.back().position));
                    break;
                } else {
                    v.pop_back();
                    cur += t * s[i];
                }
            }
        }

        long double l = 0, r = crashspeed(0, v.back().position, v.back().speed, d) + 1;
        for (int j = 0; j < 1000; ++j) {
            long double m = (l + r) / 2;
            long double cur = 0;
            bool ok = true;
            for (int i = v.size() - 1; i > 0; --i) {
                if (crashspeed(cur, v[i].position, v[i].speed, v[i - 1].position) < m) {
                    ok = false;
                    break;
                }
                cur += m * v[i].tim;
            }
            if (crashspeed(cur, v[0].position, v[0].speed, d) < m) {
                ok = false;
            }
            if (ok) {
                l = m;
            } else {
                r = m;
            }
        }

        cout << "Case #" << z + 1 << ": ";
        cout << l << "\n";

    }



    return 0;
}
