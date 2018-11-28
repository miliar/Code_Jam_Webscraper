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
        int n, q;
        cin >> n >> q;
        vector<vector<ll> > distances(n, vector<ll>(n, 0));
        vector<ll> maxd(n);
        vector<double> speed(n);
        For(i, n) cin >> maxd[i] >> speed [i];
        For(i, n) For(j, n) {
            cin >> distances [i][j];
            if (distances [i][j] == -1) distances [i][j] = 1023456789123456LL;
            if (i == j) distances [i][j] = 0;
        }
        For(k, n) For(i, n) For(j, n) distances [i][j] = min(distances [i][j], distances [i][k] + distances [k][j]);
        printf("Case #%d:", cases + 1);
        For(magic, q) {
            int from, to;
            cin >> from >> to;
            from --; to --;
            vector<double> arr_time(n, 1023456789123456789.0);
            arr_time [from] = 0.0;
            vector<bool> done(n, false);
            while(true) {
                double mintime = 1023456789123456789.0;
                int process = -1;
                for (int i = 0; i < n; i++) {
                    if (!done [i] && mintime > arr_time [i]) {
                        mintime = arr_time [i];
                        process = i;
                    }
                }
                done [process] = true;
                if (process == to) {
                    printf(" %.7lf", mintime);
                    break;
                }
                For(i, n) {
                    // Can we make it there?
                    if (!done [i] && distances [process] [i] <= maxd [process]) {
                        arr_time [i] = min(arr_time [i], mintime + double(distances[process][i])/speed [process]);
                    }
                }
            }
        }
        printf("\n");
    }
}
