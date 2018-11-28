#include<iostream>
#include<algorithm>
#include<iomanip>
using namespace std;
double d;
int n;
struct horse {
    double k,s;
};
horse h[10005];
bool cmp (horse a, horse b) {
    if (a.k > b.k) return true; else if (a.k < b.k) return false; else return a.s > b.s;
}
int main() {
    int T;
    cin >> T;
    for (int ca = 1; ca <= T; ++ca) {
        cin >> d >> n;
        for (int i = 0; i < n; ++i) {
            cin >> h[i].k >> h[i].s;
        }
        sort(h, h + n, cmp);
        double time = -1;
        for (int i = 0; i < n; ++i) {
            double t = (d - h[i].k) / h[i].s;
            if (t > time) time = t;
        }
        cout << "Case #" << ca << ": " << setprecision(15) << d / time << endl;
    }
}