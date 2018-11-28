#include <iostream>
#include <vector>

using namespace std;

int n;
double d;
vector<pair<double, double>> a;

void load() {
    a.clear();
    cin >> d >> n;
    for (int i = 0, k, s;i < n;i++) {
        cin >> k >> s;
        a.push_back(make_pair(k, s));
    }
    sort(a.begin(), a.end());
    a.push_back(make_pair(d, 0));
}


bool check(vector<pair<double, double>> & a) {
    int n = a.size();
    for (int i = 0;i < n - 2;i++) {
        double mint = 1e100;
        int pos = -1;
        for (int j = 0;j < n - 1;j++) {
            if (a[j].second <= a[j + 1].second) continue;
            double ct = (a[j + 1].first - a[j].first) / double(a[j].second - a[j + 1].second);
            if (ct < mint) {
                mint = ct;
                pos = j;
            }
        }
        if (pos == 0) {
            return false;
        }
        a.erase(a.begin() + pos);
        for (int i = 0;i < (int)a.size();i++) {
            a[i].first += a[i].second * mint;
        }
    }
    return true;
}

void solve(int test) {
    double l = 0, r = 1e18;
    for (int it = 0;it < 200;it++) {
        double mid = (l + r) / 2;
        auto b = a;
        b.push_back(make_pair(0, mid));
        sort(b.begin(), b.end());
        if (check(b)) {
            l = mid;
        } else {
            r = mid;
        }
    }

    printf("Case #%d: %.8lf\n", test, (l + r) / 2);
}

int main() {
#ifdef VALERA
    freopen("a.in", "r", stdin);
#endif
    int t;
    cin >> t;

    for (int i = 0;i < t;i++) {
        load();
        solve(i + 1);
    }
    return 0;
}
