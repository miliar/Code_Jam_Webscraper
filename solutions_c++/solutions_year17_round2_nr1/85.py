#include<bits/stdc++.h>

using namespace std;

#define mp(x,y) make_pair(x, y)
#define For(i, n) for (int i = 0; i < (int) n; i++)

typedef long long ll;
typedef vector<int> vi;
typedef pair<int, int> pii;

int main () {
    int T;
    cin >> T;
    For(cases, T) {
        int n;
        double d;
        cin >> d >> n;
        vector<pair<double, double> > horse(n);
        For(i, n) cin >> horse [i].first >> horse [i].second;

        double maxtime = -1;
        For(i, n) {
            maxtime = max(maxtime, (d - horse [i].first) / horse [i].second);
        }
        printf("Case #%d: %.6lf\n", cases + 1, d / maxtime);
    }
}
